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
from uipy.projects.assign_modal import Ui_Assign_Dialog
import win32security
import ntsecuritycon as con

from uipy.projects.edit_shot_modal import Ui_Shots_Edit_Dialog


class Shots_Edit_Modal(QDialog):
    def __init__(self,instance, *args, **kwargs):
        super(Shots_Edit_Modal, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Shots_Edit_Dialog()
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
        self.ui.shot_label.setText(self.shot['name'])
        self.ui.bid_days_le.setValidator(QtGui.QDoubleValidator(
            0.0,  # bottom
            10.0,  # top
            1,  # decimals
            notation=QtGui.QDoubleValidator.StandardNotation
        ));
        self.ui.frame_in_le.setValidator(QtGui.QDoubleValidator(
            0.0,  # bottom
            10000.0,  # top
            0,  # decimals
            notation=QtGui.QDoubleValidator.StandardNotation
        ));
        self.ui.frame_out_le.setValidator(QtGui.QDoubleValidator(
            0.0,  # bottom
            10000.0,  # top
            0,  # decimals
            notation=QtGui.QDoubleValidator.StandardNotation
        ));
        if self.shot['type'] == "NEW":
            self.ui.tyep_cb.setItemText(0, self.shot['type'])
        elif self.shot['type'] == "RETAKE":
            self.ui.tyep_cb.setItemText(1, self.shot['type'])
        elif self.shot['type'] == "ADDITIONAL":
            self.ui.tyep_cb.setItemText(2, self.shot['type'])
        self.ui.bid_days_le.setText(str(self.shot['bid_days']))
        self.ui.frame_in_le.setText(str(self.shot['actual_start_frame']))
        self.ui.frame_out_le.setText(str(self.shot['actual_end_frame']))
        self.etaEdit = self.ui.eta_edit
        self.etaEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.etaEdit.setCalendarPopup(True)
        self.etaEdit.setDisplayFormat("dd-MM-yyyy")
        self.ui.update_btn.clicked.connect(self.update_shot)
        self.ui.cancel_btn.clicked.connect(self.close_dialog)
        self.threadpool = QThreadPool()
        self.client = QtWebSockets.QWebSocket("", QtWebSockets.QWebSocketProtocol.Version13, None)
        self.sockets_host = "{}{}/ws/emp/".format(api.config['SOCKETS']['host'],
                                                  api.config['SOCKETS']['port'])

    ## Saves data using post method
    def update_shot(self):
        type = self.ui.tyep_cb.currentText()
        bid_days = self.ui.bid_days_le.text()
        frame_in = self.ui.frame_in_le.text()
        frame_out = self.ui.frame_out_le.text()
        eta_date = self.ui.eta_edit.date()
        print(eta_date.toPython())
        if bid_days == "":
            bid_days = self.shot['bid_days']
        if frame_in == "":
            frame_in = self.shot['actual_start_frame']
        if frame_out == "":
            frame_out = self.shot['actual_end_frame']
        post_data = {
            'shot': self.shot['id'],
            'type': type,
            'bid_days': bid_days,
            'actual_start_frame': frame_in,
            'actual_end_frame': frame_out,
            'eta': eta_date.toPython()
        }
        response = api.update_ShotStatus(str(self.shot['id']), post_data)
        self.close()
        if response.status_code == 201:
            msg = QMessageBox()
            msg.setText(self.shot['name']+"\nUpdated Successfully")
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("background-color: rgb(33,193,100);color:'white'")
            msg.exec_()
            self.save_history(type,bid_days,frame_in, frame_out)
        else:
            msg = QMessageBox()
            msg.setText("Something Went Wrong \n Please try Again \n or Contact Pipeline Administrator")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def close_dialog(self):
        self.close()

    def save_history(self, type, bid_days, frame_in, frame_out):
        if type != self.shot['type']:
            type_data = {
                "shot" : self.shot['id'],
                "message": "Type Changed From "+self.shot['type']+" to "+type,
                "updated_by": self.main_window.employee_details['id']
            }
            api.postShotLogs(type_data)
        if str(bid_days) != str(self.shot['bid_days']):
            bid_data = {
                "shot": self.shot['id'],
                "message": "Bid days Changed From " + str(self.shot['bid_days']) + " to " + str(bid_days),
                "updated_by": self.main_window.employee_details['id']
            }
            api.postShotLogs(bid_data)
        if str(frame_in) != str(self.shot['actual_start_frame']) or str(frame_out) != str(self.shot['actual_end_frame']):
            frame_data = {
                "shot": self.shot['id'],
                "message": "Frames Changed From " + str(self.shot['actual_start_frame'])+"-" +str(self.shot['actual_end_frame'])+ " to " + str(frame_in)+'_'+str(frame_out),
                "updated_by": self.main_window.employee_details['id']
            }
            api.postShotLogs(frame_data)

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