import configparser
import os
import random
from os.path import exists

import yaml
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QEasingCurve, QPoint, QAbstractAnimation, QCoreApplication, Qt, QObject
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QDialog, QLabel, QComboBox, QMessageBox

import api
from src.filtered_data import get_filtered_data
from _globals import *

class Filters_Panel_Modal(QObject):
    def __init__(self,instance, *args, **kwargs):
        super(Filters_Panel_Modal, self).__init__()
        self.display = instance
        self.main_window = instance.main_window
        self.main_window.ui.pro_filter_cb.activated.connect(self.project_cb_clicked)
        self.main_window.ui.stat_filter_cb.activated.connect(self.status_cb_clicked)
        self.main_window.ui.pro_filter_cb.wheelEvent = lambda event: None
        self.main_window.ui.stat_filter_cb.wheelEvent = lambda event: None
        try:
            self.main_window.ui.set_default_btn.clicked.disconnect()
            self.main_window.ui.apply_filter_btn.clicked.disconnect()
            self.main_window.ui.clear_filter_btn.clicked.disconnect()
        except:
            pass
        # self.main_window.ui.set_default_btn.clicked.connect(lambda : self.set_defaults())
        self.main_window.ui.apply_filter_btn.clicked.connect(lambda : self.apply_filters())
        # self.main_window.ui.clear_filter_btn.clicked.connect(lambda : self.clear_filters())
        self.setup_filters()

    def setup_filters(self):
        self.projects = api.get_all_projects()
        self.main_window.ui.pro_filter_cb.clear()
        self.main_window.ui.pro_filter_cb.addItem("", 0)
        self.main_window.ui.pro_filter_cb.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Select Project",
                                                                                          None, -1))
        for p, project in enumerate(self.projects):
            self.main_window.ui.pro_filter_cb.addItem("", project['id'])
            self.main_window.ui.pro_filter_cb.setItemText(p+1, QtWidgets.QApplication.translate("MainWindow", project['name'],
                                                                                        None, -1))
            self.main_window.ui.pro_filter_cb.setItemChecked(p+1, False)
            for _pid in G_PROJECTS_LIST:
                if _pid['id'] == project['id']:
                    self.main_window.ui.pro_filter_cb.setItemChecked(p+1, True)

        self.status = api.get_all_status()
        self.main_window.ui.stat_filter_cb.clear()
        self.main_window.ui.stat_filter_cb.addItem("", 0)
        self.main_window.ui.stat_filter_cb.setItemText(0, QtWidgets.QApplication.translate("MainWindow", 'Select Status',
                                                                                           None, -1))
        for s, status in enumerate(self.status):
            self.main_window.ui.stat_filter_cb.addItem("", status['id'])
            self.main_window.ui.stat_filter_cb.setItemText(s+1, QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))
            self.main_window.ui.stat_filter_cb.setItemChecked(s+1, False)
            for _sid in G_STATUS_LIST:
                if _sid['id'] == status['id']:
                    self.main_window.ui.stat_filter_cb.setItemChecked(s+1, True)

        # self.init_Client_Labels()
        # self.init_Project_Labels()
        # self.init_Status_Labels()

    def getRandomCol(self):

        r = hex(random.randrange(0, 255))[2:]
        g = hex(random.randrange(0, 255))[2:]
        b = hex(random.randrange(0, 255))[2:]

        random_col = '#' + r + g + b
        return random_col

    def project_cb_clicked(self, index):
        self.sel_pro_id = self.main_window.ui.pro_filter_cb.itemData(index)
        self.sel_project = self.main_window.ui.pro_filter_cb.currentText()
        if self.sel_pro_id in G_PROJECTS_ID_LIST:
            G_PROJECTS_ID_LIST.remove(self.sel_pro_id)
            for i, project in enumerate(G_PROJECTS_LIST):
                if project['id'] == self.sel_pro_id:
                    G_PROJECTS_LIST.pop(i)
        else:
            G_PROJECTS_ID_LIST.append(self.sel_pro_id)
            color = self.getRandomCol()
            dat = {'id': self.sel_pro_id, 'project': self.sel_project, 'color': color}
            G_PROJECTS_LIST.append(dat)
        # self.init_Project_Labels()

    def status_cb_clicked(self, index):
        self.sel_status_id = self.main_window.ui.stat_filter_cb.itemData(index)
        self.sel_status = self.main_window.ui.stat_filter_cb.currentText()
        if self.sel_status_id in G_STATUS_ID_LIST:
            G_STATUS_ID_LIST.remove(self.sel_status_id)
            for i, status in enumerate(G_STATUS_LIST):
                if status['id'] == self.sel_status_id:
                    G_STATUS_LIST.pop(i)
        else:
            G_STATUS_ID_LIST.append(self.sel_status_id)
            color = self.getRandomCol()
            dat = {'id':self.sel_status_id,'status':self.sel_status,'color':color}
            G_STATUS_LIST.append(dat)

        # self.init_Status_Labels()

    def init_Client_Labels(self):
        row = 0
        column = 0
        for i in reversed(range(self.main_window.ui.client_layout.count())):
            self.main_window.ui.client_layout.itemAt(i).widget().deleteLater()
        for client in G_CLIENTS_LIST:
            label = QLabel(self.main_window.ui.client_label_frame)
            label.setObjectName(u"label")
            font = QFont()
            font.setPointSize(9)
            font.setBold(True)
            label.setFont(font)
            label.setStyleSheet("QLabel{background-color: "+client['color']+";}")
            self.main_window.ui.client_layout.addWidget(label, row, column, 1, 1)
            column += 1
            if column > 2:
                column = 0
                row += 1
            label.setText(QCoreApplication.translate("Filters_Panel_Dialog", client['client'], None))

    def init_Project_Labels(self):
        row = 0
        column = 0
        for i in reversed(range(self.main_window.ui.project_layout.count())):
            self.main_window.ui.project_layout.itemAt(i).widget().deleteLater()
        for project in G_PROJECTS_LIST:
            label = QLabel(self.main_window.ui.project_label_frame)
            label.setObjectName(u"label")
            font = QFont()
            font.setPointSize(9)
            font.setBold(True)
            label.setFont(font)
            label.setStyleSheet("QLabel{background-color: " + project['color'] + ";}")
            self.main_window.ui.project_layout.addWidget(label, row, column, 1, 1)
            column += 1
            if column > 2:
                column = 0
                row += 1
            label.setText(QCoreApplication.translate("Filters_Panel_Dialog", project['project'], None))

    def init_Status_Labels(self):
        row = 0
        column = 0
        for i in reversed(range(self.main_window.ui.status_layout.count())):
            self.main_window.ui.status_layout.itemAt(i).widget().deleteLater()
        for status in G_STATUS_LIST:
            label = QLabel(self.main_window.ui.status_label_frame)
            label.setObjectName(u"label")
            font = QFont()
            font.setPointSize(9)
            font.setBold(True)
            label.setFont(font)
            label.setStyleSheet("QLabel{background-color: " + status['color'] + ";}")
            self.main_window.ui.status_layout.addWidget(label, row, column, 1, 1)
            column += 1
            if column > 1:
                column = 0
                row += 1
            label.setText(QCoreApplication.translate("Filters_Panel_Dialog", status['status'], None))

    def apply_filters(self):
        _get_data = get_filtered_data(team_lead=self.main_window.team_lead, teamlead_id=self.main_window.team_lead_id)
        self.display.display_table(_get_data)

    def set_defaults(self):
        _d = {'projects':G_PROJECTS_LIST, 'status':G_STATUS_LIST}
        with open(FILTERS_FILE, 'w') as yaml_file:
            yaml.dump(_d, yaml_file, default_flow_style=False)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        msg = QMessageBox()
        msg.setText("Whola!.. Filters Set to Defaults")
        msg.setWindowTitle("Success")
        msg.setIcon(QMessageBox.Information)
        # msg.setStyleSheet("background-color: rgb(64, 139, 88);color:'white'")
        msg.setFont(font)
        msg.exec_()

    def clear_filters(self):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        qm = QMessageBox()
        qm.setFont(font)
        # qm.setStyleSheet("background-color: rgb(195, 56, 56);color:'white'")
        result = qm.question(self.main_window, 'Shot Buzz Application', "Are you sure to clear the filters", qm.Yes | qm.No)
        if result == qm.Yes:
            G_PROJECTS_LIST.clear()
            G_PROJECTS_ID_LIST.clear()
            G_STATUS_LIST.clear()
            G_STATUS_ID_LIST.clear()
            _data = []

            for j in reversed(range(self.main_window.ui.project_layout.count())):
                self.main_window.ui.project_layout.itemAt(j).widget().deleteLater()
            for k in reversed(range(self.main_window.ui.status_layout.count())):
                self.main_window.ui.status_layout.itemAt(k).widget().deleteLater()
            self.display.display_table(_data)
            try:
                os.remove(FILTERS_FILE)
            except:
                pass




