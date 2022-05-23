from PySide2 import QtCore
from PySide2.QtCore import QEasingCurve, QPoint, QAbstractAnimation
from PySide2.QtWidgets import QTableWidgetItem, QDialog, QMessageBox

import api
from uipy.projects.add_project_modal import Ui_Pro_Dialog


class proDailog(QDialog):
    def __init__(self,instance, *args, **kwargs):
        super(proDailog, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Pro_Dialog()
        self.ui.setupUi(self)
        host = instance.main_window
        hostRect = host.geometry();
        point = hostRect.center() - self.rect().center()
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
        self.ui.cli_name_label.setText(instance.obj.c_data['name'])
        self.ui.pro_save_btn.setDisabled(True)
        self.ui.pro_name_text.textChanged.connect(lambda: self.textChanged())
        self.ui.pro_save_btn.clicked.connect(lambda: self.save_client())
        self.ui.pro_cancel_btn.clicked.connect(lambda: self.cancel_btn())

    def textChanged(self):
        if self.ui.pro_name_text.text() != "":
            self.ui.pro_save_btn.setEnabled(True)
        else:
            self.ui.pro_save_btn.setEnabled(False)

    def save_client(self):
        self.accept()

    def cancel_btn(self):
        self.reject()

    def getProName(self):
        return self.ui.pro_name_text.text()

class Projects(object):
    def __init__(self, obj):
        super(Projects, self).__init__()
        self.obj = obj
        self.main_window = obj.main_window
        self.show_projects()
        try:
            self.main_window.ui.pro_add_btn.clicked.disconnect()
        except:
            pass
        # self.main_window.ui.pro_table.cellDoubleClicked.connect(lambda: self.tableClicked())
        self.main_window.ui.pro_add_btn.clicked.connect(lambda: self.add_project())

    def show_projects(self):
        self.project_data = api.get_client_projects(self.obj.c_data['id'])
        self.pro_table = self.main_window.ui.pro_table
        self.pro_table.setShowGrid(False)
        # Row Count
        self.pro_table.setRowCount(len(self.project_data))
        for i, data in enumerate(self.project_data):
            pro_Item = QTableWidgetItem()
            pro_Item.setData(1, data)
            pro_Item.setText(data['client']['name'])
            self.pro_table.setItem(i, 0, pro_Item)
            self.pro_table.setItem(i, 1, QTableWidgetItem(data['name']))
            self.pro_table.setItem(i, 2, QTableWidgetItem(str(data['status'])))

        # Table will fit the screen horizontally
        self.pro_table.horizontalHeader().setStretchLastSection(False)

    def add_project(self):
        modal = proDailog(self)
        if modal.exec_():
            data = {
                'name': modal.getProName(),
                'client': self.obj.c_data['id'],
                'status': 'YTS'
            }
            post_data = api.save_project(data)
            if post_data.status_code == 201:
                response = post_data.json()
                print(response)
                row_count = self.main_window.ui.pro_table.rowCount()
                print(row_count)
                self.main_window.ui.pro_table.insertRow(row_count)
                tbWid = QTableWidgetItem()
                tbWid.setData(1, response)
                tbWid.setText(self.obj.c_data['name'])
                self.main_window.ui.pro_table.setItem(row_count, 0, tbWid)
                self.main_window.ui.pro_table.setItem(row_count, 1, QTableWidgetItem(response['name']))
                self.main_window.ui.pro_table.setItem(row_count, 2, QTableWidgetItem(str(response['status'])))
            elif post_data.status_code == 500:
                msg = QMessageBox()
                msg.setText("Project Name already exists for this Client \n Please try again with different name \n")
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Critical)
                msg.setStyleSheet("background-color: rgb(202,0,3);")
                msg.exec_()
        else:
            pass