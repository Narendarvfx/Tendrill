import csv
import datetime
import getpass
import os
from subprocess import call

import xlsxwriter
from PySide2 import QtCore, QtGui
from PySide2.QtCore import QEasingCurve, QAbstractAnimation, QCoreApplication, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QDialog, QFileDialog, QApplication, QTableWidgetItem, QHBoxLayout, QWidget, QLabel

import api
from uipy.client_status_change import Ui_Client_Status_Dialog
import pandas as pd


class ClientStatusDailog(QDialog):
    def __init__(self,instance, *args, **kwargs):
        super(ClientStatusDailog, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Client_Status_Dialog()
        self.ui.setupUi(self)
        self.instance = instance
        self.config = api.config
        host = instance.main_window
        hostRect = host.geometry();
        point = hostRect.center() - self.rect().center()
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animMove = QtCore.QPropertyAnimation(self, b"pos");
        self.animMove.setDuration(250);
        self.animMove.setStartValue(point - QtCore.QPoint(0, 30));
        self.animMove.setEndValue(point);
        self.animMove.setEasingCurve(QEasingCurve.OutQuad);
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)
        self.animMove.start(QAbstractAnimation.DeleteWhenStopped)
        try:
            self.ui.save_btn.clicked.disconnect()
            self.ui.cancel_btn.clicked.disconnect()
            self.ui.export_btn.clicked.disconnect()
            self.ui.import_btn.clicked.disconnect()
        except Exception as e:
            pass
        self.ui.save_btn.clicked.connect(lambda: self.change_status())
        self.ui.cancel_btn.clicked.connect(lambda: self.cancel_btn())
        self.ui.export_btn.clicked.connect(lambda: self.export_shots())
        self.ui.import_btn.clicked.connect(lambda: self.import_excel())

    def export_shots(self):
        # print(self.instance.selected_shots)
        data = []
        for shots in self.instance.rejected_shots:
            j_format = {
                'ID': shots['id'],
                'CLIENT': shots['sequence']['project']['client'],
                'PROJECT': shots['sequence']['project']['name'],
                'SEQUENCE': shots['sequence']['name'],
                'SHOT': shots['name'],
                'TASK TYPE': shots['task_type'],
                'STATUS': shots['status']['code'],
                'ANNOTATIONS PATH': ''
            }
            data.append(j_format)
        data_frame = pd.json_normalize(data)
        now =datetime.datetime.now()
        path = r'C:\Users\{}\Downloads'.format(getpass.getuser())
        file_name = 'Client_Retake({}).csv'.format(now.strftime("%d-%m-%Y %H%M"))
        data_frame.to_csv(os.path.join(path,file_name), index = False, header=True)

    def import_excel(self):
        self.dlg = QFileDialog().getOpenFileName(None, 'Open File', '', 'CSV files(*.csv)')
        ## To get total count of rows for avg
        self.file = open(self.dlg[0])
        self.file_name = os.path.basename(self.dlg[0])
        self.ui.sel_file_lbl.setText(self.file_name)

    def change_status(self):
        self.accept()
        with open(self.dlg[0], newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                QApplication.processEvents()
                task_type = '_'+row['TASK TYPE']
                annot_path = os.path.join(self.config['STORAGE']['storage_url'],
                                                       self.config['STORAGE']['parent_directory'],row['CLIENT'],row['PROJECT'],row['SEQUENCE'],row['SHOT'],'_feedback',task_type)
                final_path = ''
                if len(os.listdir(annot_path)) == 0:
                    os.makedirs(annot_path+"\\"+'V001')
                    final_path = os.path.join(annot_path, max(os.listdir(annot_path)))
                else:
                    version = int(max(os.listdir(annot_path)).split("V")[1])
                    version += 1
                    os.makedirs(annot_path+"\\"+'V%03d' % (version))
                    final_path = os.path.join(annot_path, max(os.listdir(annot_path)))
                if row['STATUS'] == "DTC":
                    data = {
                        'status': 'CRT'
                    }
                    res = api.update_ShotStatus(str(row['ID']), data)
                    for index in self.instance.index_shots:
                        if str(index['shot']) == str(row['ID']):
                            stWidget = QWidget();
                            st_label = QLabel();
                            st_label.setText(res.json()['status']['code'])
                            font = QFont()
                            font.setPointSize(10)
                            font.setFamily('Arial')
                            font.setBold(True)
                            st_label.setFont(font)
                            st_label.setAlignment(Qt.AlignCenter)
                            stLayout = QHBoxLayout(stWidget);
                            stLayout.addWidget(st_label);
                            stLayout.setAlignment(Qt.AlignCenter);
                            stLayout.setContentsMargins(0, 0, 0, 0);
                            stWidget.setLayout(stLayout);
                            stWidget.setStyleSheet(
                                'QWidget{margin-top:5px;margin-bottom:5px;color:white;background-color:'+res.json()['status']['color']+'}')
                            stWidget.setToolTip(res.json()['status']['name'])
                            self.instance.main_window.ui.all_shots_tbWidget.setCellWidget(index['index'], 9, stWidget)
                    call(['robocopy', row['ANNOTATIONS PATH'], final_path, "/S"])

    def cancel_btn(self):
        self.reject()