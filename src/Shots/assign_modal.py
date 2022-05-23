import datetime
import json
import os

from PySide2 import QtCore, QtGui, QtWebSockets
from PySide2.QtCore import QEasingCurve, QPoint, QAbstractAnimation, QCoreApplication, QUrl, QThreadPool, QTimer, \
    QPropertyAnimation
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QDialog, QGridLayout, QMessageBox, QTableWidgetItem, QGraphicsOpacityEffect

import api
from src.Shots.Worker_Class import Worker
from src.impersonate import Impersonate
from uipy.projects.assign_modal import Ui_Assign_Dialog
import win32security
import ntsecuritycon as con


class Assign_Modal(QDialog):
    def __init__(self,instance, *args, **kwargs):
        super(Assign_Modal, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Assign_Dialog()
        self.ui.setupUi(self)
        self.main_window = instance.main_window
        host = self.main_window.geometry()
        point = host.center() - self.rect().center()
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animMove = QtCore.QPropertyAnimation(self, b"pos");
        self.animMove.setDuration(250);
        self.animMove.setStartValue(point - QPoint(0, 30));
        self.animMove.setEndValue(point);
        self.animMove.setEasingCurve(QEasingCurve.OutQuad);
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)
        self.animMove.start(QAbstractAnimation.DeleteWhenStopped)
        self.current_row = instance.main_window.ui.all_shots_tbWidget.currentRow()
        self.shot = instance.main_window.ui.all_shots_tbWidget.item(self.current_row, 1).data(1)
        self.artist_data = api.getArtlistByShotId(self.shot['id'])
        self.ui.shot_detail_lb.setText(self.shot['name'])
        self.dateEdit = self.ui.eta_date
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("dd-MM-yyyy")
        self.timeEdit = self.ui.eta_time
        self.timeEdit.setTime(QtCore.QTime(18, 45, 0, 0))
        self.all_artists = api.getAllArtists()
        self.artist_data = api.getArtlistByShotId(self.shot['id'])
        existing_artists = []
        man_day_cnt = 0
        filtered_artists = [x for x in self.all_artists if x['department'] == self.shot['task_type']]
        for artist_data in self.artist_data:
            man_day_cnt += artist_data['assigned_bids']
            existing_artists.append(artist_data['artist'])

        grade_level = api.getGrades()

        for level in grade_level:
            self.ui.sel_art_level_cb.addItem(level['name'], level['id'])

        self.ui.sel_art_level_cb.activated.connect(self.grade_level_filter)

        if self.main_window.employee_details['role'] == "TEAM LEAD":
            for artist in self.all_artists:
                try:
                    if artist['fullName'] not in existing_artists and artist['team_lead']['id'] == self.main_window.employee_details['id']:
                        self.ui.sel_artists_cb.addItem(artist['fullName'], artist['id'])
                except:
                    pass
        else:
            for artist in filtered_artists:
                if artist['fullName'] not in existing_artists:
                    self.ui.sel_artists_cb.addItem(artist['fullName'], artist['id'])

        self.ui.shot_md_le.setValidator( QtGui.QDoubleValidator(
                0.0, # bottom
                10.0, # top
                1, # decimals
                notation=QtGui.QDoubleValidator.StandardNotation
            ));
        self.ui.shot_md_le.textChanged.connect(self.md_val_Changed)
        self.diff_mds = self.shot['bid_days']-man_day_cnt
        self.avail_mds = round(self.diff_mds,1)
        self.ui.avl_md_lb.setText(str(self.avail_mds))
        self.ui.assign_pb.clicked.connect(self.post_assign)
        self.ui.cancel_pb.clicked.connect(self.close_dialog)
        self.ui.assign_pb.setDisabled(True)
        self.threadpool = QThreadPool()
        self.client = QtWebSockets.QWebSocket("", QtWebSockets.QWebSocketProtocol.Version13, None)
        self.sockets_host = "{}{}/ws/emp/".format(api.config['SOCKETS']['host'],
                                                  api.config['SOCKETS']['port'])


    def grade_level_filter(self, index):
        self.sel_level_id = self.ui.sel_art_level_cb.itemData(index)
        self.sel_level = self.ui.sel_art_level_cb.currentText()


    ## Shows an dialog when mandays are not with in available mandays
    def md_val_Changed(self, text):
        if self.ui.shot_md_le.text() :
            val = float(text)
            if val > float(self.avail_mds):
                msg = QMessageBox()
                msg.about(self, "Error", "Please enter with in the Available Man Days")
                self.ui.shot_md_le.setStyleSheet("border:2px solid red;border-radius:3px")
            else:
                self.ui.shot_md_le.setStyleSheet("border:2px solid green;border-radius:3px")
                avail_md = float(self.avail_mds)-float(text)
                self.ui.avl_md_lb.setText(str(round(avail_md,1)))
                self.ui.assign_pb.setEnabled(True)
        else:
            self.ui.avl_md_lb.setText(str(self.avail_mds))

    ## Saves data using post method
    def post_assign(self):
        date = datetime.date(self.dateEdit.date().year(),self.dateEdit.date().month(),self.dateEdit.date().day())
        time = datetime.time(self.ui.eta_time.time().hour(),self.ui.eta_time.time().minute())
        cb_date = datetime.datetime.combine(date,time)
        self.artist_data = api.getArtlistByShotId(self.shot['id'])
        compiler = 0;
        employee_details = api.get_employee_data(str(self.ui.sel_artists_cb.currentData()))
        if self.ui.sel_Compiler_chckBox.isChecked():
            for artist in self.artist_data:
                compiler = 1
                update_data = {
                    'compiler': compiler,
                }
                api.updateTask(str(artist['id']), update_data)
            compiler = 2
        else:
            for artist in self.artist_data:
                if artist['compiler'] == 2:
                    compiler = 1
        post_data = {
            'shot': self.shot['id'],
            'artist': self.ui.sel_artists_cb.currentData(),
            'assigned_by': self.main_window.employee_details['id'],
            'task_status': "YTS",
            'assigned_bids': float(self.ui.shot_md_le.text()),
            'compiler': compiler,
            'eta': cb_date.isoformat()
        }
        response = api.assign_shot(post_data)
        if response.status_code == 201:
            if self.shot['status']['code'] == "YTA" or self.shot['status']['code'] == 'ATL':
                shot_status = {
                    'status': "YTS",
                    'location': employee_details['location']
                }
                api.update_ShotStatus(str(self.shot['id']), shot_status)
            self.close()
            # self.send_notification()
            self.insertRow(response.json())
            msg = QMessageBox()
            msg.setText(self.shot['name']+"\nSuccessfully Assigned to "+self.ui.sel_artists_cb.currentText())
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("background-color: rgb(33,193,100);color:'white'")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText("Something Went Wrong \n Please try Again \n or Contact Pipeline Administrator")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def close_dialog(self):
        self.close()

    def send_notification(self):
        selected_art_id = self.ui.sel_artists_cb.currentData()
        employee_data = api.get_employee_data(selected_art_id)
        to_id = []
        to_id.append(employee_data['id'])
        to_id.append(employee_data['team_lead']['id'])
        to_id.append(employee_data['supervisor']['id'])
        self.clients = []
        for id in to_id:
            if str(id)  !=  str(self.main_window.employee_details['id']):
                notification_data = {
                    'message': self.shot['name']+" Assigned",
                    'by': self.main_window.employee_details['id'],
                    'to': id,
                }
                post_response = api.postNotification(notification_data)
                if post_response.status_code == 201:
                    client = QtWebSockets.QWebSocket("", QtWebSockets.QWebSocketProtocol.Version13, None)
                    self.sockets_host = "{}{}/ws/emp/".format(api.config['SOCKETS']['host'],
                                                              api.config['SOCKETS']['port'])
                    ws_Url = QUrl(self.sockets_host + str(id) + "/")
                    client.error.connect(self.error)
                    client.open(ws_Url)
                    self.clients.append(client)
        QTimer.singleShot(100, self.sendNotification)

    def error(self, error_code):
        print("error code: {}".format(error_code))
        print(self.client.errorString())

    def sendNotification(self):
        for client in self.clients:
            data = {
                'Name': self.main_window.employee_details['fullName'],
                'message': self.shot['name'] + " Assigned by " + self.main_window.employee_details['fullName'],
                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            client.sendTextMessage(json.dumps(data))
            client.close()

    def insertRow(self, response):
        row_count = self.main_window.ui.team_tableWid.rowCount()
        self.main_window.ui.team_tableWid.insertRow(row_count)
        tbWid = QTableWidgetItem()
        tbWid.setData(1, response)
        tbWid.setText(self.ui.sel_artists_cb.currentText())
        tbWid.setFont(QFont('Cambria', 12, QFont.Bold))
        self.main_window.ui.team_tableWid.setItem(row_count, 0, tbWid)
        status_item = QTableWidgetItem()
        status_item.setText(QCoreApplication.translate("MainWindow", "YTS", None))
        status_item.setForeground(QtGui.QColor('#B4B1AB'))
        status_item.setTextAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(12)
        font.setFamily('Arial')
        font.setBold(True)
        status_item.setFont(font)
        self.main_window.ui.team_tableWid.setItem(row_count, 1, status_item)
        self.main_window.ui.team_tableWid.setItem(row_count, 2, QTableWidgetItem(str(response['assigned_bids'])))
        self.main_window.ui.team_tableWid.setItem(row_count, 3, QTableWidgetItem(str(response['start_date'])))
        self.main_window.ui.team_tableWid.setItem(row_count, 4, QTableWidgetItem(str(response['end_date'])))

    ## Creates Permission for shot folders
    def create_permission(self):
        i = Impersonate('user_name', 'user_password')

        # Logging in
        i.logon()
        employee_details = api.get_employee_data(str(self.ui.sel_artists_cb.currentData()))
        artist_user_id = api.get_employee_user_name(str(employee_details['profile']))
        dep_dir = "_"+employee_details['department'].lower()
        shot_dir = os.path.join(self.shot['sequence']['project']['client'],self.shot['sequence']['project']['name'], self.shot['sequence']['name'],self.shot['name'])
        scripts_dir = os.path.join(api.config['STORAGE']['storage_url'], api.config['STORAGE']['parent_directory'], shot_dir, dep_dir,'scripts')
        others = ['cp', 'internal_denoise', 'output', 'pre_renders', 'qc', 'sv']
        result = False
        for other in others:
            other_dirs = os.path.join(api.config['STORAGE']['storage_url'], api.config['STORAGE']['parent_directory'],
                                      shot_dir,
                                      dep_dir, other, str(artist_user_id['username']))
            if not os.path.exists(other_dirs):
                os.makedirs(other_dirs)
            try:
                FILENAME = other_dirs

                artist, domain, type = win32security.LookupAccountName("", str(artist_user_id['username']))

                sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

                dacl = sd.GetSecurityDescriptorDacl()

                dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                           win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT, con.GENERIC_ALL,
                                           artist)

                sd.SetSecurityDescriptorDacl(1, dacl, 0)
                win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
                result = True
            except Exception as e:
                print("Permissions:", e)
                result = False

        for scripts in os.listdir(scripts_dir):
            final_dir = os.path.join(scripts_dir, scripts, str(artist_user_id['username']))
            if not os.path.exists(final_dir):
                os.makedirs(final_dir)
            try:
                FILENAME = final_dir

                artist, domain, type = win32security.LookupAccountName("", str(artist_user_id['username']))

                sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

                dacl = sd.GetSecurityDescriptorDacl()

                dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                           win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT, con.GENERIC_ALL,
                                           artist)

                sd.SetSecurityDescriptorDacl(1, dacl, 0)
                win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
                result = True
            except Exception as e:
                print("Permissions:", e)
                result = False

        # Internal Retake Permissions
        internal_qc_folder = os.path.join(api.config['STORAGE']['storage_url'], api.config['STORAGE']['parent_directory'],
                                          shot_dir,
                                          dep_dir, "qc","internal_retake")
        try:
            FILENAME = internal_qc_folder

            artist, domain, type = win32security.LookupAccountName("", str(artist_user_id['username']))

            sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

            dacl = sd.GetSecurityDescriptorDacl()

            dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                       win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT,
                                       con.GENERIC_ALL, artist)

            sd.SetSecurityDescriptorDacl(1, dacl, 0)
            win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
            result = True
        except Exception as e:
            print("Permissions:", e)
            result = False
        Impersonate.logoff(i)
        return result