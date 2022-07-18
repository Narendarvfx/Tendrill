import datetime

import pytz
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QSize, QThreadPool, Slot, QDateTime, QDate
from PySide2.QtGui import QColor, QFont, QPixmap, Qt, QIcon
from PySide2.QtWidgets import QApplication, QGraphicsDropShadowEffect, QHBoxLayout, QLabel, QMessageBox, QProgressBar, \
    QTableWidgetItem, QWidget, QComboBox

import api
from _globals import *
from src.Shots.Worker_Class import Worker
from src.Shots.assign_modal import Assign_Modal
from src.Shots.client_version import CVersions
from src.Shots.downloads import DownloadModal
from src.Shots.lead_assign_modal import LeadAssignModal
from src.Shots.lead_versions import LVersions
from src.Shots.output_path_modal import OutputPathModal
from src.Shots.retake_path_modal import RetakePathModal
from src.Shots.shot_details import Shot_Details
from src.Shots.shots_edit_modal import Shots_Edit_Modal
from src.Shots.team_list_modal import Team_List_Modal
from src.Shots.versions import Versions

from src.filtered_data import get_filtered_data
from src.filters_panel import Filters_Panel_Modal
from src.reports import live_production


class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self._changed = False

    def flags(self, index):
        return Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)
        self._changed = True

    def hidePopup(self):
        if not self._changed:
            print(self._changed)
            super(CheckableComboBox, self).hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == QtCore.Qt.Checked

    def setItemChecked(self, index, checked=True):
        item = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)

