import os
import getpass
import xlsxwriter
import api

def get_status_counts(all_shots):
    yts = 0
    wip = 0
    approved = 0
    crt = 0
    for shot in all_shots:
        print(shot['status']['code'])
        if shot['status']['code'] in ['YTA','ATL','YTS']:
            yts += 1
        elif shot['status']['code'] in ['WIP', 'STQ', 'QIP', 'IAP', 'IRT']:
           wip += 1
        elif shot['status']['code'] in ['CAP']:
            approved += 1
        if shot['type'] == "CRT":
            crt += 1
    return yts, wip, approved, crt

def generate_report():
    user = getpass.getuser()
    file_path = r"C:\Users\{}\Documents\ofx_reports".format(user)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    path = file_path + '\studio_report.xlsx'
    workbook = xlsxwriter.Workbook(path)
    clients_data = api.get_all_clients()
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True, 'bg_color': '#43d3f7', 'border': 1, 'border_color': 'black'})
    pending_color = workbook.add_format({'bg_color': 'yellow', 'border': 1, 'border_color': 'black'})
    border = workbook.add_format({'border': 1, 'border_color': 'black'})
    # Add a number format for cells with money.
    percent = workbook.add_format({'num_format': '0.0%', 'border': 1, 'border_color': 'black'})
    worksheet = workbook.add_worksheet()
    # Write some data headers.
    worksheet.write('A1', 'CLIENT', bold)
    worksheet.write('B1', 'PROJECT', bold)
    worksheet.write('C1', 'TOTAL SHOTS', bold)
    worksheet.write('D1', 'ACTUAL MANDAYS', bold)
    worksheet.write('E1', 'ACHIEVED MANDAYS', bold)
    worksheet.write('F1', 'ACTUAL vs ACHIEVED', bold)
    worksheet.write('G1', 'PROGRESS', bold)
    worksheet.write('H1', 'YTS', bold)
    worksheet.write('I1', 'WIP', bold)
    worksheet.write('J1', 'APPROVED', bold)
    worksheet.write('K1', 'RETAKES', bold)
    p = 1
    for c,client in enumerate(clients_data):
        all_projects = api.get_client_projects(client['id'])
        worksheet.write(c + p, 0, client['name'])
        for project in all_projects:
            # print(project)
            worksheet.write(c + p, 1, project['name'])
            all_shots = api.get_all_shots(project_id=project['id'])
            worksheet.write(c + p, 2, len(all_shots))
            act_mandays = sum(item['bid_days'] for item in all_shots)
            worksheet.write(c+p, 3, act_mandays)
            achived_mandays = sum(item['achieved_mandays'] for item in all_shots)
            worksheet.write(c+p, 4, achived_mandays)
            pending_mandays = act_mandays - achived_mandays
            worksheet.write(c + p, 5, pending_mandays)
            status_count = get_status_counts(all_shots)
            worksheet.write(c + p, 7, status_count[0])
            worksheet.write(c + p, 8, status_count[1])
            worksheet.write(c + p, 9, status_count[2])
            worksheet.write(c + p, 10, status_count[3])
            try:
                per = achived_mandays/act_mandays*100
            except ZeroDivisionError:
                per = 0
            worksheet.write(c + p, 6, str(round(per,2))+'%')
            p += 1

    workbook.close()
    return path

# download_report()