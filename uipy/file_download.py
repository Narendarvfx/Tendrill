# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_download.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FileDownload_Dialog(object):
    def setupUi(self, FileDownload_Dialog):
        if not FileDownload_Dialog.objectName():
            FileDownload_Dialog.setObjectName(u"FileDownload_Dialog")
        FileDownload_Dialog.resize(596, 271)
        FileDownload_Dialog.setStyleSheet(u"QDialog{background-color: rgb(63, 188, 0);}")
        self.buttonBox = QDialogButtonBox(FileDownload_Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(200, 200, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(FileDownload_Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 571, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.report_path = QLabel(FileDownload_Dialog)
        self.report_path.setObjectName(u"report_path")
        self.report_path.setGeometry(QRect(30, 90, 401, 81))
        self.open_file_btn = QPushButton(FileDownload_Dialog)
        self.open_file_btn.setObjectName(u"open_file_btn")
        self.open_file_btn.setGeometry(QRect(240, 200, 93, 28))

        self.retranslateUi(FileDownload_Dialog)
        self.buttonBox.accepted.connect(FileDownload_Dialog.accept)
        self.buttonBox.rejected.connect(FileDownload_Dialog.reject)

        QMetaObject.connectSlotsByName(FileDownload_Dialog)
    # setupUi

    def retranslateUi(self, FileDownload_Dialog):
        FileDownload_Dialog.setWindowTitle(QCoreApplication.translate("FileDownload_Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("FileDownload_Dialog", u"Report Downloaded Successfully", None))
        self.report_path.setText("")
        self.open_file_btn.setText(QCoreApplication.translate("FileDownload_Dialog", u"Open File", None))
    # retranslateUi

