import configparser
import datetime
import getpass
import json
import os
import subprocess
import sys
import webbrowser
from pprint import pprint
from PySide2 import QtWidgets, QtGui, QtCore, QtWebSockets
from PySide2.QtCore import QUrl, QSize, QRect, QTimer, QEasingCurve, QAbstractAnimation, QThreadPool
from PySide2.QtGui import QColor, QFont, Qt
from PySide2.QtWidgets import QTreeWidgetItem, QApplication, QTreeWidget, QGraphicsDropShadowEffect, QMessageBox, \
    QFrame, QGridLayout, QLabel, QWidget, QVBoxLayout, QDialog

import api
from src.Shots.Worker_Class import Worker
from src.Shots.client_version import CVersions
from src.Shots.lead_versions import LVersions
from src.Shots.output_path_modal import OutputPathModal
from src.Shots.paths_page import PathPage
from src.Shots.per_calculator import get_previous_logs
from src.Shots.taskHelp_Modal import TaskHelp_Modal
from uipy.add_percentage_modal import Ui_Percentage_Dialog
from src.Notifications.system_tray import SystemTrayIcon
from src.Shots.assign_modal import Assign_Modal
from src.Shots.output_folder import Output_Folder
from src.Shots.pre_renders_folder import PreRenders_Folder
from src.Shots.qc_folder import Qc_Folder
from src.Shots.scripts_folder import Scripts_Folder
from src.Shots.annotations_folder import Annotations_Folder
from src.Shots.team_page import Team_Page
from src.Shots.versions import Versions
from src.Versions.Versions_Page import Versions_Page
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class perDailog(QDialog):
    def __init__(self,instance, type , *args, **kwargs):
        super(perDailog, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Percentage_Dialog()
        self.ui.setupUi(self)
        newText = """Add <strong style="color:rgb(232, 147, 10)">{SHOT}</strong> Percentage"""
        newText = newText.replace('{SHOT}', type)
        self.ui.per_name_label.setText(newText)
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
        self.ui.per_save_btn.clicked.connect(lambda: self.save_percentage())
        self.ui.per_cancel_btn.clicked.connect(lambda: self.cancel_btn())

    def save_percentage(self):
        self.accept()

    def cancel_btn(self):
        self.reject()

    def getPercentage(self):
        return self.ui.per_spin_box.value()

class Shot_Details(QTreeWidget):
    def __init__(self, obj, type=None):
        super(Shot_Details, self).__init__()
        self.main_window = obj.main_window
        try:
            self.main_window.ui.send_btn.clicked.disconnect()
            self.main_window.ui.dep_tabWidget.currentChanged.disconnect()
            self.main_window.ui.shot_details_tabWidget.currentChanged.disconnect()
            self.main_window.ui.assign_btn.clicked.disconnect()
            self.main_window.ui.start_btn.clicked.disconnect()
            self.main_window.ui.qc_btn.clicked.disconnect()
            self.main_window.ui.comp_btn.clicked.disconnect()
            self.main_window.ui.retake_btn.clicked.disconnect()
            self.main_window.ui.nuke_btn.clicked.disconnect()
            self.main_window.ui.nukeX_btn.clicked.disconnect()
            self.main_window.ui.sfx_btn.clicked.disconnect()
            self.main_window.ui.psd_btn.clicked.disconnect()
            self.main_window.ui.mocha_btn.clicked.disconnect()
            self.main_window.ui.approved_btn.clicked.disconnect()
            self.main_window.ui.hold_btn.clicked.disconnect()
            self.main_window.ui.taskHelp_btn.clicked.disconnect()
            self.main_window.ui.client_retake_btn.clicked.disconnect()
            # self.main_window.ui.add_taskPer_btn.clicked.disconnect()
            # self.main_window.ui.add_per_btn.clicked.disconnect()

            ### Folders Disconnect
            self.main_window.ui.input_TreeWid.itemClicked.disconnect()
            self.main_window.ui.Pscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Rscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Mscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Ppre_ren_treeWid.itemClicked.disconnect()
            self.main_window.ui.Rpre_ren_treeWid.itemClicked.disconnect()
            self.main_window.ui.Mpre_ren_treeWid.itemClicked.disconnect()
            self.main_window.ui.Poutput_treeWid.itemClicked.disconnect()
            self.main_window.ui.Routput_treeWid.itemClicked.disconnect()
            self.main_window.ui.Moutput_treeWid.itemClicked.disconnect()
            self.main_window.ui.Pqc_treeWid.itemClicked.disconnect()
            self.main_window.ui.Rqc_treeWid.itemClicked.disconnect()
            self.main_window.ui.Mqc_treeWid.itemClicked.disconnect()
        except:
            pass

        self.task_details = []
        self.shot_details = []
        self.task_counter = ""
        # creating a timer object
        timer = QTimer(self)
        self.start = False
        status_code = None
        status_color = None
        eta = None
        bid_days = 0
        consumed_bids = None
        start_date = None
        end_date = None
        self.threadpool = QThreadPool()
        # self.main_window.ui.start_btn.hide()
        # self.main_window.ui.qc_btn.hide()
        # self.main_window.ui.comp_btn.hide()
        # self.main_window.ui.approved_btn.hide()
        # self.main_window.ui.retake_btn.hide()
        # self.main_window.ui.hold_btn.hide()
        # self.main_window.ui.client_retake_btn.hide()
        # self.main_window.ui.taskHelp_btn.hide()
        # self.main_window.ui.nuke_btn.hide()
        # self.main_window.ui.nukeX_btn.hide()
        if type == 'task':
            self.task_details = obj.task_details
            self.shot_details = obj.task_details['shot']
            # self.task_progressBarValue(self.task_details['art_percentage'])
            # self.task_counter = self.task_details['art_percentage']
            status_code = obj.task_details['task_status']['code']
            status_color = obj.task_details['task_status']['color']
            bid_days = obj.task_details['assigned_bids']
            if obj.task_details['eta']:
                eta = datetime.datetime.strptime(obj.task_details['eta'], '%Y-%m-%dT%H:%M:%S').strftime(
                    "%d-%m-%Y %H:%M")

        else:
            self.shot_details = obj.shot_details
            print(self.shot_details)
            status_code = obj.shot_details['status']['code']
            status_color = obj.shot_details['status']['color']
            bid_days = obj.shot_details['bid_days']
            if obj.shot_details['eta']:
                eta = datetime.datetime.strptime(obj.shot_details['eta'], '%Y-%m-%dT%H:%M:%S').strftime(
                    "%d-%m-%Y %H:%M")

        self.config = api.config
        self.main_window.ui.shot_details_tabWidget.setCurrentIndex(0)
        self.main_window.ui.shotName_lbl.setText(self.shot_details['name'])
        self.main_window.ui.clientName_lbl.setText(self.shot_details['sequence']['project']['client']['name'])
        self.main_window.ui.projectName_lbl.setText(self.shot_details['sequence']['project']['name'])
        self.main_window.ui.seqName_lbl.setText(self.shot_details['sequence']['name'])
        self.main_window.ui.frameIn_lbl.setText(str(self.shot_details['actual_start_frame']))
        self.main_window.ui.frameOut_lbl.setText(str(self.shot_details['actual_end_frame']))
        self.main_window.ui.totalFrames_lbl.setText(
            str(self.shot_details['actual_end_frame'] - self.shot_details['actual_start_frame'] + 1))
        self.main_window.ui.status_btn.setText(status_code)
        self.main_window.ui.status_btn.setStyleSheet(
            'color:"#3b3839";background-color:{};padding-left:15px;padding-right:15px;padding-top:5px;padding-bottom:5px'.format(
                status_color))
        self.main_window.ui.eta_lbl.setText(str(eta))
        self.main_window.ui.totalBids_lbl.setText(str(bid_days))
        self.main_window.ui.input_TreeWid.clear()
        self.add_InputsTree_widget()
        Annotations_Folder.addTask_Annotation_widget(self)
        Annotations_Folder.addFeedback_Annotation_widget(self)
        self.main_window.ui.dep_tabWidget.currentChanged.connect(lambda: self.tabChanged())
        self.main_window.ui.shot_details_tabWidget.currentChanged.connect(lambda: self.shotDetailsTabClicked())
        if self.shot_details['task_type'] == 'PAINT':
            self.main_window.ui.dep_tabWidget.setCurrentIndex(0)
            timer.timeout.connect(Scripts_Folder.addPScriptsTree_widget(self))
            # timer.timeout.connect(PreRenders_Folder.Ppre_renders_folder(self))
            # timer.timeout.connect(Output_Folder.Poutput_folder(self))
            # timer.timeout.connect(Qc_Folder.Pqc_Folder(self))
        elif self.shot_details['task_type'] == 'ROTO':
            self.main_window.ui.dep_tabWidget.setCurrentIndex(1)
            # Scripts_Folder.addRScriptsTree_widget(self)
            # PreRenders_Folder.Rpre_renders_folder(self)
            # Output_Folder.Routput_folder(self)
            # Qc_Folder.Rqc_Folder(self)
        elif self.shot_details['task_type'] == 'MM':
            self.main_window.ui.dep_tabWidget.setCurrentIndex(2)
            # PreRenders_Folder.Mpre_renders_folder(self)
            # Output_Folder.Moutput_folder(self)
            # Qc_Folder.Mqc_Folder(self)

        # self.client.open(QUrl(sockets_host + str(self.shot_details['id']) + "/"))
        # self.client.textMessageReceived.connect(self.processTextMessage)
        # self.assign_btn = self.main_window.ui.assign_btn.clicked.connect(lambda: self.assignModal())
        # self.main_window.ui.start_btn.clicked.connect(lambda: self.task_status_update("WIP"))
        # self.main_window.ui.comp_btn.clicked.connect(lambda: self.task_status_update("STC"))
        # self.main_window.ui.qc_btn.clicked.connect(lambda: self.task_status_update("STQ"))
        approve_status = ""
        retake_status = ""
        client_retake_status = ""
        hold_status = ""
        if self.main_window.employee_details['role'] == "TEAM LEAD" or self.main_window.employee_details['role'] == "SUPERVISOR":
            # approve_status = "QIP"
            approve_status = "LAP"
            retake_status = "LRT"
        elif self.main_window.employee_details['role'] == "QC" or self.main_window.employee_details[
            'role'] == "PRODUCTION MANAGER":
            approve_status = "IAP"
            retake_status = "IRT"
            client_retake_status = "CRT"
            hold_status = "HLD"
        # self.main_window.ui.approved_btn.clicked.connect(lambda: self.shot_status_update(approve_status))
        # self.main_window.ui.retake_btn.clicked.connect(lambda: self.shot_status_update(retake_status))
        # self.main_window.ui.client_retake_btn.clicked.connect(lambda: self.shot_status_update(client_retake_status))
        # self.main_window.ui.hold_btn.clicked.connect(lambda: self.shot_status_update(hold_status))
        #
        # self.main_window.ui.send_btn.clicked.connect(lambda: self.message_function())

        bar = self.main_window.ui.scrollArea.verticalScrollBar()
        bar.rangeChanged.connect(lambda x, y: bar.setValue(y))

        # adding action to timer
        timer.timeout.connect(self.fetchShot_Messages())

        # update the timer every tenth second
        # timer.start(100)
        # # creating a timer object
        # self.timer = QTimer(self)
        # # adding action to timer
        # self.timer.timeout.connect(self.showTime)
        ## ==> APPLY DROP SHADOW EFFECT

    def progressBarValue(self, value):
        # count = self.counter
        pink = "rgb(255, 44, 174)"
        light_green = "rgb(115, 255, 171)"
        orange = "rgb(231, 128, 30)"
        red = "rgb(255, 60, 11)"
        green ="rgb(0, 170, 0)"

        if value < 25:
            color = red
        elif value >=25 and value < 50:
            color = pink
        elif value >=50 and value <75:
            color = orange
        elif value >=75 and value < 95:
            color = light_green
        elif value  >=95 and value <= 100:
            color = green

        label_color = """QLabel{color: {COLOR}; padding: 0px; background-color: none;}"""
        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(int(value)))
        newColor = label_color.replace("{COLOR}", color)
        # APPLY NEW PERCENTAGE TEXT
        self.main_window.ui.shotPercentage.setText(newHtml)
        self.main_window.ui.shotPercentage.setStyleSheet(newColor)
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
	border-radius: 110px;	
	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0) , stop:{STOP_2} {COLOR});
}
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        self.main_window.ui.shotProgress.setStyleSheet(newStylesheet)
        # if count >= self.value:
        #     self.timer.stop()
        # self.counter += 1

    def task_progressBarValue(self, value):
        # count = self.counter
        pink = "rgb(255, 44, 174)"
        light_green = "rgb(115, 255, 171)"
        orange = "rgb(231, 128, 30)"
        red = "rgb(255, 60, 11)"
        green = "rgb(0, 170, 0)"

        if value < 25:
            color = red
        elif value >= 25 and value < 50:
            color = pink
        elif value >= 50 and value < 75:
            color = orange
        elif value >= 75 and value < 95:
            color = light_green
        elif value >= 95 and value <= 100:
            color = green

        label_color = """QLabel{color: {COLOR}; padding: 0px; background-color: none;}"""
        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(int(value)))
        newColor = label_color.replace("{COLOR}", color)
        # APPLY NEW PERCENTAGE TEXT
        # self.main_window.ui.taskPercentage.setText(newHtml)
        # self.main_window.ui.taskPercentage.setStyleSheet(newColor)
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
    border-radius: 110px;	
    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0) , stop:{STOP_2} {COLOR});
}
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        # self.main_window.ui.taskProgress.setStyleSheet(newStylesheet)
        # if count >= self.value:
        #     self.timer.stop()
        # self.counter += 1

    def launch_nuke(self):
        config = configparser.ConfigParser()

        config['DEFAULT']['client'] = self.shot_details['sequence']['project']['client']['name']
        config['DEFAULT']['show'] = self.shot_details['sequence']['project']['name']
        config['DEFAULT']['seq'] = self.shot_details['sequence']['name']
        config['DEFAULT']['shot'] = self.shot_details['name']
        config['DEFAULT']['dep'] = self.shot_details['task_type']
        nk_dir = 'C:\\Users\\' + getpass.getuser() + '\\.nuke'
        if not os.path.exists(nk_dir):
            os.makedirs(nk_dir)
        with open(nk_dir + '\\config.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()
        # TODO: Open Nuke with read node containing the shot name
        try:
            # os.environ['PYTHONHOME'] = r"\\172.168.1.250\ofxbox\Nuke11.3v4"
            # sys.path.append(r'B:\Nuke11.3v4')
            newEnv = os.environ.copy()
            # newEnv["PYTHONPATH"] = newEnv["PATH"] + r"D:\Native Design\Shot-Buzz\venv"
            print(newEnv)
            # subprocess.Popen(['B:\\Nuke11.3v4\\Nuke11.3.exe'], env=newEnv)
        except Exception as e:
            print("EXCEPTION ::",e)
            pass

    def launch_nukeX(self):
        config = configparser.ConfigParser()

        config['DEFAULT']['client'] = self.shot_details['sequence']['project']['client']['name']
        config['DEFAULT']['show'] = self.shot_details['sequence']['project']['name']
        config['DEFAULT']['seq'] = self.shot_details['sequence']['name']
        config['DEFAULT']['shot'] = self.shot_details['name']
        config['DEFAULT']['dep'] = self.shot_details['task_type']
        nk_dir = 'C:\\Users\\' + getpass.getuser() + '\\.nuke'
        if not os.path.exists(nk_dir):
            os.makedirs(nk_dir)
        with open(nk_dir, 'w') as configfile:
            config.write(configfile)
            configfile.close()
        # TODO: Open Nuke with read node containing the shot name
        try:
            subprocess.Popen('\\\\172.168.1.250\\ofxbox\\Nuke11.3v4\\Nuke11.3.exe --nukex')
        except Exception as e:
            print(e)
            pass

    def launch_mocha(self):
        try:
            subprocess.Popen('\\\\172.168.1.250\\ofxbox\\mocha Pro V4\\bin\\mochapro.exe')
        except Exception as e:
            print(e)
            pass

    def launch_sfx(self):
        try:
            if self.shot_details['task_type'] == "ROTO":
                subprocess.Popen('\\\\172.168.1.250\ofxbox\\Silhouette 2020\\Silhouette.exe')
            else:
                msg = QMessageBox()
                msg.setText("Not Authorized to use the Selected Software \n Please contact IT Team \n ")
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Critical)
                msg.setStyleSheet("background-color: rgb(202,0,3,);color:'white'")
                msg.exec_()
        except Exception as e:
            print(e)
            pass

    def launch_psd(self):
        msg = QMessageBox()
        msg.setText("No Software Found in this Work Station \n Please contact IT Team \n ")
        msg.setWindowTitle("Error")
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("background-color: rgb(202,0,3,);color:'white'")
        msg.exec_()

    def add_InputsTree_widget(self):
        header = self.main_window.ui.input_TreeWid.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(False)
        # header.hide()

        scan_folder = 'scans'

        self.base_Path = r"{}\{}\{}\{}".format(self.config['STORAGE']['storage_url'],
                                                       self.shot_details['sequence']['project']['name'],
                                                       self.shot_details['sequence']['name'],
                                                       self.shot_details['name'])

        self.main_window.ui.input_TreeWid.clear()
        # self.main_window.ui.input_TreeWid.columnCount(5)
        self.main_window.ui.input_TreeWid.setHeaderLabel("folder")
        input_folders = os.path.join(self.base_Path, scan_folder)# C:\jfx\client_01\KIS\BOO_GKB\BOO_GKB_0080_fg01_v002\scans
        if os.path.exists(input_folders):
            for folder_name in os.listdir(input_folders): #[denoise, plates]
                item_0 = QTreeWidgetItem([folder_name.upper()])
                self.main_window.ui.input_TreeWid.addTopLevelItem(item_0)
                item_0.setData(0,Qt.UserRole,os.path.join(input_folders, folder_name))
                item_0.setTextColor(0, Qt.darkYellow)
                item_0.setFont(0, QFont('Arial', 10, QFont.Bold))
                sub_folders = os.listdir(os.path.join(input_folders,folder_name))

                for sub_folder in sub_folders:
                    sub_folder_path = os.path.join(input_folders,folder_name, sub_folder)
                    if os.path.isdir(sub_folder_path):
                        sub = QTreeWidgetItem(item_0, [sub_folder])
                        # sub.setForeground(Qt.red)
                        sub.setTextColor(0,Qt.darkGreen)
                        sub.setData(0,Qt.UserRole,sub_folder_path)



        self.main_window.ui.input_TreeWid.expandToDepth(0)
        self.main_window.ui.input_TreeWid.itemClicked.connect(lambda: self.inputItemClicked())

    def inputItemClicked(self):
        it = self.main_window.ui.input_TreeWid.currentItem()
        os.startfile(it.data(0, Qt.UserRole))

    def tabChanged(self):
        currentIndex = self.main_window.ui.dep_tabWidget.currentIndex()
        if currentIndex == 0:
            self.main_window.ui.Pscripts_treeWid.clear()
            Scripts_Folder.addPScriptsTree_widget(self)
            # PreRenders_Folder.Ppre_renders_folder(self)
            # Output_Folder.Poutput_folder(self)
            # Qc_Folder.Pqc_Folder(self)
        elif currentIndex == 1:
            self.main_window.ui.Rscripts_treeWid.clear()
            # Scripts_Folder.addRScriptsTree_widget(self)
            # PreRenders_Folder.Rpre_renders_folder(self)
            # Output_Folder.Routput_folder(self)
            # Qc_Folder.Rqc_Folder(self)
        elif currentIndex == 2:
            self.main_window.ui.Mscripts_treeWid.clear()
            # Scripts_Folder.addMScriptsTree_widget(self)
            # PreRenders_Folder.Mpre_renders_folder(self)
            # Output_Folder.Moutput_folder(self)
            # Qc_Folder.Mqc_Folder(self)

    def shotDetailsTabClicked(self):
        index = self.main_window.ui.shot_details_tabWidget.currentIndex()
        if index == 0:
            pass
        elif index == 1:
            Versions_Page.int_ver_table(self)
            Versions_Page.qc_ver_table(self)
            pass
        elif index == 2:
            Team_Page(self)
        elif index == 3:
            PathPage(self)

    def assignModal(self):
        modal = Assign_Modal(self)
        if modal.exec_():
            pass
        else:
            pass

    def taskHelpModal(self):
        modal = TaskHelp_Modal(self)
        if modal.exec_():
            pass
        else:
            pass

    def task_status_update(self, status):
        # if self.start:
        #     self.start = False;
        #     self.timer.stop()
        # else:
        #     self.start = True
        #     # update the timer every tenth second
        #     self.timer.start(1000)
        data = {
            'task_status': status
        }
        qm = QMessageBox()
        result = qm.question(self, 'Shot Buzz Application', "Are you sure with {}".format(status), qm.Yes | qm.No)
        if result == qm.Yes:
            response = api.updateTask(str(self.task_details['id']), data)
            if response.status_code == 201:
                shot_data = {
                    'status': status
                }
                if status != "STC":
                    api.update_ShotStatus(str(self.shot_details['id']), shot_data)
                if status == "WIP":
                    self.main_window.ui.start_btn.hide()
                    if self.task_details['compiler'] == 2 or self.task_details['compiler'] == 0:
                        self.main_window.ui.qc_btn.show()
                    else:
                        self.main_window.ui.comp_btn.show()
                elif status == "STQ":
                    self.main_window.ui.qc_btn.hide()
                    Versions.create_version(self)
                elif status == "STC":
                    self.main_window.ui.comp_btn.hide()
                self.main_window.ui.status_btn.setText(response.json()['task_status']['code'])
                self.main_window.ui.status_btn.setStyleSheet(
                    'color:"#3b3839";background-color:{};padding-left:15px;padding-right:15px;padding-top:5px;padding-bottom:5px'.format(
                        response.json()['task_status']['color']))
                self.shadow = QGraphicsDropShadowEffect()
                self.shadow.setBlurRadius(50)
                self.shadow.setXOffset(0)
                self.shadow.setYOffset(0)
                self.shadow.setColor(QColor(response.json()['task_status']['color']))
                self.main_window.ui.shot_details_top_frame.setGraphicsEffect(self.shadow)

    def shot_status_update(self, status):
        if status == "IAP":
            modal = OutputPathModal(self)
            if modal.exec_():
                output_path = modal.get_output_path()
                data = {
                    'status': status,
                    'output_path': output_path
                }
            else:
                pass
        else:
            data = {
                'status': status
            }
        qm = QMessageBox()
        result = qm.question(self, 'Shot Buzz Application', "Are you sure with {}".format(status), qm.Yes | qm.No)
        if result == qm.Yes:
            shot_response = api.update_ShotStatus(str(self.shot_details['id']), data)
            if shot_response.status_code == 201:
                if status == "LAP":
                    # Lead Approval
                    Versions.update_ver_status(self, status)
                    LVersions.create_version(self)
                elif status == "LRT":
                    # Lead Rejected
                    Versions.update_ver_status(self, status)
                elif status == "IAP" or status == "IRT" or status == "CRT":
                    # Versions.update_ver_status(self, status)
                    LVersions.update_ver_status(self, status)
                    if status == "IAP":
                        CVersions.create_version(self)
                    # if status == "IAP":
                    #     worker = Worker(self.send_email)  # Any other args, kwargs are passed to the run function
                    #     self.threadpool.start(worker)

                if status != "HRT" or status != "CRT" or status != "HLD":
                    task_api = api.getArtlistByShotId(shot_response.json()['id'])
                    for task in task_api:
                        task_data = {
                            'task_status': status
                        }
                        response = api.updateTask(str(task['id']), task_data)
                    if status == "CRT":
                        CVersions.update_ver_status(self, status)
                self.main_window.ui.status_btn.setText(shot_response.json()['status']['code'])
                self.main_window.ui.status_btn.setStyleSheet(
                    'color:"#3b3839";background-color:{};padding-left:15px;padding-right:15px;padding-top:5px;padding-bottom:5px'.format(
                        shot_response.json()['status']['color']))
                self.shadow = QGraphicsDropShadowEffect()
                self.shadow.setBlurRadius(5)
                self.shadow.setXOffset(0)
                self.shadow.setYOffset(0)
                self.shadow.setColor(QColor(shot_response.json()['status']['color']))
                self.main_window.ui.shot_details_top_frame.setGraphicsEffect(self.shadow)

    def send_email(self):
        from_addr = "shotbuzzalerts@oscarfx.com"
        to_addr = "datasupport@oscarfx.com"

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "{} is ready for Client Upload".format(self.shot_details['name'])
        msg['From'] = self.config['SMTP']['from_addr']
        msg['To'] = to_addr
        task_type = '_'+self.shot_details['task_type']
        path = os.path.join(self.config['STORAGE']['storage_url'],
                                                       self.shot_details['sequence']['project'][
                                                           'client']['name'],
                                                       self.shot_details['sequence']['project']['name'],
                                                       self.shot_details['sequence']['name'],
                                                       self.shot_details['name'], '_forsubmission',task_type)
        path = os.path.join(path, max(os.listdir(path)))

        # Create the body of the message (a plain-text and an HTML version).
        html = """<html><body>
        <div>Dear Data Team, following shot has been approved please download from <strong>SHOT BUZZ</strong><br><br></div>
        <table id="bgtable" align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%">
    <tr>
        <td align="center" valign="top">
            <table border="0" cellpadding="0" cellspacing="0" class="container" style="...">
                <!-- HEADER -->
                <tr>
                    <td align="left">
                        <strong>Client:</strong> 
                    </td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td align="left">
                        <strong>Project:</strong> 
                    </td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td align="left">
                        <strong>Sequence:</strong> 
                    </td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td align="left">
                        <strong>Shot:</strong> 
                    </td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td align="left">
                        <strong>Task Type:</strong> 
                    </td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td align="left">
                        <strong>Approved By:</strong> 
                    </td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td align="left">
                        <strong>Path:</strong> 
                    </td>
                    <td>{}</td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<div>
            </br>
            </br>
            </br>
            </br>
            <h5>Do not reply to this email. This is automated email notification from ShotBuzz Automated Email System.</h5>
            <div style="font-size: 13px; font-family: Tahoma, Helvetica, sans-serif;"><span style="color: rgb(153, 153, 153); font-family: tahoma, sans-serif; font-size: x-small; background-color: rgb(255, 255, 255);">This message and any attachment(s) is intended only for the use of the addressee(s) and may contain information that is PRIVILEGED and CONFIDENTIAL. If you are not the intended addressee(s), you are hereby notified that any use, distribution, disclosure or copying of this communication is strictly prohibited. If you have received this communication in error, please erase all copies of the message and its attachment(s) and notify the sender immediately.</span></div>&nbsp;</div>
            </div>
        </body></html>""".format(self.shot_details['sequence']['project']['client']['name'], self.shot_details['sequence']['project']['name'],self.shot_details['sequence']['name'],self.shot_details['name'],self.shot_details['task_type'],self.main_window.employee_details['fullName'],path)

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(html, 'html')
        msg.attach(part1)

        # Send the message via local SMTP server.
        s = smtplib.SMTP(self.config['SMTP']['host'])
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(from_addr, to_addr, msg.as_string())
        s.quit()

    def message_function(self):
        try:
            self.client.textMessageReceived.disconnect(self.processTextMessage)
        except Exception as e:
            print("MSG FUNCTION", e)
        data = {
            'Name': self.main_window.employee_details['fullName'],
            'message': self.main_window.ui.text_type_edit.toPlainText(),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        post_data = {
            'sender': self.main_window.employee_details['id'],
            'shot': self.shot_details['id'],
            'content': self.main_window.ui.text_type_edit.toPlainText()
        }
        res = api.post_shotMessages(post_data)
        if (res.status_code == 201):
            self.client.sendTextMessage(json.dumps(data))
        self.client.textMessageReceived.connect(self.processTextMessage)
        self.main_window.ui.text_type_edit.clear()

    def processTextMessage(self, message):
        message_json = json.loads(message)
        if self.chat_area_widget is None:
            self.chat_area_widget = QWidget()
            self.chat_area_widget.setGeometry(QRect(0, 0, 450, 539))
            self.verticalLayout = QVBoxLayout(self.chat_area_widget)
            self.verticalLayout.setSpacing(5)

            self.main_window.ui.scrollArea.setWidget(self.chat_area_widget)
        self.frame = QFrame(self.chat_area_widget)
        self.frame.setMaximumSize(QSize(450, 2000))
        if message_json['Name'] == self.main_window.employee_details['fullName']:
            self.frame.setStyleSheet(u"background-color: rgb(45, 49, 59)")
        else:
            self.frame.setStyleSheet(u"background-color: rgb(35, 39, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(5, 1, 5, 1)
        self.sent_user = QLabel(self.frame)
        font11 = QFont()
        font11.setFamily(u"Sitka Text")
        font11.setPointSize(8)
        self.sent_user.setFont(font11)
        self.sent_user.setStyleSheet(u"border:none;\n"
                                     "color: rgb(154, 154, 154);")

        self.gridLayout.addWidget(self.sent_user)

        self.msg_label = QLabel(self.frame)
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(9)
        self.msg_label.setFont(font12)
        self.msg_label.setStyleSheet(u"border:none;padding-left:20px;")
        self.msg_label.setWordWrap(True)
        self.msg_label.setOpenExternalLinks(True)
        self.msg_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.msg_label)

        self.date_label = QLabel(self.frame)
        self.date_label.setStyleSheet(u"border:none;\n"
                                      "color: rgb(99, 99, 99);")
        self.date_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.date_label)

        self.verticalLayout.addWidget(self.frame)
        self.sent_user.setText(message_json['Name'])
        if os.path.isabs(message_json['message']):
            self.msg_label.setText(
                '<a href="file:{}" style="color: rgb(0, 150, 225);">{}</a>'.format(message_json['message'],
                                                                                    message_json['message']))

        else:
            self.msg_label.setText(message_json['message'])
        self.date_label.setText('({})'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        self.tray_notify(message_json['message'])
        # self.main_window.ui.message_area.append('({})'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))+'<strong>{}</strong>'.format(message_json['Name']) + ': ' + message_json['message'])

    def tray_notify(self, message):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()
        w = QtWidgets.QWidget()
        w.setWindowTitle("Tendril ")
        tray_icon = SystemTrayIcon(QtGui.QIcon(":/oscarfx/icons/oscarfx/icon.png"), w)
        tray_icon.show()
        tray_icon.showMessage('Tendril Pipeline', message)
        app.exec_()

    def fetchShot_Messages(self):
        try:
            if self.chat_area_widget is not None:
                self.chat_area_widget.deleteLater()
        except:
            pass
        shot_messages = api.get_shotMessages(self.shot_details['id'])
        self.chat_area_widget = QWidget()
        self.chat_area_widget.setGeometry(QRect(0, 0, 450, 539))
        self.chat_area_widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.chat_area_widget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_window.ui.scrollArea.setWidget(self.chat_area_widget)
        for message in shot_messages:
            timestamp = datetime.datetime.strptime(message['timestamp'], '%Y-%m-%dT%H:%M:%S.%f').strftime(
                "%Y-%m-%d %H:%M")
            # print(message)
            self.frame = QFrame(self.chat_area_widget)
            self.frame.setMaximumSize(QSize(450, 2000))
            if message['sender'] == self.main_window.employee_details['fullName']:
                self.frame.setStyleSheet(u"background-color: rgb(45, 49, 59)")
            else:
                self.frame.setStyleSheet(u"background-color: rgb(35, 39, 49);")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.gridLayout = QGridLayout(self.frame)
            self.gridLayout.setHorizontalSpacing(0)
            self.gridLayout.setVerticalSpacing(6)
            self.gridLayout.setContentsMargins(5, 1, 5, 1)
            self.sent_user = QLabel(self.frame)
            self.sent_user.setObjectName(u"sent_user")
            font11 = QFont()
            font11.setFamily(u"Sitka Text")
            font11.setPointSize(8)
            self.sent_user.setFont(font11)
            self.sent_user.setStyleSheet(u"border:none;\n"
                                         "color: rgb(154, 154, 154);")

            self.gridLayout.addWidget(self.sent_user)

            self.msg_label = QLabel(self.frame)
            font12 = QFont()
            font12.setFamily(u"Segoe UI")
            font12.setPointSize(9)
            self.msg_label.setFont(font12)
            self.msg_label.setStyleSheet(u"border:none;padding-left:20px;")
            self.msg_label.setWordWrap(True)
            self.msg_label.setOpenExternalLinks(True)
            self.msg_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse)
            self.gridLayout.addWidget(self.msg_label)

            self.date_label = QLabel(self.frame)
            self.date_label.setStyleSheet(u"border:none;\n"
                                          "color: rgb(99, 99, 99);")
            self.date_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            self.gridLayout.addWidget(self.date_label)

            self.verticalLayout.addWidget(self.frame)
            self.sent_user.setText(message['sender'])
            if os.path.isabs(message['content']):
                self.msg_label.setText('<a href="file:{}" style="color: rgb(0, 150, 225);">{}</a>'.format(message['content'], message['content']))

            else:
                self.msg_label.setText(message['content'])
            self.date_label.setText(timestamp)
            # self.main_window.ui.message_area.append('({}) '.format(timestamp)+'<strong style="color:white">{}</strong>'.format(message['sender']) + ': ' + message['content'])

    def calculate_per(self, shot_details, per, employee):
        get_previous_logs(self, shot_details, per, employee)

    def add_percentage(self, type):
        pass
        # modal = perDailog(self, type)
        # # modal.move(self.main_window.geometry().center())
        # if modal.exec_():
        #     if type == "SHOT":
        #         per = modal.getPercentage()
        #         employee = self.main_window.employee_details
        #         self.calculate_per(self.shot_details, per, employee)
        #     else:
        #         data = {
        #             'art_percentage': modal.getPercentage()
        #         }
        #         res = api.updateTask(str(self.task_details['id']), data)
        #         # res = api.update_ShotStatus(self.shot_details['id'], data)
        #         if res.status_code == 201:
        #             self.task_progress = modal.getPercentage()
        #             self.timer = QTimer()
        #             self.timer.timeout.connect(self.task_progressBarAnimated)
        #             self.timer.start()
        # else:
        #     pass

    def progressBarAnimated(self):
        count = self.counter
        pink = "rgb(255, 44, 174)"
        light_green = "rgb(115, 255, 171)"
        orange = "rgb(231, 128, 30)"
        red = "rgb(255, 60, 11)"
        green = "rgb(0, 170, 0)"

        if count < 25:
            color = red
        elif count >= 25 and count < 50:
            color = pink
        elif count >= 50 and count < 75:
            color = orange
        elif count >= 75 and count < 95:
            color = light_green
        elif count >= 95 and count <= 100:
            color = green

        label_color = """QLabel{color: {COLOR}; padding: 0px; background-color: none;}"""
        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(int(count)))
        newColor = label_color.replace("{COLOR}", color)
        # APPLY NEW PERCENTAGE TEXT
        self.main_window.ui.shotPercentage.setText(newHtml)
        self.main_window.ui.shotPercentage.setStyleSheet(newColor)
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
    border-radius: 110px;	
    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0) , stop:{STOP_2} {COLOR});
}
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - count) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        self.main_window.ui.shotProgress.setStyleSheet(newStylesheet)
        if count < self.progress:
            self.counter += 1
        elif self.progress < count:
            self.counter -= 1
        else:
            self.timer.stop()
            self.counter = self.progress

    def task_progressBarAnimated(self):
        count = self.task_counter
        pink = "rgb(255, 44, 174)"
        light_green = "rgb(115, 255, 171)"
        orange = "rgb(231, 128, 30)"
        red = "rgb(255, 60, 11)"
        green = "rgb(0, 170, 0)"

        if count < 25:
            color = red
        elif count >= 25 and count < 50:
            color = pink
        elif count >= 50 and count < 75:
            color = orange
        elif count >= 75 and count < 95:
            color = light_green
        elif count >= 95 and count <= 100:
            color = green

        label_color = """QLabel{color: {COLOR}; padding: 0px; background-color: none;}"""
        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(int(count)))
        newColor = label_color.replace("{COLOR}", color)
        # APPLY NEW PERCENTAGE TEXT
        # self.main_window.ui.taskPercentage.setText(newHtml)
        # self.main_window.ui.taskPercentage.setStyleSheet(newColor)
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
    border-radius: 110px;	
    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0) , stop:{STOP_2} {COLOR});
}
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - count) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        # self.main_window.ui.taskProgress.setStyleSheet(newStylesheet)
        # if count < self.task_progress:
        #     self.task_counter += 1
        # elif self.task_progress < count:
        #     self.task_counter -= 1
        # else:
        #     self.timer.stop()
        #     self.task_counter = self.task_progress