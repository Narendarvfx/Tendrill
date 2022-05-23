import re
import sys

from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox

import api
from uipy.change_password import Ui_CP_MainWindow


class ChangePassword(QMainWindow):
    def __init__(self, obj):
        super(ChangePassword, self).__init__()
        self.main_window = obj
        self.main_window.ui.change_butt.clicked.connect(lambda: self.validate_pwd())

    def validate_pwd(self):
        old_pwd = self.main_window.ui.old_pwd_le.text()
        new_pwd1 = self.main_window.ui.new_pwd1_le.text()
        new_pwd2 = self.main_window.ui.new_pwd2_le.text()
        user_id = self.main_window.employee_details['id']
        if old_pwd != new_pwd1:
            if new_pwd1 == new_pwd2:
                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"

                # compiling regex
                pat = re.compile(reg)

                # searching regex
                mat = re.search(pat, new_pwd1)

                # validating conditions
                if mat:
                    msg = "Password Changed Successfully"
                    data = {
                        "old_password":old_pwd,
                        "new_password":new_pwd1
                    }
                    res = api.update_password(data, user_id)
                    if res.status_code == 400:
                        msg = "Current Password is incorrect"
                        self.popup_message(False, msg)
                    elif res.status_code == 204:
                        msg = "Password Changed Successfully\n Please logout and login again"
                        self.popup_message(True, msg)
                else:
                    msg = "Password Should be the combination of Uppercase, Lowercase, \n Numeric, Special Character and minimum 8 character length"
                    self.popup_message(False, msg)
            else:
                msg = "Passwords not match"
                self.popup_message(False, msg)
        else:
            msg = "Current Password and New Password Should not be same!"
            self.popup_message(False, msg)

    def popup_message(self, result, message):
        if result:
            msg = QMessageBox()
            msg.setText(message)
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("background-color: rgb(33,193,100);color:'white'")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText(message)
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
            msg.exec_()