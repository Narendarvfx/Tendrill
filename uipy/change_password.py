# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CP_MainWindow(object):
    def setupUi(self, CP_MainWindow):
        if not CP_MainWindow.objectName():
            CP_MainWindow.setObjectName(u"CP_MainWindow")
        CP_MainWindow.resize(500, 200)
        CP_MainWindow.setMaximumSize(QSize(500, 200))
        self.centralwidget = QWidget(CP_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.new_pwd1_le = QLineEdit(self.centralwidget)
        self.new_pwd1_le.setObjectName(u"new_pwd1_le")
        font1 = QFont()
        font1.setPointSize(12)
        self.new_pwd1_le.setFont(font1)
        self.new_pwd1_le.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.new_pwd1_le, 2, 0, 1, 1)

        self.old_pwd_le = QLineEdit(self.centralwidget)
        self.old_pwd_le.setObjectName(u"old_pwd_le")
        self.old_pwd_le.setFont(font1)
        self.old_pwd_le.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.old_pwd_le, 1, 0, 1, 1)

        self.cp_butt = QPushButton(self.centralwidget)
        self.cp_butt.setObjectName(u"cp_butt")
        font2 = QFont()
        font2.setPointSize(10)
        self.cp_butt.setFont(font2)

        self.gridLayout.addWidget(self.cp_butt, 4, 0, 1, 1)

        self.new_pwd2_le = QLineEdit(self.centralwidget)
        self.new_pwd2_le.setObjectName(u"new_pwd2_le")
        self.new_pwd2_le.setFont(font1)
        self.new_pwd2_le.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.new_pwd2_le, 3, 0, 1, 1)

        CP_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CP_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        CP_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CP_MainWindow)

        QMetaObject.connectSlotsByName(CP_MainWindow)
    # setupUi

    def retranslateUi(self, CP_MainWindow):
        CP_MainWindow.setWindowTitle(QCoreApplication.translate("CP_MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("CP_MainWindow", u"Change Password Form", None))
        self.new_pwd1_le.setPlaceholderText(QCoreApplication.translate("CP_MainWindow", u"Enter New Password", None))
        self.old_pwd_le.setPlaceholderText(QCoreApplication.translate("CP_MainWindow", u"Old Password", None))
        self.cp_butt.setText(QCoreApplication.translate("CP_MainWindow", u"Change Password", None))
        self.new_pwd2_le.setPlaceholderText(QCoreApplication.translate("CP_MainWindow", u"Re Enter New Password", None))
    # retranslateUi

