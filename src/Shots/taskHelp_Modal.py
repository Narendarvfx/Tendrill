import datetime
import json
import os
import time
from shutil import copyfile, copy2

from PySide2 import QtCore, QtGui, QtWebSockets
from PySide2.QtCore import QEasingCurve, QPoint, QAbstractAnimation, QCoreApplication, QUrl, QThreadPool, QTimer, \
    QPropertyAnimation
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QDialog, QGridLayout, QMessageBox, QTableWidgetItem, QGraphicsOpacityEffect

import api
import win32security
import ntsecuritycon as con

from uipy.projects.task_help_modal import Ui_TaskHelp_Dialog


class TaskHelp_Modal(QDialog):
    def __init__(self,instance, *args, **kwargs):
        super(TaskHelp_Modal, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_TaskHelp_Dialog()
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
        man_day_cnt = 0
        for artist_data in self.artist_data:
            man_day_cnt += artist_data['assigned_bids']

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
        self.ui.request_pb.clicked.connect(self.post_assign)
        self.ui.cancel_pb.clicked.connect(self.close_dialog)
        self.ui.request_pb.setDisabled(True)
        # self.threadpool = QThreadPool()
        # self.client = QtWebSockets.QWebSocket("", QtWebSockets.QWebSocketProtocol.Version13, None)
        # self.sockets_host = "{}{}/ws/emp/".format(api.config['SOCKETS']['host'],
        #                                           api.config['SOCKETS']['port'])

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
                self.ui.request_pb.setEnabled(True)
        else:
            self.ui.avl_md_lb.setText(str(self.avail_mds))

    ## Saves data using post method
    def post_assign(self):
        date = datetime.date(self.dateEdit.date().year(),self.dateEdit.date().month(),self.dateEdit.date().day())
        time = datetime.time(self.ui.eta_time.time().hour(),self.ui.eta_time.time().minute())
        cb_date = datetime.datetime.combine(date,time)
        print(self.ui.sel_type_cb.currentIndex())
        post_data = {
            'shot': self.shot['id'],
            'task_type': self.ui.sel_type_cb.currentIndex(),
            'requested_by': self.main_window.employee_details['id'],
            'status': "RTA",
            'bid_days': float(self.ui.shot_md_le.text()),
            # 'eta': cb_date.isoformat()
        }
        # self.send_notification()
        response = api.request_TaskHelp(post_data)
        # per = self.create_permission()
        # if per == True:
        #     response = api.assign_shot(post_data)
        #     if response.status_code == 201:
        #         if self.shot['status']['code'] == "RTA" or self.shot['status']['code'] == 'WTS':
        #             shot_status = {
        #                 'status': "RTW"
        #             }
        #             api.update_ShotStatus(str(self.shot['id']), shot_status)
        #         self.close()
        #         self.send_notification()
        #         self.insertRow(response.json())
        #         msg = QMessageBox()
        #         msg.setText(self.shot['name']+"\nSuccessfully Assigned to "+self.ui.sel_artists_cb.currentText())
        #         msg.setWindowTitle("Success")
        #         msg.setIcon(QMessageBox.Information)
        #         msg.setStyleSheet("background-color: rgb(33,193,100);color:'white'")
        #         msg.exec_()
        # else:
        #     msg = QMessageBox()
        #     msg.setText("Something Went Wrong \n Please try Again \n or Contact Pipeline Administrator")
        #     msg.setWindowTitle("Error")
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
        #     msg.exec_()

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

        ## Creates Permission for shot folders
    def create_permission(self):
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
        return result