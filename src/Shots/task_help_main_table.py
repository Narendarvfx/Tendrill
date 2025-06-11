import datetime
import time

from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCore import QCoreApplication, QSize, QPropertyAnimation, QThreadPool, QEasingCurve, QAbstractAnimation, \
    Slot
from PySide2.QtGui import QFont, Qt, QPixmap, QColor
from PySide2.QtWidgets import QTableWidgetItem, QWidget, QLabel, QHBoxLayout, QApplication, QGraphicsDropShadowEffect, \
    QMessageBox, QProgressBar, QTableWidget, QDialog

import api
from src.Shots.task_help_assign_modal import Task_Help_Assign_Modal
from src.Shots.task_help_shot_details import Task_Help_Shot_Details
from uipy.client_status_change import Ui_Client_Status_Dialog
from src.Shots.Shots_Ingestion import Worker
from src.Shots.assign_modal import Assign_Modal
from src.Shots.client_status_change import ClientStatusDailog
from src.Shots.downloads import DownloadModal
from src.Shots.lead_assign_modal import LeadAssignModal
from src.Shots.shot_details import Shot_Details
from src.Shots.team_list_modal import Team_List_Modal

class TaskHelp_Main(object):
    def __init__(self, obj):
        super(TaskHelp_Main, self).__init__()
        self.main_window = obj
        self.config = api.config
        self.main_window.ui.taskHelp_tbWidget.setRowCount(0)
        self.threadpool = QThreadPool()
        try:
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
        ##Clear Block
        self.main_window.ui.input_TreeWid.clear()
        self.main_window.ui.Pscripts_treeWid.clear()
        self.main_window.ui.Rscripts_treeWid.clear()
        self.main_window.ui.Mscripts_treeWid.clear()
        self.main_window.ui.Ppre_ren_treeWid.clear()
        self.main_window.ui.Rpre_ren_treeWid.clear()
        self.main_window.ui.Mpre_ren_treeWid.clear()
        self.main_window.ui.Poutput_treeWid.clear()
        self.main_window.ui.Routput_treeWid.clear()
        self.main_window.ui.Moutput_treeWid.clear()
        self.main_window.ui.Pqc_treeWid.clear()
        self.main_window.ui.Rqc_treeWid.clear()
        self.main_window.ui.Mqc_treeWid.clear()

        pixmap = QPixmap("")
        splash = QtWidgets.QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)
        splash.setMask(pixmap.mask())
        splash.setStyleSheet('background:rgb(39, 44, 54)')
        splash.move(self.main_window.geometry().center());
        splash.show()
        splash.showMessage("<p style='color:white'><h3>Loading...</h3></p>", Qt.AlignCenter | Qt.AlignCenter,
                           Qt.red)
        QApplication.processEvents()
        self.shots_list = []
        self.default_list = []
        role = self.main_window.employee_details['role']
        # self.role = self.main_window.role
        department = self.main_window.employee_details['department']
        if role == 'TEAM LEAD':
            lead_shots = api.get_lead_shots(str(self.main_window.employee_details['id']), "WTS")
            for shots in lead_shots:
                if shots['shot']['status']['code'] != "CAP" and shots['shot']['status']['code'] != 'IAP' and \
                        shots['shot']['status']['code'] != 'HLD' and shots['shot']['status']['code'] != 'OMT' and shots['shot']['status']['code'] != 'DTC':
                    self.default_list.append(shots['shot'])
                self.shots_list.append(shots['shot'])
            self.main_window.ui.assign_leads_btn.hide()
            self.main_window.ui.sel_all_shtTable_chkBox.hide()
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(0, True)
        elif role == 'SUPERVISOR':
            req_task_Help = api.getRequestedTaskHelps()
            for shots in req_task_Help:
                if shots['task_type'] == department:
                    if shots['status']['code'] != "CAP" and shots['status']['code'] != 'IAP' and shots['status'][
                        'code'] != 'HLD' and shots['status']['code'] != 'OMT' and shots['status']['code'] != 'DTC':
                        self.default_list.append(shots)
                    self.shots_list.append(shots)
            self.main_window.ui.assign_leads_btn.hide()
        elif role == 'PRODUCTION MANAGER':
            req_task_Help = api.getRequestedTaskHelps()
            for shots in req_task_Help:
                if shots['status']['code'] != "CAP" and shots['status']['code'] != 'IAP' and shots['status'][
                    'code'] != 'HLD' and shots['status']['code'] != 'OMT' and shots['status']['code'] != 'DTC':
                    self.default_list.append(shots)
            self.shots_list = req_task_Help
        self.display_table(self.default_list)
        self.main_window.ui.shot_search_btn.clicked.connect(lambda: self.perform_search())
        self.main_window.ui.assign_leads_btn.clicked.connect(lambda: self.assign_leads())
        self.clients = api.get_all_clients()
        self.main_window.ui.client_sel_cb.clear()
        self.main_window.ui.client_sel_cb.addItem("Client", None)
        for c, client in enumerate(self.clients):
            self.main_window.ui.client_sel_cb.addItem("", client['id'])
            self.main_window.ui.client_sel_cb.setItemText(c + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", client['name'],
                                                                                           None, -1))

        self.projects = api.get_all_projects()
        self.main_window.ui.pro_sel_cb.clear()
        self.main_window.ui.pro_sel_cb.addItem("Project", None)
        for p, project in enumerate(self.projects):
            self.main_window.ui.pro_sel_cb.addItem("", project['id'])
            self.main_window.ui.pro_sel_cb.setItemText(p + 1,
                                                       QtWidgets.QApplication.translate("MainWindow", project['name'],
                                                                                        None, -1))

        self.status = api.get_all_status()
        self.main_window.ui.status_sel_cb.clear()
        self.main_window.ui.status_sel_cb.addItem("Status", None)
        for s, status in enumerate(self.status):
            self.main_window.ui.status_sel_cb.addItem("", status['id'])
            self.main_window.ui.status_sel_cb.setItemText(s + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))

        self.sel_cli_id = None;
        self.sel_pro = None
        self.main_window.ui.client_sel_cb.activated.connect(self.filterByClient)
        self.main_window.ui.pro_sel_cb.activated.connect(self.filterByProject)
        self.main_window.ui.status_sel_cb.activated.connect(self.filterByStatus)

    @Slot()
    def perform_search(self):
        text = self.main_window.ui.shot_search_lineEdit.text()
        all_shots = self.shots_list
        data = []
        for shots in all_shots:
            if shots['name'].lower().find(text.lower()) != -1:
                data.append(shots)
        self.reset_filters()
        self.display_table(data)
        # self.display_table(data)

    def reset_filters(self):
        self.main_window.ui.client_sel_cb.clear()
        self.main_window.ui.client_sel_cb.addItem("Select", None)
        for c, client in enumerate(self.clients):
            self.main_window.ui.client_sel_cb.addItem("", client['id'])
            self.main_window.ui.client_sel_cb.setItemText(c + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", client['name'],
                                                                                           None, -1))

        self.main_window.ui.pro_sel_cb.clear()
        self.main_window.ui.pro_sel_cb.addItem("Select", None)
        for p, project in enumerate(self.projects):
            self.main_window.ui.pro_sel_cb.addItem("", project['id'])
            self.main_window.ui.pro_sel_cb.setItemText(p + 1,
                                                       QtWidgets.QApplication.translate("MainWindow", project['name'],
                                                                                        None, -1))

        self.main_window.ui.status_sel_cb.clear()
        self.main_window.ui.status_sel_cb.addItem("Select", None)
        for s, status in enumerate(self.status):
            self.main_window.ui.status_sel_cb.addItem("", status['id'])
            self.main_window.ui.status_sel_cb.setItemText(s + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))

    def filterByClient(self, index):
        self.sel_cli_id = self.main_window.ui.client_sel_cb.itemData(index)
        self.sel_client = self.main_window.ui.client_sel_cb.currentText()
        if self.sel_client != "Select":
            all_shots = self.shots_list
            data = []
            for shots in all_shots:
                if shots['sequence']['project']['client'].lower().find(self.sel_client.lower()) != -1:
                    data.append(shots)
        else:
            data = self.shots_list
        self.display_table(data)
        if self.sel_cli_id is not None:
            self.projects = api.get_client_projects(self.sel_cli_id)

        self.main_window.ui.pro_sel_cb.clear()
        self.main_window.ui.pro_sel_cb.addItem("Select", None)
        for p, project in enumerate(self.projects):
            self.main_window.ui.pro_sel_cb.addItem("", project['id'])
            self.main_window.ui.pro_sel_cb.setItemText(p + 1,
                                                       QtWidgets.QApplication.translate("MainWindow", project['name'],
                                                                                        None, -1))
        self.main_window.ui.status_sel_cb.clear()
        self.main_window.ui.status_sel_cb.addItem("Select", None)
        for s, status in enumerate(self.status):
            self.main_window.ui.status_sel_cb.addItem("", status['id'])
            self.main_window.ui.status_sel_cb.setItemText(s + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))
        self.main_window.ui.pro_sel_cb.activated.connect(self.filterByProject)

    def filterByProject(self, index):
        try:
            self.main_window.ui.shot_search_lineEdit.clear()
        except:
            pass
        self.sel_pro = self.main_window.ui.pro_sel_cb.itemData(index)
        data = []
        all_shots = self.shots_list
        if self.sel_pro is not None:
            for shots in all_shots:
                if shots['sequence']['project']['id'] == self.sel_pro:
                    data.append(shots)
        else:
            if self.sel_cli_id is not None:
                for shots in all_shots:
                    if shots['sequence']['project']['client'].lower().find(self.sel_client.lower()) != -1:
                        data.append(shots)
            else:
                data = self.shots_list

        self.main_window.ui.status_sel_cb.clear()
        self.main_window.ui.status_sel_cb.addItem("Select", None)
        for s, status in enumerate(self.status):
            self.main_window.ui.status_sel_cb.addItem("", status['id'])
            self.main_window.ui.status_sel_cb.setItemText(s + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))
        self.display_table(data)

    def filterByStatus(self, index):
        try:
            self.main_window.ui.shot_search_lineEdit.clear()
        except:
            pass
        self.sel_status = self.main_window.ui.status_sel_cb.itemData(index)
        all_shots = self.shots_list
        data = []
        if self.sel_cli_id is not None:
            if self.sel_pro is not None:
                for shots in all_shots:
                    if shots['sequence']['project']['id'] == self.sel_pro and shots['status']['id'] == self.sel_status:
                        data.append(shots)
            else:
                for shots in all_shots:
                    if shots['sequence']['project']['client'].lower().find(self.sel_client.lower()) != -1 and \
                            shots['status']['id'] == self.sel_status:
                        data.append(shots)
        else:
            if self.sel_pro is not None:
                for shots in all_shots:
                    if shots['sequence']['project']['id'] == self.sel_pro and shots['status']['id'] == self.sel_status:
                        data.append(shots)
            else:
                if self.sel_status is not None:
                    for shots in all_shots:
                        if shots['status']['id'] == self.sel_status:
                            data.append(shots)
                else:
                    data = self.shots_list
        self.display_table(data)

    def display_table(self, shots_data):
        try:
            self.main_window.ui.taskHelp_tbWidget.cellDoubleClicked.disconnect()
            self.main_window.ui.send_btn.clicked.disconnect()
        except:
            pass
        self.artist = ""
        self.team_lead = ""
        self.main_window.ui.taskHelp_tbWidget.setRowCount(0)
        pixmap = QPixmap("")
        splash = QtWidgets.QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)
        splash.setMask(pixmap.mask())
        splash.setStyleSheet('background:rgb(39, 44, 54)')
        splash.move(self.main_window.geometry().center());
        splash.show()
        splash.showMessage("<p style='color:white'><h3>Analyzing...</h3></p>", Qt.AlignCenter | Qt.AlignCenter, Qt.red)
        QApplication.processEvents()
        self.main_window.ui.taskHelp_tbWidget.setRowCount(len(shots_data))
        self.main_window.ui.taskHelp_tbWidget.cellDoubleClicked.connect(lambda: self.cellClicked())
        try:
            for i, shots in enumerate(shots_data):
                self.main_window.ui.taskHelp_tbWidget.setSortingEnabled(False)
                if shots['eta'] is not None:
                    eta = datetime.datetime.strptime(shots['eta'], '%Y-%m-%dT%H:%M:%S').strftime("%d-%m-%Y %H:%M")
                else:
                    eta =""

                all_tasks = api.getArtlistByShotId(shots['id'])
                # self.artist = ''
                # for tasks in all_tasks:
                #     if tasks['compiler'] == 2 or tasks['compiler'] == 0:
                #         self.artist = tasks['artist']
                # for task in shots['task']:
                #     if task['compiler'] == 2 or task['compiler'] == 0:
                #         self.artist = task['artist']['fullName']
                #         self.team_lead = task['artist']['team_lead']
                row_Item = QTableWidgetItem()
                row_Item.setData(1, shots)
                row_Item.setText(shots['shot']['sequence']['project']['client'])
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 0, row_Item)
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 1, QTableWidgetItem(shots['shot']['sequence']['project']['name']))
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 2, QTableWidgetItem(shots['shot']['sequence']['name']))
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 3, QTableWidgetItem(shots['shot']['name']))
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 4, QTableWidgetItem(shots['task_type']))
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 5, QTableWidgetItem(str(shots['shot']['actual_start_frame'])))
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 6, QTableWidgetItem(str(shots['shot']['actual_end_frame'])))
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 7, QTableWidgetItem(str(0)))
                stWidget = QWidget();
                st_label = QLabel();
                st_label.setMaximumSize(QSize(32, 32));
                st_label.setText(shots['status']['code'])
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
                stWidget.setStyleSheet('QWidget{margin-top:5px;margin-bottom:5px;color:white;background-color:'+shots['status']['color']+'}')
                stWidget.setToolTip(shots['status']['name'])
                self.main_window.ui.taskHelp_tbWidget.setCellWidget(i, 8, stWidget)
                bid_item = QTableWidgetItem()
                bid_item.setText(str(shots['bid_days']))
                bid_item.setTextAlignment(Qt.AlignCenter)
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 9, bid_item)
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 10, QTableWidgetItem(eta))
                self.main_window.ui.taskHelp_tbWidget.setItem(i, 11, QTableWidgetItem(self.artist))
                self.aWidget = QWidget();
                self.assign_label = QLabel();
                self.assign_label.setMaximumSize(QSize(32, 32));
                self.assign_label.setScaledContents(True);
                self.assign_label.setPixmap(QPixmap(":/20x20/icons/20x20/cil-user-follow.png"));
                self.aLayout = QHBoxLayout(self.aWidget);
                self.aLayout.addWidget(self.assign_label);
                self.aLayout.setAlignment(Qt.AlignCenter);
                self.aLayout.setContentsMargins(0, 0, 0, 0);
                self.aWidget.setLayout(self.aLayout);
                self.aWidget.setStyleSheet('QWidget{background-color:none}')
                self.aWidget.setToolTip('Assign')
                self.main_window.ui.taskHelp_tbWidget.setCellWidget(i, 12, self.aWidget)
                self.main_window.ui.taskHelp_tbWidget.setSortingEnabled(True)
        except Exception as e:
            print(e)

    def cellClicked(self):
        self.current_row = self.main_window.ui.taskHelp_tbWidget.currentRow()
        self.task_details = self.main_window.ui.taskHelp_tbWidget.item(self.current_row, 0).data(1)
        column = self.main_window.ui.taskHelp_tbWidget.currentColumn()
        if column == 12:
            self.assign_modal()
        elif column == 16:
            self.team_list_modal()
        else:
            self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.shot_details_page)
            ## SHOW ==> DROP SHADOW
            self.shadow = QGraphicsDropShadowEffect()
            self.shadow.setBlurRadius(50)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(self.task_details['status']['color']))
            self.main_window.ui.shot_details_top_frame.setGraphicsEffect(self.shadow)
            Task_Help_Shot_Details(self, type='task')

    def assign_leads(self):
        self.check_data = []
        for i in range(self.main_window.ui.all_shots_tbWidget.rowCount()):
            if self.main_window.ui.all_shots_tbWidget.cellWidget(i, 0).isChecked():
                self.check_data.append(self.main_window.ui.all_shots_tbWidget.item(i, 1).data(1))
        if len(self.check_data) > 0:
            modal = LeadAssignModal(self)
            if modal.exec_():
                pass
            else:
                pass
        else:
            msg = QMessageBox()
            msg.setText("No Shots are Selected \n")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            # msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def assign_modal(self):
        modal = Task_Help_Assign_Modal(self)
        if modal.exec_():
            pass
        else:
            pass

    def team_list_modal(self):
        modal = Team_List_Modal(self)
        if modal.exec_():
            pass
        else:
            pass