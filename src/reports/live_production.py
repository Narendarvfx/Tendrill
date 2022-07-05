import datetime
import getpass
import os

import requests
import xlsxwriter
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox

import api

base_url = api.base_url
token = api.token
session = requests.Session()
headers = {'Authorization': 'token {}'.format(token)}

def get_data(dept):
    status_list = "RTA|WTS|RTW|IP|STC|REW|IRT|IAP|CRT|LAP|LRT"
    allShotsData = api.allShotsData(status_list, dept=dept)

    return allShotsData

def create_workbook():
    # Create a workbook and add a worksheet.
    user = getpass.getuser()
    file_path = r"C:\Users\{}\Documents\ofx_reports".format(user)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    path = file_path+'\live_production_report.xlsx'
    workbook = xlsxwriter.Workbook(path)
    for dept in ['PAINT','ROTO', 'MM','COMP']:
        shots_data = get_data(dept)
        worksheet = workbook.add_worksheet(dept)
        write_to_excel(workbook, worksheet, shots_data)

    workbook.close()
    download_success_dialog(path)

def download_success_dialog(path):
    msg = QMessageBox()
    msg.setText("Report Downloaded Successfully in following path\n\n "+path+"\n\n\n Tip: select and copy the path and open in file browser")
    msg.setWindowTitle("Success")
    msg.setIcon(QMessageBox.Information)
    # msg.setStyleSheet("background-color: rgb(33,193,100);color:'white'")
    msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
    msg.exec_()

def write_to_excel(workbook, worksheet, shots_data):
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True, 'bg_color': '#43d3f7', 'border': 1, 'border_color': 'black'})
    pending_color = workbook.add_format({'bg_color': 'yellow', 'border': 1, 'border_color': 'black'})
    border = workbook.add_format({'border': 1, 'border_color': 'black'})
    # Add a number format for cells with percentage.
    percent = workbook.add_format({'num_format': '0.0%', 'border': 1, 'border_color': 'black'})

    # Write some data headers.
    worksheet.write('A1', 'CLIENT', bold)
    worksheet.write('B1', 'PROJECT', bold)
    worksheet.write('C1', 'SHOT CODE', bold)
    worksheet.write('D1', 'TOTAL FRAMES', bold)
    worksheet.write('E1', 'TASK', bold)
    worksheet.write('F1', 'STATUS', bold)
    worksheet.write('G1', 'BID DAYS', bold)
    worksheet.write('H1', 'IP%', bold)
    worksheet.write('I1', 'DUE MANDAYS', bold)
    worksheet.write('J1', 'DUE DATE', bold)
    worksheet.write('K1', 'NOTES', bold)
    worksheet.write('L1', 'TEAM', bold)
    worksheet.write('M1', 'ARTIST NAME', bold)
    worksheet.write('N1', 'IN DATE', bold)
    worksheet.write('O1', 'PACKAGE ID', bold)
    worksheet.write('P1', 'ESTIMATE ID', bold)
    worksheet.write('Q1', 'ESTIMATE DATE', bold)

    # # Start from the first cell below the headers.
    col = 0
    row = 0
    for shot_data in shots_data:
        shot_status = shot_data['status']['code']
        if shot_data['status']['code'] in ['RTA', 'WTS', 'RTW']:
            shot_status = "RTW"
        elif shot_data['status']['code'] in ['IP', 'STC', 'LRT']:
            shot_status = "IP"
        elif shot_data['status']['code'] in ['REW', 'IRT', 'LAP']:
            shot_status = "QC"
        elif shot_data['status']['code'] == "IAP":
            shot_status = "IAP"
        elif shot_data['status']['code'] == "CRT":
            shot_status = "RETAKE"

        if shot_data['type'] == "RETAKE":
            bid_days = 0
            percentile = 0
        else:
            bid_days = float(shot_data['bid_days'])
            percentile = shot_data['progress'] / 100
        bid_column = 'G{}'.format(row + 2)
        progress_column = 'H{}'.format(row + 2)
        total_frames = shot_data['actual_end_frame'] - shot_data['actual_start_frame'] + 1
        due_date = ""
        if shot_data['eta']:
            due_date = datetime.datetime.strptime(shot_data['eta'], '%Y-%m-%dT%H:%M:%S').strftime(
                "%d-%m-%Y")
        worksheet.write(row + 1, col, shot_data['sequence']['project']['client']['name'], border)
        worksheet.write(row + 1, col + 1, shot_data['sequence']['project']['name'], border)
        worksheet.write(row + 1, col + 2, shot_data['name'], border)
        worksheet.write(row + 1, col + 3, str(total_frames), border)
        worksheet.write(row + 1, col + 4, shot_data['task_type'], border)
        worksheet.write(row + 1, col + 5, shot_status, border)
        worksheet.write(row + 1, col + 6, bid_days, border)
        worksheet.write(row + 1, col + 7, percentile, percent)
        worksheet.write(row + 1, col + 8,
                        '=ROUND(({}-{}*{}),1)'.format(bid_column, bid_column, progress_column), pending_color)
        worksheet.write(row + 1, col + 9, due_date, border)
        worksheet.write(row + 1, col + 10, " ", border)
        worksheet.write(row + 1, col + 11, shot_data['team_lead'], border)
        worksheet.write(row + 1, col + 12, shot_data['artist'], border)
        in_date = datetime.datetime.strptime(shot_data['creation_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime(
            "%d-%m-%Y")
        worksheet.write(row + 1, col + 13, in_date, border)
        worksheet.write(row + 1, col + 14, shot_data['package_id'], border)
        worksheet.write(row + 1, col + 15, shot_data['estimate_id'], border)
        if shot_data['estimate_date']:
            estimate_date = datetime.datetime.strptime(shot_data['estimate_date'], '%Y-%m-%dT%H:%M:%S').strftime(
                "%d-%m-%Y")
        else:
            estimate_date = ""
        worksheet.write(row + 1, col + 16, estimate_date, border)
        row += 1
# write_to_excel()