class All_Shots(object):
    def __init__(self, obj):
        super(All_Shots, self).__init__()

        self.main_window = obj
        self.config = api.config
        self.main_window.ui.all_shots_tbWidget.setRowCount(0)
        self.threadpool = QThreadPool()
        try:
            worker = Worker(self.disconnect_slots)  # Any other args, kwargs are passed to the run function
            self.threadpool.start(worker)
        except Exception as e:
            pass
        #Clear Block
        self.main_window.ui.input_TreeWid.clear()
        self.main_window.ui.Pscripts_treeWid.clear()
        self.main_window.ui.Rscripts_treeWid.clear()
        self.main_window.ui.Mscripts_treeWid.clear()
        self.main_window.ui.Poutput_treeWid.clear()
        self.main_window.ui.Routput_treeWid.clear()
        self.main_window.ui.Moutput_treeWid.clear()
        QApplication.processEvents()
        self.main_window.ui.sel_all_shtTable_chkBox.setChecked(False)
        header = self.main_window.ui.all_shots_tbWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(13, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(14, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(15, QtWidgets.QHeaderView.ResizeToContents)
        self.shots_list = []
        self.default_list = []
        self.check_roles()
        self.main_window.ui.refresh_btn.clicked.connect(lambda: self.refresh_all())
        # self.main_window.ui.shot_search_btn.clicked.connect(lambda: self.perform_search())
        self.main_window.ui.sel_all_shtTable_chkBox.toggled.connect(lambda: self.select_all_shots())
        self.main_window.ui.assign_leads_btn.clicked.connect(lambda: self.assign_leads())
        self.main_window.ui.all_shots_tbWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.main_window.ui.all_shots_tbWidget.customContextMenuRequested.connect(self.on_customContextMenuRequested)
        # self.main_window.ui.download_btn.clicked.connect(lambda: self.download_shots())
        # self.main_window.ui.cli_approve_btn.clicked.connect(lambda: self.client_approve_update("CAP"))
        # self.main_window.ui.cli_retake_btn.clicked.connect(lambda: self.client_status_update("CRT"))
        # self.main_window.ui.dtc_btn.clicked.connect(lambda: self.deliver_status_update("DTC"))
        # self.main_window.ui.export_btn.clicked.connect(lambda: self.export_to_excel())
        self.sel_cli_id = None;
        self.sel_pro = None
        # self.main_window.ui.tl_sel_cb.activated.connect(self.filterByTL)
        self.status_selected = []
        Filters_Panel_Modal(self)
        # self.main_window.ui.filter_btn.clicked.connect(self.filter_panel)

    @Slot()
    def refresh_all(self):
        self.check_roles()

    # @QtCore.pyqtSlot(QtCore.QPoint)
    def on_customContextMenuRequested(self, pos):
        it = self.main_window.ui.all_shots_tbWidget.itemAt(pos)
        if it is None: return
        # c = it.column()
        # item_range = QtWidgets.QTableWidgetSelectionRange(0, c, self.main_window.ui.all_shots_tbWidget.rowCount() - 1, c)
        # self.main_window.ui.all_shots_tbWidget.setRangeSelected(item_range, True)

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
        assign_action = ''
        approve_action = ''
        reject_action = ''
        edit_action = ''
        if self.role == 'TEAM LEAD' or self.role == 'SUPERVISOR' or self.role == 'QC':
            assign_action = menu.addAction(QIcon(":/custom/icons/custom/tick_icon.png"), "&Assign")
            approve_action = menu.addAction(QIcon(":/custom/icons/custom/tick_icon.png"), "&Approve")
            reject_action = menu.addAction(QIcon(":/custom/icons/custom/tick_icon.png"), "&Reject")
        elif self.role == 'DATA I/O':
            edit_action = menu.addAction(QIcon(":/custom/icons/custom/tick_icon.png"),"&Edit")
        team_action = menu.addAction(QIcon(":/custom/icons/custom/tick_icon.png"), "&Team")

        action = menu.exec_(self.main_window.ui.all_shots_tbWidget.viewport().mapToGlobal(pos))
        try:
            if action == approve_action:
                self.status_check(self.approve_status)
            elif action == reject_action:
                self.status_check(self.retake_status)
            elif action == assign_action:
                self.assign_modal()
            elif action == team_action:
                self.team_list_modal()
            elif action == edit_action:
                self.shot_edit_modal()
        except Exception as e:
            pass
            # self.main_window.ui.all_shots_tbWidget.removeColumn(c)

    def status_check(self, status):
        self.current_row = self.main_window.ui.all_shots_tbWidget.currentRow()
        shot_details = self.main_window.ui.all_shots_tbWidget.item(self.current_row, 1).data(1)
        if self.role == "TEAM LEAD" or self.role == "SUPERVISOR":
            if shot_details['status']['code'] == "STQ":
                self.shot_status_update(status)
            else:
                msg = QMessageBox()
                msg.setText("Shot not submitted Qc\n")
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Critical)
                msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
                msg.exec_()
        if self.role == "QC":
            if shot_details['status']['code'] == "LAP":
                self.shot_status_update(status)
            else:
                msg = QMessageBox()
                msg.setText("Shot not submitted Qc\n")
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Critical)
                msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
                msg.exec_()

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
        result = qm.question(self.main_window, 'Tendrill Application', "Are you sure with {}".format(status), qm.Yes | qm.No)
        if result == qm.Yes:
            self.current_row = self.main_window.ui.all_shots_tbWidget.currentRow()
            column = self.main_window.ui.all_shots_tbWidget.currentColumn()
            shot_response = api.update_ShotStatus(str(self.main_window.ui.all_shots_tbWidget.item(self.current_row, 1).data(1)['id']), data)
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

    def filter_panel(self):
        filter_pan = Filters_Panel_Modal(self)
        if filter_pan.exec_():
            pass
        else:
            pass

    def check_roles(self):
        self.approve_status = ""
        self.retake_status = ""
        self.client_retake_status = ""
        self.hold_status = ""
        self.role = self.main_window.employee_details['role']
        self.department = self.main_window.employee_details['department']
        if self.role == 'SUPERVISOR' or self.role == 'AST SUPERVISOR':
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(13, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(14, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(15, True)
            G_DEPARTMENT_LIST.append(self.department)
            self.approve_status = "LAP"
            self.retake_status = "LRT"
        elif self.role == 'PRODUCTION MANAGER' or self.role == 'AST PRODUCTION MANAGER':
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(13, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(14, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(15, True)

            G_DEPARTMENT_LIST.extend(['PAINT', 'ROTO', 'MM', 'COMP'])
            self.approve_status = "IAP"
            self.retake_status = "IRT"
            self.client_retake_status = "CRT"
            self.hold_status = "HLD"
        elif self.role == 'TEAM LEAD':
            self.main_window.ui.assign_leads_btn.hide()
            self.main_window.ui.sel_all_shtTable_chkBox.hide()
            # self.main_window.ui.tl_sel_cb.hide()
            # self.main_window.ui.export_btn.hide()
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(0, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(13, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(14, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(15, True)
            self.main_window.team_lead = True
            self.main_window.team_lead_id = self.main_window.employee_details['id']
            self.approve_status = "LAP"
            self.retake_status = "LRT"
        elif self.role == 'QC':
            self.main_window.ui.assign_leads_btn.hide()
            self.main_window.ui.sel_all_shtTable_chkBox.hide()
            # self.main_window.ui.tl_sel_cb.hide()
            # self.main_window.ui.export_btn.hide()
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(0, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(13, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(14, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(15, True)
            G_DEPARTMENT_LIST.append(self.department)
            self.approve_status = "IAP"
            self.retake_status = "IRT"
            self.client_retake_status = "CRT"
            self.hold_status = "HLD"
        elif self.role == 'DATA I/O':
            self.main_window.ui.assign_leads_btn.hide()
            # self.main_window.ui.download_btn.show()
            # self.main_window.ui.dtc_btn.show()
            # self.main_window.ui.cli_retake_btn.show()
            # self.main_window.ui.cli_approve_btn.show()
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(13, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(14, True)
            self.main_window.ui.all_shots_tbWidget.setColumnHidden(15, True)
            G_DEPARTMENT_LIST.extend(['PAINT', 'ROTO', 'MM', 'COMP'])
        self._data = get_filtered_data(team_lead=self.main_window.team_lead, teamlead_id=self.main_window.team_lead_id)
        self.display_table(self._data)

    @Slot()
    def perform_search(self):
        text = self.main_window.ui.shot_search_lineEdit.text()
        all_shots = self._data
        data = []
        for shots in all_shots:
            if shots['name'].lower().find(text.lower()) != -1:
                data.append(shots)
        self.display_table(data)

    def filterByTL(self, index):
        try:
            self.main_window.ui.shot_search_lineEdit.clear()
        except:
            pass
        self.sel_tl = self.main_window.ui.tl_sel_cb.currentText()
        all_shots = self.shots_list
        data = []
        if self.sel_tl != "Select Team Lead":
            for shots in all_shots:
                if shots['team_lead']:
                    if shots['team_lead'] == self.sel_tl:
                        data.append(shots)
        else:
            data = self.shots_list
        self.display_table(data)

    def disconnect_slots(self):
        try:
            self.main_window.ui.all_shots_tbWidget.customContextMenuRequested.disconnect()
            self.main_window.ui.apply_filter_btn.clicked.disconnect()
            self.main_window.ui.refresh_btn.clicked.disconnect()
            # self.main_window.ui.tl_sel_cb.activated.disconnect()
            self.main_window.ui.all_shots_tbWidget.cellDoubleClicked.disconnect()
            # self.main_window.ui.shot_search_btn.clicked.disconnect()
            self.main_window.ui.sel_all_shtTable_chkBox.toggled.disconnect()
            self.main_window.ui.assign_leads_btn.clicked.disconnect()
            # self.main_window.ui.download_btn.clicked.disconnect()
            # self.main_window.ui.cli_approve_btn.clicked.disconnect()
            # self.main_window.ui.cli_retake_btn.clicked.disconnect()
            # self.main_window.ui.dtc_btn.clicked.disconnect()
            # self.main_window.ui.export_btn.clicked.disconnect()
            # self.main_window.ui.taskHelp_btn.clicked.disconnect()
            # self.main_window.ui.add_per_btn.clicked.disconnect()

            self.main_window.ui.dep_tabWidget.currentChanged.disconnect()
            self.main_window.ui.shot_details_tabWidget.currentChanged.disconnect()
            self.main_window.ui.assign_btn.clicked.disconnect()

            ### Folders Disconnect
            # self.main_window.ui.input_TreeWid.itemClicked.disconnect()
            # self.main_window.ui.Pscripts_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Rscripts_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Mscripts_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Ppre_ren_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Rpre_ren_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Mpre_ren_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Poutput_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Routput_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Moutput_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Pqc_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Rqc_treeWid.itemClicked.disconnect()
            # self.main_window.ui.Mqc_treeWid.itemClicked.disconnect()

            #Filters Disconnect
            # self.main_window.ui.pro_sel_cb.activated.disconnect()
            self.main_window.ui.shot_search_lineEdit.clear()
        except:
            pass

    def display_table(self, shots_data):
        try:
            self.main_window.ui.all_shots_tbWidget.cellDoubleClicked.disconnect()
        except:
            pass
        self.main_window.ui.all_shots_tbWidget.setRowCount(0)
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
        self.main_window.ui.all_shots_tbWidget.setRowCount(len(shots_data))
        self.main_window.ui.all_shots_tbWidget.cellDoubleClicked.connect(lambda: self.cellClicked())
        for i, shots in enumerate(shots_data):
            self.artist = ""
            self.team_lead = ""
            self.main_window.ui.all_shots_tbWidget.setSortingEnabled(False)
            pending_mandays = 0
            pm = float(shots['bid_days'])/100*float(shots['progress'])
            pending_mandays = shots['bid_days']-pm
            eta = ""
            eta_item = QTableWidgetItem();
            if shots['eta']:
                eta = datetime.datetime.strptime(shots['eta'], '%Y-%m-%dT%H:%M:%S')
                eta_item.setData(Qt.DisplayRole, QDate(eta.year, eta.month, eta.day))
            try:
                if shots['team_lead']:
                    self.team_lead = shots['team_lead']
            except Exception as e:
                pass
            if shots['artist']:
                    self.artist = shots['artist']
            row_Item = QTableWidgetItem()
            row_Item.setData(1, shots)
            row_Item.setText(shots['sequence']['project']['name'])
            checkbox = QtWidgets.QCheckBox()
            checkbox.setStyleSheet('QWidget{background-color:none}')
            self.main_window.ui.all_shots_tbWidget.setCellWidget(i, 0, checkbox)
            self.main_window.ui.all_shots_tbWidget.setItem(i, 1, row_Item)
            self.main_window.ui.all_shots_tbWidget.setItem(i, 2, QTableWidgetItem(shots['sequence']['name']))
            self.main_window.ui.all_shots_tbWidget.setItem(i, 3, QTableWidgetItem(shots['name']))
            self.main_window.ui.all_shots_tbWidget.setItem(i, 4, QTableWidgetItem(shots['task_type']))
            stWidget = QWidget();
            st_label = QLabel();
            st_label.setMinimumSize(QSize(21, 21));
            st_label.setMaximumSize(QSize(21, 21));
            st_label.setStyleSheet("border-radius:10px;background-color:"+ shots['status']['color'])
            st_label.setAlignment(Qt.AlignCenter)
            st_label1 = QLabel();
            st_label1.setMaximumSize(QSize(35, 35));
            st_label1.setText(shots['status']['code'])
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
            stWidget.setToolTip(shots['status']['name'])
            self.main_window.ui.all_shots_tbWidget.setCellWidget(i, 5, stWidget)
            self.main_window.ui.all_shots_tbWidget.setItem(i, 6, QTableWidgetItem(self.artist))
            self.main_window.ui.all_shots_tbWidget.setItem(i, 7, QTableWidgetItem(self.team_lead))
            self.main_window.ui.all_shots_tbWidget.setItem(i, 8, QTableWidgetItem(str(shots['actual_start_frame'])))
            self.main_window.ui.all_shots_tbWidget.setItem(i, 9, QTableWidgetItem(str(shots['actual_end_frame'])))
            self.main_window.ui.all_shots_tbWidget.setItem(i, 10, QTableWidgetItem(str(shots['actual_end_frame']-shots['actual_start_frame']+1)))

            bid_item = QTableWidgetItem()
            bid_item.setText(str(shots['bid_days']))
            bid_item.setTextAlignment(Qt.AlignCenter)
            self.main_window.ui.all_shots_tbWidget.setItem(i, 11, bid_item)
            self.main_window.ui.all_shots_tbWidget.setItem(i, 12, eta_item)
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
            self.main_window.ui.all_shots_tbWidget.setCellWidget(i, 13, self.aWidget)
            lWidget = QWidget();
            l_label = QLabel();
            l_label.setMaximumSize(QSize(32, 32));
            l_label.setScaledContents(True);
            l_label.setPixmap(QPixmap(":/20x20/icons/20x20/cil-user.png"));
            lLayout = QHBoxLayout(lWidget);
            lLayout.addWidget(l_label);
            lLayout.setAlignment(Qt.AlignCenter);
            lLayout.setContentsMargins(0, 0, 0, 0);
            lWidget.setLayout(lLayout);
            lWidget.setStyleSheet('QWidget{background-color:none}')
            lWidget.setToolTip("Assignees")

            self.main_window.ui.all_shots_tbWidget.setCellWidget(i, 14, lWidget)
            eWidget = QWidget();
            e_label = QLabel();
            e_label.setMaximumSize(QSize(32, 32));
            e_label.setScaledContents(True);
            e_label.setPixmap(QPixmap(":/20x20/icons/20x20/cil-pencil.png"));
            eLayout = QHBoxLayout(eWidget);
            eLayout.addWidget(e_label);
            eLayout.setAlignment(Qt.AlignCenter);
            eLayout.setContentsMargins(0, 0, 0, 0);
            eWidget.setLayout(eLayout);
            eWidget.setStyleSheet('QWidget{background-color:none}')
            eWidget.setToolTip("Edit")

            self.main_window.ui.all_shots_tbWidget.setCellWidget(i, 15, eWidget)
            self.main_window.ui.all_shots_tbWidget.setSortingEnabled(True)

    def cellClicked(self):
        self.current_row = self.main_window.ui.all_shots_tbWidget.currentRow()
        column = self.main_window.ui.all_shots_tbWidget.currentColumn()
        self.shot_details = self.main_window.ui.all_shots_tbWidget.item(self.current_row, 1).data(1)
        if column == 14:
            self.assign_modal()
        elif column == 15:
            self.team_list_modal()
        elif column == 16:
            self.shot_edit_modal()
        else:
            self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.shot_details_page)
            ## SHOW ==> DROP SHADOW
            self.shadow = QGraphicsDropShadowEffect()
            self.shadow.setBlurRadius(50)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(self.shot_details['status']['color']))
            self.main_window.ui.shot_details_top_frame.setGraphicsEffect(self.shadow)
            Shot_Details(self)

    def select_all_shots(self):
        if self.main_window.ui.sel_all_shtTable_chkBox.isChecked():
            for i in range(self.main_window.ui.all_shots_tbWidget.rowCount()):
                self.main_window.ui.all_shots_tbWidget.cellWidget(i, 0).setChecked(True)
        else:
            for i in range(self.main_window.ui.all_shots_tbWidget.rowCount()):
                self.main_window.ui.all_shots_tbWidget.cellWidget(i, 0).setChecked(False)

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
            msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def assign_modal(self):
        modal = Assign_Modal(self)
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

    def shot_edit_modal(self):
        modal = Shots_Edit_Modal(self)
        if modal.exec_():
            pass
        else:
            pass

    def client_approve_update(self, status):
        self.selected_shots = []
        for i in range(self.main_window.ui.all_shots_tbWidget.rowCount()):
            if self.main_window.ui.all_shots_tbWidget.cellWidget(i, 0).isChecked():
                self.selected_shots.append(self.main_window.ui.all_shots_tbWidget.item(i, 1).data(1))
                shot = self.main_window.ui.all_shots_tbWidget.item(i, 1).data(1)
                if shot['status']['code'] == "DTC":
                    data = {
                        'status': status
                    }
                    res = api.update_ShotStatus(str(shot['id']), data)
                    if res.status_code == 201:
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
                            'QWidget{margin-top:5px;margin-bottom:5px;color:white;background-color:' +
                            res.json()['status']['color'] + '}')
                        stWidget.setToolTip(res.json()['status']['name'])
                        self.main_window.ui.all_shots_tbWidget.setCellWidget(i, 10, stWidget)

        if not len(self.selected_shots) > 0:
            msg = QMessageBox()
            msg.setText("Please select atleast one shot to continue! \n")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def client_status_update(self, status):
        self.rejected_shots = []
        self.index_shots = []
        for i in range(self.main_window.ui.all_shots_tbWidget.rowCount()):
            if self.main_window.ui.all_shots_tbWidget.cellWidget(i, 0).isChecked():
                self.rejected_shots.append(self.main_window.ui.all_shots_tbWidget.item(i, 1).data(1))
                shot = self.main_window.ui.all_shots_tbWidget.item(i, 1).data(1)
                data = {
                    'index': i,
                    'shot': shot['id']
                }
                self.index_shots.append(data)

        if len(self.rejected_shots) > 0:
            modal = RetakePathModal(self)
            if modal.exec_():
                retake_path = modal.get_retake_path()
            else:
                pass
            for shots in self.rejected_shots:
                if shots['status']['code'] == "DTC":
                    data = {
                            'status': 'CRT',
                            'retake_path': retake_path
                        }
                    res = api.update_ShotStatus(str(shots['id']), data)
                    CVersions.update_clientver_status(self, shots['id'], status)
            msg = QMessageBox()
            msg.setText("Successfully Updated, please refresh.. \n")
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("background-color: rgb(0,204,0);color:'white'")
            msg.exec_()
            # modal = ClientStatusDailog(self)
            # if modal.exec_():
            #     pass
        else:
            msg = QMessageBox()
            msg.setText("Please select atleast one shot to continue! \n")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def deliver_status_update(self, status):
        selected_shots = []
        for i in range(self.main_window.ui.all_shots_tbWidget.rowCount()):
            if self.main_window.ui.all_shots_tbWidget.cellWidget(i, 0).isChecked():
                selected_shots.append(self.main_window.ui.all_shots_tbWidget.item(i, 1).data(1))
                shot = self.main_window.ui.all_shots_tbWidget.item(i, 1).data(1)
                tz_NY = pytz.timezone('Asia/Kolkata')
                datetime_NY = datetime.datetime.now(tz_NY)
                submitted_date =  datetime_NY.strftime("%Y-%m-%d %H:%M:%S.%f")
                if shot['version'] is not None:
                    version = int(shot['version'].split("V")[1])
                    version += 1
                else:
                    version = 1
                if shot['status']['code'] == "IAP":
                    data = {
                        'status': status,
                        'version': 'V%03d' % (version),
                        'submitted_date': submitted_date
                    }
                    res = api.update_ShotStatus(str(shot['id']), data)
                    if res.status_code == 201:
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
                            'QWidget{margin-top:5px;margin-bottom:5px;color:white;background-color:' +
                            res.json()['status']['color'] + '}')
                        stWidget.setToolTip(res.json()['status']['name'])
                        self.main_window.ui.all_shots_tbWidget.setCellWidget(i, 10, stWidget)

        if not len(selected_shots) > 0:
            msg = QMessageBox()
            msg.setText("Please select atleast one shot to continue! \n")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def download_shots(self):
        self.selected_shots = []
        for i in range(self.main_window.ui.all_shots_tbWidget.rowCount()):
            if self.main_window.ui.all_shots_tbWidget.cellWidget(i, 0).isChecked():
                self.selected_shots.append(self.main_window.ui.all_shots_tbWidget.item(i, 1).data(1))
        if len(self.selected_shots) > 0:
            modal = DownloadModal(self)
            if modal.exec_():
                pass
            else:
                pass
        else:
            msg = QMessageBox()
            msg.setText("Please select atleast one shot to continue! \n")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def export_to_excel(self):
        live_production.create_workbook()
