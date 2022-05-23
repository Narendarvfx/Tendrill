# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CP_Dialog(object):
    def setupUi(self, CP_Dialog):
        if not CP_Dialog.objectName():
            CP_Dialog.setObjectName(u"CP_Dialog")
        CP_Dialog.setWindowModality(Qt.ApplicationModal)
        CP_Dialog.resize(530, 288)
        self.gridLayout = QGridLayout(CP_Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 1, 1, 1)

        self.old_pwd_le = QLineEdit(CP_Dialog)
        self.old_pwd_le.setObjectName(u"old_pwd_le")
        font = QFont()
        font.setPointSize(10)
        self.old_pwd_le.setFont(font)
        self.old_pwd_le.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.old_pwd_le, 1, 1, 1, 3)

        self.new_pwd1_le = QLineEdit(CP_Dialog)
        self.new_pwd1_le.setObjectName(u"new_pwd1_le")
        self.new_pwd1_le.setFont(font)
        self.new_pwd1_le.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.new_pwd1_le, 2, 1, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 3, 1, 1)

        self.cp_butt = QPushButton(CP_Dialog)
        self.cp_butt.setObjectName(u"cp_butt")
        self.cp_butt.setFont(font)

        self.gridLayout.addWidget(self.cp_butt, 5, 2, 1, 1)

        self.new_pwd1_le_2 = QLineEdit(CP_Dialog)
        self.new_pwd1_le_2.setObjectName(u"new_pwd1_le_2")
        self.new_pwd1_le_2.setFont(font)
        self.new_pwd1_le_2.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.new_pwd1_le_2, 3, 1, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 4, 1, 1)

        self.label = QLabel(CP_Dialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 2, 1, 1)


        self.retranslateUi(CP_Dialog)

        QMetaObject.connectSlotsByName(CP_Dialog)
    # setupUi

    def retranslateUi(self, CP_Dialog):
        CP_Dialog.setWindowTitle(QCoreApplication.translate("CP_Dialog", u"Dialog", None))
        self.old_pwd_le.setPlaceholderText(QCoreApplication.translate("CP_Dialog", u"Old Password", None))
        self.new_pwd1_le.setPlaceholderText(QCoreApplication.translate("CP_Dialog", u"Enter New Password", None))
        self.cp_butt.setText(QCoreApplication.translate("CP_Dialog", u"Change Password", None))
        self.new_pwd1_le_2.setPlaceholderText(QCoreApplication.translate("CP_Dialog", u"Re Enter New Password", None))
        self.label.setText(QCoreApplication.translate("CP_Dialog", u"Change Password Form", None))
    # retranslateUi

