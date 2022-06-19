from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QEasingCurve, QPoint, QAbstractAnimation, Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QTableWidgetItem, QDialog, QApplication, QMessageBox

import api
from uipy.clients.add_client_modal import Ui_Cli_Dialog
from src.Projects.projects import Projects


class cliDailog(QDialog):
    def __init__(self, instance, *args, **kwargs):
        super(cliDailog, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Cli_Dialog()
        self.ui.setupUi(self)
        host = instance.main_window
        hostRect = host.geometry();
        point = hostRect.center() - self.rect().center()
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animMove = QtCore.QPropertyAnimation(self, b"pos");
        self.animMove.setDuration(250);
        self.animMove.setStartValue(point - QtCore.QPoint(0, 30));
        self.animMove.setEndValue(point);
        self.animMove.setEasingCurve(QEasingCurve.OutQuad);
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)
        self.animMove.start(QAbstractAnimation.DeleteWhenStopped)
        self.ui.cli_save_btn.setDisabled(True)
        self.ui.cli_name_text.textChanged.connect(lambda: self.textChanged())
        self.ui.cli_save_btn.clicked.connect(lambda: self.save_client())
        self.ui.cli_cancel_btn.clicked.connect(lambda: self.cancel_btn())

        localities = api.get_Localities()
        self.ui.cli_locality_cb.clear()
        self.ui.cli_locality_cb.addItem("Select Client", None)
        for c, locality in enumerate(localities):
            self.ui.cli_locality_cb.addItem("", locality['id'])
            self.ui.cli_locality_cb.setItemText(c + 1,
                                                QtWidgets.QApplication.translate("MainWindow", locality['name'],
                                                                                 None, -1))

    def textChanged(self):
        if self.ui.cli_name_text.text() != "":
            self.ui.cli_save_btn.setEnabled(True)
        else:
            self.ui.cli_save_btn.setEnabled(False)

    def save_client(self):
        if self.ui.cli_locality_cb.currentText() != "":
            self.accept()
        else:
            msg = QMessageBox()
            msg.setText("Please Select Locality")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            # msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()

    def cancel_btn(self):
        self.reject()

    def getName(self):
        return self.ui.cli_name_text.text()

    def getCountry(self):
        return self.ui.cli_country_text.text()

    def getLocality(self):
        locality_name = self.ui.cli_locality_cb.currentText()
        return locality_name


class Clients(object):
    def __init__(self, obj, parent=None):
        super(Clients, self).__init__()
        self.main_window = obj
        self.show_clients()
        try:
            self.main_window.ui.cli_table.cellDoubleClicked.disconnect()
            self.main_window.ui.cli_add_btn.clicked.disconnect()
            self.main_window.ui.pro_add_btn.clicked.disconnect()
        except:
            pass
        self.main_window.ui.cli_table.cellDoubleClicked.connect(lambda: self.tableClicked())
        self.main_window.ui.cli_add_btn.clicked.connect(lambda: self.add_client())

    def show_clients(self):
        pixmap = QPixmap("")
        splash = QtWidgets.QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)
        splash.setMask(pixmap.mask())
        splash.setStyleSheet('background:rgb(39, 44, 54)')
        splash.showMessage("<p style='color:white'><h3>Loading...</h3></p>", Qt.AlignCenter | Qt.AlignCenter, Qt.red)
        splash.show()
        QApplication.processEvents()
        self.client_data = api.get_all_clients()
        self.cli_table = self.main_window.ui.cli_table
        # Row Count
        self.cli_table.setRowCount(len(self.client_data))
        for i, data in enumerate(self.client_data):
            cli_Item = QTableWidgetItem()
            cli_Item.setData(1, data)
            cli_Item.setText(data['name'])
            self.cli_table.setItem(i, 0, cli_Item)
            self.cli_table.setItem(i, 1, QTableWidgetItem(data['country']))
            self.cli_table.setItem(i, 2, QTableWidgetItem(data['locality']))

        # Table will fit the screen horizontally
        self.cli_table.horizontalHeader().setStretchLastSection(False)

    def tableClicked(self):
        c_row = self.main_window.ui.cli_table.currentRow()
        self.c_data = self.main_window.ui.cli_table.item(c_row, 0).data(1)
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.projects_page)
        Projects(self)

    def add_client(self):
        modal = cliDailog(self)
        # modal.move(self.main_window.geometry().center())
        if modal.exec_():
            data = {
                'name': modal.getName(),
                'country': modal.getCountry(),
                'locality': modal.getLocality()
            }
            post_data = api.save_client(data)
            if post_data.status_code == 201:
                response = post_data.json()
                row_count = self.main_window.ui.cli_table.rowCount()
                self.main_window.ui.cli_table.insertRow(row_count)
                tbWid = QTableWidgetItem()
                tbWid.setData(1, response)
                tbWid.setText(response['name'])
                self.main_window.ui.cli_table.setItem(row_count, 0, tbWid)
                self.main_window.ui.cli_table.setItem(row_count, 1, QTableWidgetItem(response['country']))
                self.main_window.ui.cli_table.setItem(row_count, 2, QTableWidgetItem(response['locality']))
        else:
            pass
