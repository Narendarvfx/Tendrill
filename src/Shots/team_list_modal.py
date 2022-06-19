from PySide2 import QtCore
from PySide2.QtCore import QEasingCurve, QPoint, QAbstractAnimation, QSize
from PySide2.QtGui import QPixmap, Qt
from PySide2.QtWidgets import QDialog, QTableWidgetItem, QButtonGroup, QRadioButton, QWidget, QLabel, QHBoxLayout, \
    QMessageBox

import api
from uipy.projects.team_list_modal import Ui_Team_List_Dialog


class Team_List_Modal(QDialog):
    def __init__(self, instance):
        super(Team_List_Modal, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Team_List_Dialog()
        self.ui.setupUi(self)
        self.main_window = instance.main_window
        self.current_row = instance.main_window.ui.all_shots_tbWidget.currentRow()
        self.shot = instance.main_window.ui.all_shots_tbWidget.item(self.current_row, 1).data(1)
        host = self.main_window.geometry()
        point = host.center() - self.rect().center()
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animMove = QtCore.QPropertyAnimation(self, b"pos");
        self.animMove.setDuration(250);
        self.animMove.setStartValue(point - QPoint(0, 30));
        self.animMove.setEndValue(point);
        self.animMove.setEasingCurve(QEasingCurve.OutQuad);
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)
        self.animMove.start(QAbstractAnimation.DeleteWhenStopped)
        self.team_list_data = api.getArtlistByShotId(self.shot['id'])
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.team_tabWid.cellClicked.connect(self.saveData)
        self.team_table()

    def team_table(self):
        self.ui.team_tabWid.setRowCount(len(self.team_list_data))
        button_group = QButtonGroup(self)
        for i, data in enumerate(self.team_list_data):
            teamTabWid = QTableWidgetItem()
            teamTabWid.setData(1, data)
            teamTabWid.setFlags(teamTabWid.flags() & ~QtCore.Qt.ItemIsEditable)
            teamTabWid.setText(data['artist'])
            self.ui.team_tabWid.setItem(i, 0, teamTabWid)
            self.ui.team_tabWid.setItem(i, 1, QTableWidgetItem(str(data['assigned_bids'])))
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            button_group.setExclusive(True)
            checkbox = QRadioButton("Compiler", self)
            button_group.addButton(checkbox)
            if data['compiler'] == 2:
                checkbox.setChecked(True)
            checkbox.setStyleSheet(
                "QRadioButton::indicator {border: 3px solid rgb(52, 59, 72);width: 15px;height: 15px;border-radius: 10px;background: rgb(44, 49, 60);}QRadioButton::indicator:hover {border: 3px solid rgb(58, 66, 81);}QRadioButton::indicator:checked {background: 3px solid rgb(255, 170, 0);border: 3px solid rgb(52, 59, 72);	}")
            self.ui.team_tabWid.setCellWidget(i, 2, checkbox)
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
            self.ui.team_tabWid.setCellWidget(i, 3, lWidget);

    def saveData(self):
        if self.ui.team_tabWid.currentColumn() == 3:
            task_id = self.ui.team_tabWid.item(self.ui.team_tabWid.currentRow(), 0).data(1)
            checked = self.ui.team_tabWid.cellWidget(self.ui.team_tabWid.currentRow(), 2).isChecked()
            md = self.ui.team_tabWid.item(self.ui.team_tabWid.currentRow(), 1).text()
            if checked:
                for artist in self.team_list_data:
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