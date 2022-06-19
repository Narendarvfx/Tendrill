from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsDropShadowEffect, QMessageBox

import api
import pandas as pd

from src.reports.studio_report_download import generate_report


class Studio_Reports(object):
    def __init__(self, obj):
        super(Studio_Reports, self).__init__()
        self.main_window = obj
        self.get_data()
        self.main_window.ui.sr_download_btn.clicked.connect(lambda: self.download_report())

    def get_data(self):
        client_data = api.get_all_clients()
        # print(len(data))
        self.main_window.ui.sr_clients_lbl.setText(str(len(client_data)))
        project_data = api.get_all_projects()
        self.main_window.ui.sr_shows_lbl.setText(str(len(project_data)))
        shots_data = api.get_all_shots()
        self.main_window.ui.sr_shots_lbl.setText(str(len(shots_data)))
        # print(shots_data)
        act_mandays = sum(item['bid_days'] for item in shots_data)
        self.main_window.ui.sr_actmandays_lbl.setText(str(round(act_mandays,2)))
        achived_mandays = sum(item['achieved_mandays'] for item in shots_data)
        self.main_window.ui.sr_ach_mandays_lbl.setText(str(round(achived_mandays,2)))
        pending_mandays = act_mandays - achived_mandays
        self.main_window.ui.sr_delta_lbl.setText(str(round(pending_mandays,2)))

        yts_status = 'YTA|YTS|ATL'
        yts = api.allShotsData(yts_status)
        self.main_window.ui.sr_yts_lbl.setText(str(len(yts)))

        wip_status = 'WIP|STQ|IRT'
        wip = api.allShotsData(wip_status)
        self.main_window.ui.sr_wip_lbl.setText(str(len(wip)))

        cap_status = 'CAP'
        cap = api.allShotsData(cap_status)
        self.main_window.ui.sr_cmp_lbl.setText(str(len(cap)))

    def download_report(self):
        try:
            g = generate_report()
            self.download_success_dialog(g)
        except Exception as e:
            print(e)

    def download_success_dialog(self, fpath):
        msg = QMessageBox()
        msg.setText(
            "Report Downloaded Successfully in following path\n\n " + fpath + "\n\n\n Tip: select and copy the path and open in file browser")
        msg.setWindowTitle("Success")
        msg.setIcon(QMessageBox.Information)
        # msg.setStyleSheet("background-color: rgb(33,193,100);color:'white'")
        msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
        msg.exec_()

