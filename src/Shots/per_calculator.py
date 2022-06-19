import datetime

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QMessageBox

import api

def update_shot_per(self, shot, e_per):
    achieved_mandays = shot['bid_days'] / 100 * e_per
    pending_mandays = shot['bid_days'] - achieved_mandays
    data = {
        'progress': e_per,
        'achieved_mandays': achieved_mandays,
        'pending_mandays': pending_mandays
    }
    res = api.update_ShotStatus(shot['id'], data)
    if res.status_code == 201:
        self.progress = e_per
        self.timer = QTimer()
        self.timer.timeout.connect(self.progressBarAnimated)
        self.timer.start()

def create_log(self, shot, e_per, employee):
    day_per = e_per - shot['progress']
    cons_mandays = shot['bid_days'] / 100 * day_per
    data = {
        'shot': shot['id'],
        'percentage': e_per,
        'day_percentage': day_per,
        'consumed_man_day': round(cons_mandays, 2),
        'artist': employee['id'],
        'updated_by': employee['id'],
    }

    res = api.post_day_logs(data)
    if res.status_code == 201:
        update_shot_per(self, shot, e_per)


def update_log(self, shot,logid, e_per, employee):
    day_per = e_per - shot['progress']
    cons_mandays = shot['bid_days'] / 100 * day_per
    data = {
        'percentage': e_per,
        'day_percentage': day_per,
        'consumed_man_day': round(cons_mandays, 2),
    }
    res = api.update_day_logs(data, logid)
    if res.status_code == 201:
        update_shot_per(self, shot, e_per)

def error_msg():
    msg = QMessageBox()
    msg.setText("Current Percentage should not be less than the previous day's percentage")
    msg.setWindowTitle("Error")
    msg.setIcon(QMessageBox.Critical)
    # msg.setStyleSheet("background-color: rgb(202,0,3,);color:'white'")
    msg.exec_()

def get_previous_logs(self, shot, e_per, employee):
    previous_logs = api.last_day_log(shot['id'])
    todate = str(datetime.datetime.now().date())
    if len(previous_logs) == 2:
        ud = datetime.datetime.strptime(previous_logs[0]['updated_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime(
            "%Y-%m-%d")
        if ud == todate:
            per = previous_logs[1]['percentage']
            if float(e_per) > per:
                update_log(self,shot, previous_logs[0]['id'], e_per, employee)
            else:
                error_msg()
        else:
            per = previous_logs[0]['percentage']
            if float(e_per) > per:
                create_log(self,shot, e_per, employee)
            else:
                error_msg()
    elif len(previous_logs) == 1:
        ud = datetime.datetime.strptime(previous_logs[0]['updated_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y-%m-%d")
        if ud == todate:
            update_log(self,shot, previous_logs[0]['id'], e_per, employee)
        else:
            per = previous_logs[0]['percentage']
            if float(e_per) > per:
                create_log(self,shot, e_per, employee)
            else:
                error_msg()
    else:
        create_log(self, shot, e_per, employee)
