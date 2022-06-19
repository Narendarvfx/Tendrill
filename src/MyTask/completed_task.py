import datetime

from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, Qt, QSize
from PySide2.QtGui import QFont, QColor
from PySide2.QtWidgets import QApplication, QTableWidgetItem, QSizePolicy, QHeaderView, QGraphicsDropShadowEffect, \
    QProgressBar, QWidget, QLabel, QHBoxLayout

import api
from src.Shots.shot_details import Shot_Details


class Completed_Task(object):
    def __init__(self, instance):
        super(Completed_Task, self).__init__()
        self.main_window = instance.main_window
        self.main_window.ui.task_search_lineEdit.hide()
        self.main_window.ui.task_search_btn.hide()
        try:
            self.main_window.ui.task_search_btn.clicked.disconnect()
            self.main_window.ui.task_pending_tableWid.cellDoubleClicked.disconnect()
            self.main_window.ui.task_completed_tableWid.cellDoubleClicked.disconnect()
            self.main_window.ui.task_help_art_tableWid.cellDoubleClicked.disconnect()
        except:
            pass
        task_data = api.get_artist_shots(str(self.main_window.employee_details['id']))
        self.task_filtered_data = [x for x in task_data if
                              (x['task_status']['code'] == "CAP" or x['task_status']['code'] == 'IAP' or
                               x['task_status']['code'] == 'HLD' or x['task_status']['code'] == 'OMT')]
        self.completed_task_page(self.task_filtered_data)
        self.main_window.ui.task_search_btn.clicked.connect(lambda: self.perform_search())
        # self.clients = api.get_all_clients()
        # self.main_window.ui.t_cli_sel_cb.clear()
        # self.main_window.ui.t_cli_sel_cb.addItem("Select", None)
        # for c, client in enumerate(self.clients):
        #     self.main_window.ui.t_cli_sel_cb.addItem("", client['id'])
        #     self.main_window.ui.t_cli_sel_cb.setItemText(c + 1,
        #                                                  QtWidgets.QApplication.translate("MainWindow", client['name'],
        #                                                                                   None, -1))

        self.projects = api.get_all_projects()
        self.main_window.ui.t_pro_sel_cb.clear()
        self.main_window.ui.t_pro_sel_cb.addItem("Select", None)
        for p, project in enumerate(self.projects):
            self.main_window.ui.t_pro_sel_cb.addItem("", project['id'])
            self.main_window.ui.t_pro_sel_cb.setItemText(p + 1,
                                                         QtWidgets.QApplication.translate("MainWindow", project['name'],
                                                                                          None, -1))

        self.status = api.get_all_status()
        self.main_window.ui.t_status_sel_cb.clear()
        self.main_window.ui.t_status_sel_cb.addItem("Select", None)
        for s, status in enumerate(self.status):
            self.main_window.ui.t_status_sel_cb.addItem("", status['id'])
            self.main_window.ui.t_status_sel_cb.setItemText(s + 1,
                                                            QtWidgets.QApplication.translate("MainWindow",
                                                                                             status['name'],
                                                                                             None, -1))

        self.sel_cli_id = None;
        self.sel_pro = None
        # self.main_window.ui.t_cli_sel_cb.activated.connect(self.filterByClient)
        self.main_window.ui.t_pro_sel_cb.activated.connect(self.filterByProject)
        self.main_window.ui.t_status_sel_cb.activated.connect(self.filterByStatus)

    def perform_search(self):
        text = self.main_window.ui.task_search_lineEdit.text()
        all_tasks = self.task_filtered_data
        data = []
        for task in all_tasks:
            if task['shot']['name'].lower().find(text.lower()) != -1:
                data.append(task)

        self.reset_filters()
        self.completed_task_page(data)

    def reset_filters(self):
        self.main_window.ui.t_cli_sel_cb.clear()
        self.main_window.ui.t_cli_sel_cb.addItem("Select", None)
        for c, client in enumerate(self.clients):
            self.main_window.ui.t_cli_sel_cb.addItem("", client['id'])
            self.main_window.ui.t_cli_sel_cb.setItemText(c + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", client['name'],
                                                                                           None, -1))

        self.main_window.ui.t_pro_sel_cb.clear()
        self.main_window.ui.t_pro_sel_cb.addItem("Select", None)
        for p, project in enumerate(self.projects):
            self.main_window.ui.t_pro_sel_cb.addItem("", project['id'])
            self.main_window.ui.t_pro_sel_cb.setItemText(p + 1,
                                                       QtWidgets.QApplication.translate("MainWindow", project['name'],
                                                                                        None, -1))

        self.main_window.ui.t_status_sel_cb.clear()
        self.main_window.ui.t_status_sel_cb.addItem("Select", None)
        for s, status in enumerate(self.status):
            self.main_window.ui.t_status_sel_cb.addItem("", status['id'])
            self.main_window.ui.t_status_sel_cb.setItemText(s + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))

    def filterByClient(self, index):
        try:
            self.main_window.ui.t_pro_sel_cb.activated.disconnect()
            self.main_window.ui.shot_search_lineEdit.clear()
        except:
            pass
        self.sel_cli_id = self.main_window.ui.t_cli_sel_cb.itemData(index)
        self.sel_client = self.main_window.ui.t_cli_sel_cb.currentText()
        if self.sel_client != "Select":
            all_shots = self.task_filtered_data
            data = []
            for shots in all_shots:
                if shots['shot']['sequence']['project']['client'].lower().find(self.sel_client.lower()) != -1:
                    data.append(shots)
        else:
            data = self.task_filtered_data
        self.completed_task_page(data)
        if self.sel_cli_id is not None:
            self.projects = api.get_client_projects()

        self.main_window.ui.t_pro_sel_cb.clear()
        self.main_window.ui.t_pro_sel_cb.addItem("Select", None)
        for p, project in enumerate(self.projects):
            self.main_window.ui.t_pro_sel_cb.addItem("", project['id'])
            self.main_window.ui.t_pro_sel_cb.setItemText(p + 1,
                                                       QtWidgets.QApplication.translate("MainWindow", project['name'],
                                                                                        None, -1))
        self.main_window.ui.t_status_sel_cb.clear()
        self.main_window.ui.t_status_sel_cb.addItem("Select", None)
        for s, status in enumerate(self.status):
            self.main_window.ui.t_status_sel_cb.addItem("", status['id'])
            self.main_window.ui.t_status_sel_cb.setItemText(s + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))
        self.main_window.ui.t_pro_sel_cb.activated.connect(self.filterByProject)

    def filterByProject(self, index):
        try:
            self.main_window.ui.shot_search_lineEdit.clear()
        except:
            pass
        self.sel_pro = self.main_window.ui.t_pro_sel_cb.itemData(index)
        data = []
        all_shots = self.task_filtered_data
        if self.sel_pro is not None:
            for shots in all_shots:
                if shots['shot']['sequence']['project']['id'] == self.sel_pro:
                    data.append(shots)
        else:
            if self.sel_cli_id is not None:
                for shots in all_shots:
                    if shots['shot']['sequence']['project']['client'].lower().find(self.sel_client.lower()) != -1:
                        data.append(shots)
            else:
                data = self.task_filtered_data

        self.main_window.ui.t_status_sel_cb.clear()
        self.main_window.ui.t_status_sel_cb.addItem("Select", None)
        for s, status in enumerate(self.status):
            self.main_window.ui.t_status_sel_cb.addItem("", status['id'])
            self.main_window.ui.t_status_sel_cb.setItemText(s + 1,
                                                          QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))
        self.completed_task_page(data)


    def filterByStatus(self, index):
        try:
            self.main_window.ui.shot_search_lineEdit.clear()
        except:
            pass
        self.sel_status = self.main_window.ui.t_status_sel_cb.itemData(index)
        all_shots = self.task_filtered_data
        data = []
        if self.sel_cli_id is not None:
            if self.sel_pro is not None:
                for shots in all_shots:
                    if shots['shot']['sequence']['project']['id'] == self.sel_pro and shots['task_status']['id'] == self.sel_status:
                        data.append(shots)
            else:
                for shots in all_shots:
                    if shots['shot']['sequence']['project']['client'].lower().find(self.sel_client.lower()) != -1 and shots['task_status']['id'] == self.sel_status:
                        data.append(shots)
        else:
            if self.sel_pro is not None:
                for shots in all_shots:
                    if shots['sequence']['project']['id'] == self.sel_pro and shots['task_status']['id'] == self.sel_status:
                        data.append(shots)
            else:
                if self.sel_status is not None:
                    for shots in all_shots:
                        if shots['task_status']['id'] == self.sel_status:
                            data.append(shots)
                else:
                    data = self.task_filtered_data
        self.completed_task_page(data)

    def completed_task_page(self, task_filtered_data):
        try:
            self.main_window.ui.task_completed_tableWid.cellDoubleClicked.disconnect()
            self.main_window.ui.task_pending_tableWid.cellDoubleClicked.disconnect()
            self.main_window.ui.task_help_art_tableWid.cellDoubleClicked.disconnect()
        except:
            pass
        header = self.main_window.ui.task_completed_tableWid.horizontalHeader()
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        self.main_window.ui.task_completed_tableWid.setRowCount(len(task_filtered_data))
        self.main_window.ui.task_completed_tableWid.cellDoubleClicked.connect(lambda: Completed_Task.cellClicked(self))
        QApplication.processEvents()
        eta = None
        for i, task in enumerate(task_filtered_data):
            if task['eta']:
                eta = datetime.datetime.strptime(task['eta'], '%Y-%m-%dT%H:%M:%S').strftime("%Y-%m-%d %H:%M")
            row_Item = QTableWidgetItem()
            row_Item.setData(1, task)
            row_Item.setText(task['shot']['sequence']['project']['client'])
            # self.main_window.ui.task_completed_tableWid.setItem(i, 0, row_Item)
            self.main_window.ui.task_completed_tableWid.setItem(i, 0,
                                                              QTableWidgetItem(
                                                                  task['shot']['sequence']['project']['name']))
            self.main_window.ui.task_completed_tableWid.setItem(i, 1, QTableWidgetItem(task['shot']['sequence']['name']))
            self.main_window.ui.task_completed_tableWid.setItem(i, 2, QTableWidgetItem(task['shot']['name']))
            self.main_window.ui.task_completed_tableWid.setItem(i, 3, QTableWidgetItem(task['shot']['type']))
            self.main_window.ui.task_completed_tableWid.setItem(i, 4,
                                                              QTableWidgetItem(str(task['shot']['actual_start_frame'])))
            self.main_window.ui.task_completed_tableWid.setItem(i, 5,
                                                              QTableWidgetItem(str(task['shot']['actual_end_frame'])))
            self.main_window.ui.task_completed_tableWid.setItem(i, 6, QTableWidgetItem(str(0)))
            stWidget = QWidget();
            st_label = QLabel();
            st_label.setMaximumSize(QSize(32, 32));
            st_label.setText(task['task_status']['code'])
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
                'QWidget{margin-top:5px;margin-bottom:5px;color:white;background-color:' + task['task_status'][
                    'color'] + '}')
            stWidget.setToolTip(task['task_status']['name'])
            self.main_window.ui.task_completed_tableWid.setCellWidget(i, 7, stWidget)
            self.main_window.ui.task_completed_tableWid.setItem(i, 8, QTableWidgetItem(str(task['assigned_bids'])))
            progressBar = QProgressBar()
            value = task['art_percentage']
            progressBar.setValue(value)
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
            styleSheet = """ QProgressBar {background:transparent;margin-top:5px;margin-bottom:5px;text-align: center;color:white}QProgressBar::chunk {background-color:{COLOR};border-top-right-radius: 13px;border-bottom-right-radius: 13px;} """
            newStyleSheet = styleSheet.replace("{COLOR}", color)
            progressBar.setStyleSheet(newStyleSheet)
            progressBar.setFont(QFont('Arial', 10))
            # progressBar.setStyleSheet("QProgressBar:horizontal {border: 1px solid gray;border-radius: 3px;background: transparent;padding: 1px;text-align: right;margin-right: 10ex;}QProgressBar::chunk:horizontal {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 green, stop: 1 white);margin-right: 2px; /* space */width: 10px;}")
            # self.main_window.ui.task_completed_tableWid.setCellWidget(i, 9, progressBar)
            self.main_window.ui.task_completed_tableWid.setItem(i, 9, QTableWidgetItem(str(eta)))

    def cellClicked(self):
        self.current_row = self.main_window.ui.task_completed_tableWid.currentRow()
        self.task_details = self.main_window.ui.task_completed_tableWid.item(self.current_row, 0).data(1)
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.shot_details_page)
        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(self.task_details['task_status']['color']))
        self.main_window.ui.shot_details_top_frame.setGraphicsEffect(self.shadow)
        Shot_Details(self,type='task')