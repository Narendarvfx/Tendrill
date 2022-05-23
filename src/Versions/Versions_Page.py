import datetime

from PySide2.QtWidgets import QTableWidgetItem

import api


class Versions_Page():
    def __init__(self):
        super(Versions_Page, self).__init__()

    def int_ver_table(self):
        all_int_ver = api.getAllShotVersions(str(self.shot_details['id']))
        self.main_window.ui.int_tabWid.setRowCount(len(all_int_ver.json()))
        for i, int_ver in enumerate(all_int_ver.json()):
            verified_date = ""
            verified_by = ""
            sent_date = datetime.datetime.strptime(int_ver['sent_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y-%m-%d %H:%M")
            if int_ver['verified_date']:
                verified_date = datetime.datetime.strptime(int_ver['verified_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y-%m-%d %H:%M")
            if int_ver['verified_by']:
                verified_by = int_ver['verified_by']
            self.main_window.ui.int_tabWid.setItem(i, 0, QTableWidgetItem(str(int_ver['version'])))
            self.main_window.ui.int_tabWid.setItem(i, 1, QTableWidgetItem(str(int_ver['sent_by'])))
            self.main_window.ui.int_tabWid.setItem(i, 2, QTableWidgetItem(str(sent_date)))
            self.main_window.ui.int_tabWid.setItem(i, 3, QTableWidgetItem(str(int_ver['status'])))
            self.main_window.ui.int_tabWid.setItem(i, 4, QTableWidgetItem(str(verified_by)))
            self.main_window.ui.int_tabWid.setItem(i, 5, QTableWidgetItem(str(verified_date)))

    def qc_ver_table(self):
        all_qc_ver = api.getAllQcVersions(str(self.shot_details['id']))
        self.main_window.ui.qc_tabWid.setRowCount(len(all_qc_ver.json()))
        for i, int_ver in enumerate(all_qc_ver.json()):
            verified_date = ""
            verified_by = ""
            sent_date = datetime.datetime.strptime(int_ver['sent_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime(
                "%Y-%m-%d %H:%M")
            if int_ver['verified_date']:
                verified_date = datetime.datetime.strptime(int_ver['verified_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime(
                    "%Y-%m-%d %H:%M")
            if int_ver['verified_by']:
                verified_by = int_ver['verified_by']
            self.main_window.ui.qc_tabWid.setItem(i, 0, QTableWidgetItem(str(int_ver['version'])))
            self.main_window.ui.qc_tabWid.setItem(i, 1, QTableWidgetItem(str(int_ver['sent_by'])))
            self.main_window.ui.qc_tabWid.setItem(i, 2, QTableWidgetItem(str(sent_date)))
            self.main_window.ui.qc_tabWid.setItem(i, 3, QTableWidgetItem(str(int_ver['status'])))
            self.main_window.ui.qc_tabWid.setItem(i, 4, QTableWidgetItem(str(verified_by)))
            self.main_window.ui.qc_tabWid.setItem(i, 5, QTableWidgetItem(str(verified_date)))
