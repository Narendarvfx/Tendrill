import datetime
import os

import requests
import xlsxwriter

token = '90cca45e7d7cc3f2ae98832d77ab6bc1978bbf12'
tl_data = requests.get('https://192.168.5.12/api/hrm/teams/', headers={'Authorization': 'token {}'.format(token)},
                       verify=False)

date = datetime.datetime.now().date()
for s, tl in enumerate(tl_data.json()):
    tl_details = requests.get('https://192.168.5.12/api/hrm/employee/' + str(tl['lead']) + '/',
                              headers={'Authorization': 'token {}'.format(token)}, verify=False)
    if not os.path.isdir('./{}'.format(date)):
        os.makedirs('./{}'.format(date))
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(
        './{}/OFX_{}_{}_{}_DAY END REPORT_{}.xlsx'.format(date,
                                                       tl_details.json()['department'],
                                                       tl_details.json()['fullName'], tl_details.json()['id'],date))
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True, 'bg_color': '#43d3f7', 'border': 1, 'border_color': 'black'})
    pending_color = workbook.add_format({'bg_color': 'yellow', 'border': 1, 'border_color': 'black'})
    border = workbook.add_format({'border': 1, 'border_color': 'black'})
    # Add a number format for cells with money.
    percent = workbook.add_format({'num_format': '0.0%', 'border': 1, 'border_color': 'black'})

    # Write some data headers.
    worksheet.write('A1', 'CLIENT', bold)
    worksheet.write('B1', 'PROJECT', bold)
    worksheet.write('C1', 'SHOT', bold)
    worksheet.write('D1', 'TOTAL FRAMES', bold)
    worksheet.write('E1', 'TASK', bold)
    worksheet.write('F1', 'STATUS', bold)
    worksheet.write('G1', 'BID DAYS', bold)
    worksheet.write('H1', 'WIP%', bold)
    worksheet.write('I1', 'PENDING MANDAYS', bold)
    worksheet.write('J1', 'DUE DATE', bold)
    worksheet.write('K1', 'NOTES', bold)
    worksheet.write('L1', 'TEAM', bold)
    worksheet.write('M1', 'ARTIST NAME', bold)

    tl_shot_data = requests.get('http://127.0.0.1:8000/api/production/leads/shots/' + str(tl['lead']) + '/',
                                headers={'Authorization': 'token {}'.format(token)}, verify=False)
    # # Start from the first cell below the headers.
    col = 0
    row = 0
    for shot_data in tl_shot_data.json():
        artist = []
        shot_status = shot_data['shot']['status']['code']
        if shot_status == 'YTS' or shot_status == 'WIP' or shot_status == 'STQ' or shot_status == 'QIP' or shot_status == 'IAP' or shot_status == 'DTC':
            date_obj = datetime.datetime.strptime(shot_data['shot']['modified_date'], '%Y-%m-%dT%H:%M:%S.%f')
            form_date = date_obj.strftime('%Y-%m-%d')
            dates_list = []
            for i in range(0, datetime.datetime.now().isoweekday()):
                ok = datetime.datetime.today().date() - datetime.timedelta(days=i)
                dk = ok.strftime('%Y-%m-%d')
                dd = datetime.datetime.strptime(dk, '%Y-%m-%d')
                dates_list.append(dd)

            if shot_data['shot']['status']['code'] == "DTC" and datetime.datetime.strptime(form_date,
                                                                                           '%Y-%m-%d') not in dates_list:
                pass
            else:
                for task in shot_data['shot']['task']:
                    artist.append(task['artist']['fullName'])
                bid_column = 'G{}'.format(row + 2)
                progress_column = 'H{}'.format(row + 2)
                percentile = shot_data['shot']['progress'] / 100
                total_frames = shot_data['shot']['actual_end_frame'] - shot_data['shot']['actual_start_frame'] + 1
                due_date = datetime.datetime.strptime(shot_data['shot']['eta'], '%Y-%m-%dT%H:%M:%S').strftime(
                    "%d-%m-%Y")
                worksheet.write(row + 1, col, shot_data['shot']['sequence']['project']['client'], border)
                worksheet.write(row + 1, col + 1, shot_data['shot']['sequence']['project']['name'], border)
                worksheet.write(row + 1, col + 2, shot_data['shot']['name'], border)
                worksheet.write(row + 1, col + 3, str(total_frames), border)
                worksheet.write(row + 1, col + 4, shot_data['shot']['task_type'], border)
                worksheet.write(row + 1, col + 5, shot_data['shot']['status']['code'], border)
                worksheet.write(row + 1, col + 6, int(shot_data['shot']['bid_days']), border)
                worksheet.write(row + 1, col + 7, percentile, percent)
                worksheet.write(row + 1, col + 8,
                                '=ROUND(({}-{}*{}),1)'.format(bid_column, bid_column, progress_column), pending_color)
                worksheet.write(row + 1, col + 9, due_date, border)
                worksheet.write(row + 1, col + 10, " ", border)
                worksheet.write(row + 1, col + 11, tl_details.json()['fullName'], border)
                worksheet.write(row + 1, col + 12, ', '.join(artist), border)
                row += 1

    workbook.close()
