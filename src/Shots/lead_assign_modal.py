import os

import ntsecuritycon as con
import win32security
from PySide2 import QtCore
from PySide2.QtCore import QEasingCurve, QAbstractAnimation, QPoint
from PySide2.QtWidgets import QDialog, QMessageBox

import api
from uipy.projects.lead_assign_modal import Ui_Lead_Assign_Dialog


class LeadAssignModal(QDialog):
    def __init__(self, instance):
        super(LeadAssignModal, self).__init__()
        self.checked_data = instance.check_data
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Lead_Assign_Dialog()
        self.ui.setupUi(self)
        self.main_window = instance.main_window
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
        try:
            self.ui.lead_cancel_btn.clicked.disconnect()
            self.ui.lead_assign_btn.clicked.disconnect()
        except:
            pass
        self.lead_data = api.getAllArtists()
        if self.main_window.employee_details['role'] == "PRODUCTION MANAGER":
            for lead_data in self.lead_data:
                if lead_data['role'] == "TEAM LEAD":
                    self.ui.sel_lead_cb.addItem(lead_data['fullName'], lead_data['id'])
        else:
            for lead_data in self.lead_data:
                if lead_data['role'] == "TEAM LEAD" and lead_data['department'] == self.main_window.employee_details[
                    'department']:
                    self.ui.sel_lead_cb.addItem(lead_data['fullName'], lead_data['id'])
        self.ui.lead_cancel_btn.clicked.connect(self.close_dialog)
        self.ui.lead_assign_btn.clicked.connect(self.lead_assign)

    def lead_assign(self):
        try:
            for data in self.checked_data:
                self.shot = data
                shot_data = {
                    'shot': data['id'],
                    'lead': self.ui.sel_lead_cb.currentData(),
                    'status': 11,
                    'assigned_by': self.main_window.employee_details['id']
                }
                post_response = api.post_lead_assignment(shot_data)
                # self.create_permission()
                if post_response.status_code == 201:
                    if data['status']['code'] == "RTA":
                        shot_status = {
                            'status': "WTS"
                        }
                        api.update_ShotStatus(str(data['id']), shot_status)

            msg = QMessageBox()
            msg.setText("\nSuccessfully Assigned to " + self.ui.sel_lead_cb.currentText())
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("background-color: rgb(33,193,100);color:'white'")
            msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setText("Something Went Wrong \n Please try Again \n or Contact Pipeline Administrator \n" + str(
                post_response.json()))
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("background-color: rgb(202,0,3,);color:'white'")
            msg.exec_()
        self.close()

    def close_dialog(self):
        self.close()

    ## Creates Permission for shot folders
    def create_permission(self):
        employee_details = api.get_employee_data(str(self.ui.sel_lead_cb.currentData()))
        artist_user_id = api.get_employee_user_name(str(employee_details['profile']))
        dep_dir = '_' + employee_details['department'].lower()
        perm_dir = os.path.join(api.config['STORAGE']['storage_url'], api.config['STORAGE']['parent_directory'],
                                self.shot['sequence']['project']['client'], self.shot['sequence']['project']['name'],
                                self.shot['sequence']['name'], self.shot['name'], dep_dir)
        try:
            FILENAME = perm_dir

            artist, domain, type = win32security.LookupAccountName("", str(artist_user_id['username']))

            sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

            dacl = sd.GetSecurityDescriptorDacl()

            dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                       win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT, con.GENERIC_ALL,
                                       artist)

            sd.SetSecurityDescriptorDacl(1, dacl, 0)
            win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)

        except Exception as e:
            print("Permissions:", e)
