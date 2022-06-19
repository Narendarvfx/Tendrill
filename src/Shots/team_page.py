import datetime

from PySide2 import QtGui, QtCore
from PySide2.QtCore import QCoreApplication, Qt, QSize
from PySide2.QtGui import QFont, QPixmap
from PySide2.QtWidgets import QApplication, QTableWidgetItem, QRadioButton, QButtonGroup, QHBoxLayout, QLabel, QWidget, \
    QMessageBox, QProgressBar

import api


class Team_Page(QWidget):
    def __init__(self, instance):
        super(Team_Page, self).__init__()
        self.instance = instance
        self.main_window = instance.main_window
        try:
            self.main_window.ui.team_tableWid.cellClicked.disconnect()
        except:
            pass
        self.shot_details = instance.shot_details
        self.employee_details = instance.main_window.employee_details
        self.main_window.ui.team_tableWid.setRowCount(0)
        self.main_window.ui.team_tableWid.cellClicked.connect(lambda: self.saveData())
        self.role = self.employee_details['role']
        self.team_table()

    def team_table(self):
        self.all_tasks = api.getArtlistByShotId(self.shot_details['id'])
        self.main_window.ui.team_tableWid.setRowCount(len(self.all_tasks))
        button_group = QButtonGroup(self)
        if self.role == "VFX ARTIST":
            self.main_window.ui.team_tableWid.setColumnHidden(9, True)
        for i, task in enumerate(self.all_tasks):
            row_Item = QTableWidgetItem()
            row_Item.setData(1, task)
            row_Item.setText(task['artist'])
            row_Item.setFlags(row_Item.flags() & ~Qt.ItemIsEditable)
            row_Item.setFont(QFont('Cambria', 12, QFont.Bold))
            self.main_window.ui.team_tableWid.setItem(i, 0, row_Item)
            status_item = QTableWidgetItem()
            status_item.setText(QCoreApplication.translate("MainWindow", task['task_status']['code'], None))
            status_item.setForeground(QtGui.QColor(task['task_status']['color']))
            status_item.setFlags(status_item.flags() & ~Qt.ItemIsEditable)
            status_item.setTextAlignment(Qt.AlignCenter)
            font = QFont()
            font.setPointSize(12)
            font.setFamily('Arial')
            font.setBold(True)
            status_item.setFont(font)
            self.main_window.ui.team_tableWid.setItem(i, 1, status_item)
            task_bid = QTableWidgetItem()
            task_bid.setText(str(task['assigned_bids']))
            if self.role == "VFX ARTIST":
                task_bid.setFlags(task_bid.flags() & ~Qt.ItemIsEditable)
            self.main_window.ui.team_tableWid.setItem(i, 2, task_bid)
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
            self.main_window.ui.team_tableWid.setCellWidget(i, 3, progressBar)
            # self.main_window.ui.team_tableWid.setItem(i, 3, per)
            chkBoxItem = QTableWidgetItem()

            chkBoxItem.setFlags(~QtCore.Qt.ItemIsUserCheckable | ~QtCore.Qt.ItemIsEnabled)
            button_group.setExclusive(True)
            checkbox = QRadioButton("Compiler", self)
            if self.role == "VFX ARTIST":
                checkbox.setEnabled(False)
            button_group.addButton(checkbox)
            if task['compiler'] == 2:
                checkbox.setChecked(True)
            checkbox.setStyleSheet(
                "QRadioButton{background:none;text-align:center}QRadioButton::indicator {border: 3px solid rgb(52, 59, 72);width: 15px;height: 15px;border-radius: 10px;background: rgb(44, 49, 60);}QRadioButton::indicator:hover {border: 3px solid rgb(58, 66, 81);}QRadioButton::indicator:checked {background: 3px solid rgb(255, 170, 0);border: 3px solid rgb(52, 59, 72);	}")
            self.main_window.ui.team_tableWid.setCellWidget(i, 4, checkbox)
            creation_date = datetime.datetime.strptime(task['creation_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime(
                    "%d-%m-%Y %H:%M")
            self.main_window.ui.team_tableWid.setItem(i, 5, QTableWidgetItem(creation_date))
            eta = datetime.datetime.strptime(task['eta'], '%Y-%m-%dT%H:%M:%S').strftime(
                "%d-%m-%Y %H:%M")
            self.main_window.ui.team_tableWid.setItem(i, 6, QTableWidgetItem(eta))
            start_date = QTableWidgetItem()
            start_date.setText(task['start_date'])
            start_date.setFlags(start_date.flags() & ~Qt.ItemIsEditable)
            self.main_window.ui.team_tableWid.setItem(i, 7, start_date)
            end_date = QTableWidgetItem()
            end_date.setText(task['end_date'])
            end_date.setFlags(start_date.flags() & ~Qt.ItemIsEditable)
            self.main_window.ui.team_tableWid.setItem(i, 8, end_date)
            lWidget = QWidget();
            l_label = QLabel();
            l_label.setMaximumSize(QSize(32, 32));
            l_label.setScaledContents(True);
            l_label.setPixmap(QPixmap(":/custom/icons/custom/tick_icon.png"));
            lLayout = QHBoxLayout(lWidget);
            lLayout.addWidget(l_label);
            lLayout.setAlignment(Qt.AlignCenter);
            lLayout.setContentsMargins(0, 0, 0, 0);
            lWidget.setLayout(lLayout);
            lWidget.setStyleSheet("background:none;")
            self.main_window.ui.team_tableWid.setCellWidget(i, 9, lWidget);

    def saveData(self):
        if self.main_window.ui.team_tableWid.currentColumn() == 9:
            task_id = self.main_window.ui.team_tableWid.item(self.main_window.ui.team_tableWid.currentRow(), 0).data(1)
            checked = self.main_window.ui.team_tableWid.cellWidget(self.main_window.ui.team_tableWid.currentRow(), 4).isChecked()
            md = self.main_window.ui.team_tableWid.item(self.main_window.ui.team_tableWid.currentRow(), 2).text()
            if checked:
                for artist in self.all_tasks:
                    if artist['id'] == task_id['id']:
                        compiler = 2
                    else:
                        compiler = 1
                    update_data = {
                        'compiler': compiler,
                    }
                    api.updateTask(str(artist['id']), update_data)
            update_data = {
                'assigned_bids' : float(md)
            }
            res = api.updateTask(str(task_id['id']), update_data)
            if res.status_code == 201:
                msg = QMessageBox()
                msg.setText("Successfully Updated")
                msg.setWindowTitle("Success")
                msg.setIcon(QMessageBox.Information)
                # msg.setStyleSheet("background-color: rgb(33,193,100);")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setText("Something Went Wrong \n Please try Again \n or Contact Pipeline Administrator \n" + str(res.json()))
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Critical)
                # msg.setStyleSheet("background-color: rgb(202,0,3);")
                msg.exec_()