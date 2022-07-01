import datetime

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QFont, QPixmap, QIcon
from PySide2.QtWidgets import QTableWidgetItem, QApplication, QProgressBar, QHBoxLayout, \
    QWidget, QLabel, QMessageBox

import api
from src.Shots.shot_details import Shot_Details
from src.Shots.versions import Versions

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Pending_Task(object):

    def __init__(self,instance):
        super(Pending_Task, self).__init__()
        self.main_window = instance.main_window
        self.main_window.ui.task_search_lineEdit.hide()
        self.main_window.ui.task_search_btn.hide()
        try:
            self.main_window.ui.mytask_tableWid.customContextMenuRequested.disconnect()
            self.main_window.ui.task_search_btn.clicked.disconnect()
            self.main_window.ui.mytask_tableWid.cellDoubleClicked.disconnect()
        except:
            pass
        self.task_data = api.get_artist_shots(str(self.main_window.employee_details['id']))
        print(self.task_data)
        self.task_filtered_data = [x for x in self.task_data if
                              (x['task_status']['code'] != "CAP" and x['task_status']['code'] != 'IAP' and
                               x['task_status']['code'] != 'HLD' and x['task_status']['code'] != 'OMT' and x['task_status']['code'] != 'IRT' and x['task_status']['code'] != 'LRT')]
        self.pending_task_page(self.task_data)
        # self.main_window.ui.refresh_btn.clicked.connect(lambda: self.pending_task_page(self.task_data))
        self.main_window.ui.refresh_btn.clicked.connect(lambda: self.hai())

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
                                                          QtWidgets.QApplication.translate("MainWindow", status['name'],
                                                                                           None, -1))

        self.sel_cli_id = None;
        self.sel_pro = None
        self.main_window.ui.t_pro_sel_cb.activated.connect(self.filterByProject)
        self.main_window.ui.t_status_sel_cb.activated.connect(self.filterByStatus)
        self.main_window.ui.mytask_tableWid.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.main_window.ui.mytask_tableWid.customContextMenuRequested.connect(self.on_customContextMenuRequested)
        delegate = AlignDelegate(self.main_window.ui.mytask_tableWid)
        for x in range(10):
            self.main_window.ui.mytask_tableWid.setItemDelegateForColumn(x, delegate)
    def hai(self):
        new_task_data = api.get_artist_shots(str(self.main_window.employee_details['id']))
        self.pending_task_page(new_task_data)
        print ("hai")

    def on_customContextMenuRequested(self, pos):
        it = self.main_window.ui.mytask_tableWid.itemAt(pos)
        if it is None: return
        menu = QtWidgets.QMenu()
        menu.setStyleSheet(u"QMenu {\n"
                           "background-color: #ABABAB; /* sets background of the menu */\n"
                           "border-radius: 5px;\n"
                           "border: 1px solid black;\n"
                           "margin:2px;\n"
                           "}\n"

                           "QMenu::item {\n"
                           "/* sets background of menu item. set this to something non-transparent\n"
                           "if you want menu color and menu item color to be different */\n"
                           "background-color: transparent;\n"
                           "padding: 2px 25px 2px 2px;\n"
                           "border: 1px solid transparent;\n"
                           "}\n"

                           "QMenu::item:selected { /* when user selects item using mouse or keyboard */\n"
                           "background-color: rgba(100, 100, 100, 150);\n"
                           "border-color: darkblue;\n"
                           "}")
        font1 = QFont()
        font1.setPointSize(12)
        menu.setFont(font1)
        wip_action = menu.addAction(QIcon(":/custom/icons/custom/tick_icon.png"), "&WIP")
        current_row = self.main_window.ui.mytask_tableWid.currentRow()
        self.task_details = self.main_window.ui.mytask_tableWid.item(current_row, 0).data(Qt.UserRole)
        if self.task_details['compiler'] == 2 or self.task_details['compiler'] == 0:
            stq_action = menu.addAction(QIcon(":/custom/icons/custom/tick_icon.png"), "&Submit to QC")
        else:
            stc_action = menu.addAction(QIcon(":/custom/icons/custom/tick_icon.png"), "&Submit to Compiler")

        action = menu.exec_(self.main_window.ui.mytask_tableWid.viewport().mapToGlobal(pos))
        try:
            if action == wip_action:
                self.wip_status_check("WIP")
            elif action == stq_action:
                self.status_check("STQ")
            elif action == stc_action:
                self.status_check("STC")


        except Exception as e:
            pass


    def status_check(self, status):
        print ('hwh')
        if self.task_details['shot']['status']['code'] == "WIP":
            self.task_status_update(status)

        else:
            msg = QMessageBox()
            msg.setText("Shot not in wip\n")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            # msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def wip_status_check(self, status):
        if self.task_details['shot']['status']['code'] == 'YTS' or self.task_details['shot']['status'][
            'code'] == 'LRT' or self.task_details['shot']['status']['code'] == 'CRT':
            self.task_status_update(status)
            self.pending_task_page(self.task_data)
        else:
            msg = QMessageBox()
            msg.setText("Shot is in QC or Approved and cannot be changed to WIP\n")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            # msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def task_status_update(self, status):
        data = {
            'task_status': status
        }
        qm = QMessageBox()
        result = qm.question(self.main_window , 'Tendrill Application', "Are you sure with status {}".format(status), qm.Yes | qm.No)
        if result == qm.Yes:
            response = api.updateTask(str(self.task_details['id']), data)
            if response.status_code == 201:
                shot_data = {
                    'status': status
                }
                if status != "STC":
                    api.update_ShotStatus(str(self.task_details['shot']['id']), shot_data)
                if status == "STQ":
                    Versions.create_version(self)





    def perform_search(self):
        text = self.main_window.ui.task_search_lineEdit.text()
        all_tasks = self.task_filtered_data
        data = []
        for task in all_tasks:
            if task['shot']['name'].lower().find(text.lower()) != -1:
                data.append(task)
        self.reset_filters()
        self.pending_task_page(data)

    def reset_filters(self):
        # self.main_window.ui.t_cli_sel_cb.clear()
        # self.main_window.ui.t_cli_sel_cb.addItem("Select", None)
        # for c, client in enumerate(self.clients):
        #     self.main_window.ui.t_cli_sel_cb.addItem("", client['id'])
        #     self.main_window.ui.t_cli_sel_cb.setItemText(c + 1,
        #                                                   QtWidgets.QApplication.translate("MainWindow", client['name'],
        #                                                                                    None, -1))

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
        self.pending_task_page(data)
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
        self.pending_task_page(data)


    def filterByStatus(self, index):
        try:
            self.main_window.ui.shot_search_lineEdit.clear()
        except:
            pass
        self.sel_status = self.main_window.ui.t_status_sel_cb.itemData(index)
        all_shots = self.task_filtered_data
        data = []
        # if self.sel_cli_id is not None:
        if self.sel_pro is not None:
            for shots in all_shots:
                if shots['shot']['sequence']['project']['id'] == self.sel_pro and shots['task_status']['id'] == self.sel_status:
                    data.append(shots)
        else:
            for shots in all_shots:
                if shots['task_status']['id'] == self.sel_status:
                    data.append(shots)

        self.pending_task_page(data)

    def pending_task_page(self, task_filtered_data):
        try:
            self.main_window.ui.mytask_tableWid.cellDoubleClicked.disconnect()
        except:
            pass
        pixmap = QPixmap("")
        splash = QtWidgets.QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)
        splash.setMask(pixmap.mask())
        splash.setStyleSheet('background:rgb(39, 44, 54)')
        splash.move(self.main_window.geometry().center());
        splash.showMessage("<p style='color:white'><h3>Loading...</h3></p>", Qt.AlignCenter | Qt.AlignCenter,
                           Qt.red)
        splash.show()
        QApplication.processEvents()
        header = self.main_window.ui.mytask_tableWid.horizontalHeader()
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        self.main_window.ui.mytask_tableWid.setRowCount(len(task_filtered_data))
        self.main_window.ui.mytask_tableWid.cellDoubleClicked.connect(lambda: Pending_Task.cellClicked(self))
        eta = None
        for i, _task in enumerate(task_filtered_data):
            if _task['eta']:
                eta = datetime.datetime.strptime(_task['eta'], '%Y-%m-%dT%H:%M:%S').strftime("%Y-%m-%d %H:%M")
            row_Item = QTableWidgetItem()
            row_Item.setData(Qt.UserRole, _task)
            row_Item.setText(_task['shot']['sequence']['project']['name'])
            # self.main_window.ui.mytask_tableWid.setItem(i, 0, row_Item)
            self.main_window.ui.mytask_tableWid.setItem(i, 0,
                                                           row_Item)
            self.main_window.ui.mytask_tableWid.setItem(i, 1, QTableWidgetItem(_task['shot']['sequence']['name']))
            self.main_window.ui.mytask_tableWid.setItem(i, 2, QTableWidgetItem(_task['shot']['name']))
            self.main_window.ui.mytask_tableWid.setItem(i, 3, QTableWidgetItem(_task['shot']['type']))
            self.main_window.ui.mytask_tableWid.setItem(i, 4, QTableWidgetItem(str(_task['shot']['actual_start_frame'])))
            self.main_window.ui.mytask_tableWid.setItem(i, 5, QTableWidgetItem(str(_task['shot']['actual_end_frame'])))
            self.main_window.ui.mytask_tableWid.setItem(i, 6, QTableWidgetItem(str(_task['shot']['actual_end_frame']-_task['shot']['actual_start_frame'])))
            stWidget = QWidget();
            st_label = QLabel();
            st_label.setMinimumSize(QSize(21, 21));
            st_label.setMaximumSize(QSize(21, 21));
            st_label.setStyleSheet("border-radius:10px;background-color:"+ _task['shot']['status']['color'])
            st_label.setAlignment(Qt.AlignCenter)
            st_label1 = QLabel();
            st_label1.setMaximumSize(QSize(35, 35));
            st_label1.setText(_task['shot']['status']['code'])
            font = QFont()
            font.setPointSize(10)
            font.setFamily('Arial')
            font.setBold(True)
            st_label1.setFont(font)
            st_label1.setAlignment(Qt.AlignCenter)
            stLayout = QHBoxLayout(stWidget);
            stLayout.addWidget(st_label);
            stLayout.addWidget(st_label1);
            stLayout.setAlignment(Qt.AlignCenter);
            stLayout.setContentsMargins(0, 0, 0, 0);
            stWidget.setLayout(stLayout);
            stWidget.setToolTip(_task['shot']['status']['name'])
            self.main_window.ui.mytask_tableWid.setCellWidget(i, 7, stWidget)
            self.main_window.ui.mytask_tableWid.setItem(i, 8, QTableWidgetItem(str(_task['assigned_bids'])))
            progressBar = QProgressBar()
            value = _task['art_percentage']
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
            self.main_window.ui.mytask_tableWid.setItem(i, 9, QTableWidgetItem(str(eta)))

            
    def cellClicked(self):
        self.current_row = self.main_window.ui.mytask_tableWid.currentRow()
        self.task_details = self.main_window.ui.mytask_tableWid.item(self.current_row, 0).data(Qt.UserRole)
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.shot_details_page)
        Shot_Details(self, type='task')