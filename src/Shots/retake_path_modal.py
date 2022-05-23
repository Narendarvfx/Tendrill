import datetime
import json
import os

from PySide2 import QtCore, QtGui, QtWebSockets
from PySide2.QtCore import QEasingCurve, QPoint, QAbstractAnimation, QCoreApplication, QUrl, QThreadPool, QTimer, \
    QPropertyAnimation
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QDialog, QGridLayout, QMessageBox, QTableWidgetItem, QGraphicsOpacityEffect

import api
from src.Shots.Worker_Class import Worker
from uipy.projects.assign_modal import Ui_Assign_Dialog
import win32security
import ntsecuritycon as con

from uipy.projects.edit_shot_modal import Ui_Shots_Edit_Dialog
from uipy.projects.retake_path_modal import Ui_Retake_Path_Dialog


class RetakePathModal(QDialog):
    def __init__(self,instance, *args, **kwargs):
        super(RetakePathModal, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Retake_Path_Dialog()
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
        self.ui.save_btn.clicked.connect(self.save_shot)

    def get_retake_path(self):
        retake_path = self.ui.retake_path_textEdit.toPlainText()
        return retake_path

    def save_shot(self):
        self.accept()
