import datetime
import time

from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCore import QCoreApplication, QSize, QPropertyAnimation, QThreadPool, QEasingCurve, QAbstractAnimation, \
    Slot
from PySide2.QtGui import QFont, Qt, QPixmap, QColor, QBrush, QPainter
from PySide2.QtWidgets import QTableWidgetItem, QWidget, QLabel, QHBoxLayout, QApplication, QGraphicsDropShadowEffect, \
    QMessageBox, QProgressBar, QTableWidget, QDialog, QMainWindow

import api
from uipy.client_status_change import Ui_Client_Status_Dialog
from src.Shots.Shots_Ingestion import Worker
from src.Shots.assign_modal import Assign_Modal
from src.Shots.client_status_change import ClientStatusDailog
from src.Shots.downloads import DownloadModal
from src.Shots.lead_assign_modal import LeadAssignModal
from src.Shots.shot_details import Shot_Details
from src.Shots.team_list_modal import Team_List_Modal
from PySide2.QtCharts import QtCharts

class All_Users(QMainWindow):
    def __init__(self, obj):
        super(All_Users, self).__init__(obj)
        self.main_window = obj
        try:
            self.main_window.ui.sel_user_status_cbBox.activated.disconnect()
            self.main_window.ui.user_search_btn.clicked.disconnect()
        except:
            pass
        self.config = api.config
        self.main_window.ui.user_tbWidget.setRowCount(10)
        self.threadpool = QThreadPool()
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
        self.users_data = api.get_employees_by_status()
        self.display_table(self.users_data)
        self.main_window.ui.sel_user_status_cbBox.activated.connect(self.filterByStatus)
        self.main_window.ui.user_search_btn.clicked.connect(lambda: self.perform_search())
        data = self.generate_statistics(self.users_data)
        self.create_piechart(data)
        self.slice_value = ""

    @Slot()
    def perform_search(self):
        text = self.main_window.ui.user_search_lineEdit.text()
        all_users = self.users_data
        data = []
        for user in all_users:
            if user['fullName'].lower().find(text.lower()) != -1:
                data.append(user)
        # self.reset_filters()
        self.display_table(data)

    def filterByStatus(self, index):
        try:
            self.main_window.ui.user_search_lineEdit.clear()
        except:
            pass
        self.sel_status = self.main_window.ui.sel_user_status_cbBox.currentText()
        if self.sel_status != "Select":
            users_data = api.get_employees_by_status(self.sel_status)
        else:
            users_data = api.get_employees_by_status()
        self.display_table(users_data)
        data = self.generate_statistics(users_data)
        data = {
            'Yts': 80,
            "Pending": 30,
            "completed": 20
        }
        self.create_piechart(data, replace=True)


    def generate_statistics(self, data):
        self.paint_count = 0
        self.roto_count = 0
        self.mm_count = 0
        self.it_count = 0
        self.manage_count = 0
        self.other_count = 0
        for user in data:
            if user['department'] == "PAINT":
                self.paint_count += 1
            elif user['department'] == "ROTO":
                self.roto_count += 1
            elif user['department'] == "MM":
                self.mm_count += 1
            elif user['department'] == "IT":
                self.it_count += 1
            elif user['department'] == "MANAGEMENT":
                self.manage_count +1
            else:
                self.other_count += 1
        data = {
            "Paint": (self.paint_count, QColor("#e67d75")),
            "Roto": (self.roto_count, QColor("#f0945b")),
            "MM": (self.mm_count, QColor("#74b6f7")),
            "IT": (self.it_count, QColor("#e67d75")),
            "Management": (self.manage_count, QColor("#aeed8a")),
            "Others": (self.other_count, QColor("e67d75"))
        }
        return data

    def display_table(self, users_data):
        try:
            self.main_window.ui.user_tbWidget.cellDoubleClicked.disconnect()
        except:
            pass
        self.main_window.ui.user_tbWidget.setRowCount(0)
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
        self.main_window.ui.user_tbWidget.setRowCount(len(users_data))
        # self.main_window.ui.all_shots_tbWidget.cellDoubleClicked.connect(lambda: self.cellClicked())
        for i, user in enumerate(users_data):
            user_name = api.getUserById(str(user['profile']))
            self.main_window.ui.user_tbWidget.setItem(i, 0, QTableWidgetItem(user_name['username']))
            self.main_window.ui.user_tbWidget.setItem(i, 1, QTableWidgetItem(user['fullName']))
            self.main_window.ui.user_tbWidget.setItem(i, 2, QTableWidgetItem(str(user['employee_id'])))
            self.main_window.ui.user_tbWidget.setItem(i, 3, QTableWidgetItem(user['department']))
            self.main_window.ui.user_tbWidget.setItem(i, 4, QTableWidgetItem(user['role']))
            if user['team_lead'] is not None:
                self.main_window.ui.user_tbWidget.setItem(i, 5, QTableWidgetItem(user['team_lead']['fullName']))
            self.main_window.ui.user_tbWidget.setItem(i, 6, QTableWidgetItem(user['employement_status']))

    def cellClicked(self):
        self.current_row = self.main_window.ui.all_shots_tbWidget.currentRow()
        column = self.main_window.ui.all_shots_tbWidget.currentColumn()
        self.shot_details = self.main_window.ui.all_shots_tbWidget.item(self.current_row, 1).data(1)
        if column == 15:
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
            self.shadow.setColor(QColor(self.shot_details['status']['color']))
            self.main_window.ui.shot_details_top_frame.setGraphicsEffect(self.shadow)
            Shot_Details(self)

    def assign_modal(self):
        modal = Assign_Modal(self)
        if modal.exec_():
            pass
        else:
            pass

    def create_piechart(self, user_data, replace=False):
        self.series = QtCharts.QPieSeries()
        for name, (value, color) in user_data.items():
            _slice = self.series.append("<span style=\"color: white;\">{} {}</span>".format(name, value), value)
            _slice.setBrush(color)
            _slice.setLabelVisible(True)
            _slice.setLabelColor(QColor('black'))
        self.series.hovered.connect(self.pie_clicked)

        chart = QtCharts.QChart()
        chart.legend().hide()
        chart.setBackgroundBrush(QBrush(QColor(Qt.transparent)))
        chart.addSeries(self.series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.setTitle("<span style=\"color: white;\">Department Wise Employee Stats</span>")
        chart.setFont(QtGui.QFont("Arial", 12))

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setFont(QtGui.QFont("Arial", 10))
        chartview = QtCharts.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        # chartview.setParent(self.main_window.ui.frame_25)
        try:
            self.main_window.ui.gridLayout_59.removeWidget(chartview)
            chartview.close()
            self.main_window.ui.gridLayout_59.addWidget(chartview, 0, 0, 1, 1)
        except:
            # pass
            self.main_window.ui.gridLayout_59.addWidget(chartview)
        self.main_window.ui.gridLayout_59.update()

    def pie_clicked(self, slice):
        slice.setExploded(True)
        slice.setExplodeDistanceFactor(0.09)
        # slice.setLabelVisible(True)
        for sli in self.series.slices():
            if sli == self.slice_value:
                sli.setExploded(False)
                # sli.setLabelVisible(False)
        self.slice_value = slice
