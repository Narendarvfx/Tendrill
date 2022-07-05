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
from src.Shots.client_version import CVersions
from src.Shots.lead_versions import LVersions
from src.Shots.output_path_modal import OutputPathModal
from src.Shots.paths_page import PathPage
from src.Shots.taskHelp_Modal import TaskHelp_Modal
from src.Shots.assign_modal import Assign_Modal
from src.Shots.scripts_folder import Scripts_Folder
from src.Shots.annotations_folder import Annotations_Folder
from src.Shots.team_page import Team_Page
from src.Shots.versions import Versions
from src.Versions.Versions_Page import Versions_Page


class Shot_Details(QTreeWidget):
    def __init__(self, obj, type=None):
        super(Shot_Details, self).__init__()
        self.main_window = obj.main_window
        try:
            self.main_window.ui.dep_tabWidget.currentChanged.disconnect()
            self.main_window.ui.shot_details_tabWidget.currentChanged.disconnect()

            ### Folders Disconnect
            self.main_window.ui.input_TreeWid.itemClicked.disconnect()
            self.main_window.ui.Pscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Rscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Mscripts_treeWid.itemClicked.disconnect()
            self.main_window.ui.Poutput_treeWid.itemClicked.disconnect()
            self.main_window.ui.Routput_treeWid.itemClicked.disconnect()
            self.main_window.ui.Moutput_treeWid.itemClicked.disconnect()
        except:
            pass

        #### Hiding Version and Team Tabs
        self.main_window.ui.shot_details_tabWidget.setTabVisible(2, False)
        self.main_window.ui.shot_details_tabWidget.setTabVisible(3, False)
        self.task_details = []
        self.shot_details = []
        self.task_counter = ""
        # creating a timer object
        timer = QTimer(self)
        self.start = False
        eta = None

        self.threadpool = QThreadPool()
        if type == 'task':
            self.task_details = obj.task_details
            self.shot_details = obj.task_details['shot']
            status_code = obj.task_details['task_status']['code']
            status_color = obj.task_details['task_status']['color']
            bid_days = obj.task_details['assigned_bids']
            if obj.task_details['eta']:
                eta = datetime.datetime.strptime(obj.task_details['eta'], '%Y-%m-%dT%H:%M:%S').strftime(
                    "%d-%m-%Y %H:%M")

        else:
            self.shot_details = obj.shot_details
            status_code = obj.shot_details['status']['code']
            status_color = obj.shot_details['status']['color']
            bid_days = obj.shot_details['bid_days']
            if obj.shot_details['eta']:
                eta = datetime.datetime.strptime(obj.shot_details['eta'], '%Y-%m-%dT%H:%M:%S').strftime(
                    "%d-%m-%Y %H:%M")

        self.config = api.config
        self.main_window.ui.shot_details_tabWidget.setCurrentIndex(0)
        self.main_window.ui.shotName_lbl.setText(self.shot_details['name'])
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

        elif self.shot_details['task_type'] == 'ROTO':
            self.main_window.ui.dep_tabWidget.setCurrentIndex(1)

        elif self.shot_details['task_type'] == 'MM':
            self.main_window.ui.dep_tabWidget.setCurrentIndex(2)

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
        elif currentIndex == 1:
            self.main_window.ui.Rscripts_treeWid.clear()

        elif currentIndex == 2:
            self.main_window.ui.Mscripts_treeWid.clear()


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
        data = {
            'task_status': status
        }
        qm = QMessageBox()
        result = qm.question(self, 'Tendrill Application', "Are you sure with {}".format(status), qm.Yes | qm.No)
        if result == qm.Yes:
            response = api.updateTask(str(self.task_details['id']), data)
            if response.status_code == 201:
                shot_data = {
                    'status': status
                }
                if status != "STC":
                    api.update_ShotStatus(str(self.shot_details['id']), shot_data)
                if status == "IP":
                    self.main_window.ui.start_btn.hide()
                    if self.task_details['compiler'] == 2 or self.task_details['compiler'] == 0:
                        self.main_window.ui.qc_btn.show()
                    else:
                        self.main_window.ui.comp_btn.show()
                elif status == "REW":
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
        result = qm.question(self, 'Tendrill Application', "Are you sure with {}".format(status), qm.Yes | qm.No)
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