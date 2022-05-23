# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_status_change.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import files_rc

class Ui_Client_Status_Dialog(object):
    def setupUi(self, Client_Status_Dialog):
        if not Client_Status_Dialog.objectName():
            Client_Status_Dialog.setObjectName(u"Client_Status_Dialog")
        Client_Status_Dialog.resize(400, 159)
        Client_Status_Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(27, 29, 35);\n"
"border:1px solid rgba(255, 170, 0,0.5);\n"
"border-radius:5px}\n"
"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(44, 49, 60);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(Client_Status_Dialog)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(Client_Status_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 5, 0, 5)
        self.sel_file_lbl = QLabel(self.frame)
        self.sel_file_lbl.setObjectName(u"sel_file_lbl")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        self.sel_file_lbl.setFont(font)
        self.sel_file_lbl.setStyleSheet(u"color:white")

        self.gridLayout.addWidget(self.sel_file_lbl, 1, 0, 1, 4)

        self.export_btn = QPushButton(self.frame)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setMinimumSize(QSize(120, 30))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.export_btn.setFont(font1)
        self.export_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 85, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(100, 100, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(70, 70, 104);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/24x24/icons/24x24/cil-description.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_btn.setIcon(icon)

        self.gridLayout.addWidget(self.export_btn, 0, 0, 1, 1)

        self.import_btn = QPushButton(self.frame)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setMinimumSize(QSize(120, 30))
        self.import_btn.setFont(font1)
        self.import_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 127);\n"
"	color:white\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 190, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(209, 139, 104);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/24x24/icons/24x24/cil-vertical-align-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.import_btn, 0, 1, 1, 2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cancel_btn = QPushButton(self.frame_2)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(80, 30))
        font2 = QFont()
        font2.setPointSize(9)
        self.cancel_btn.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_btn.setIcon(icon2)

        self.gridLayout_3.addWidget(self.cancel_btn, 0, 3, 1, 1)

        self.save_btn = QPushButton(self.frame_2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(80, 30))
        self.save_btn.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon3)

        self.gridLayout_3.addWidget(self.save_btn, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Client_Status_Dialog)

        QMetaObject.connectSlotsByName(Client_Status_Dialog)
    # setupUi

    def retranslateUi(self, Client_Status_Dialog):
        Client_Status_Dialog.setWindowTitle(QCoreApplication.translate("Client_Status_Dialog", u"Dialog", None))
        self.sel_file_lbl.setText("")
        self.export_btn.setText(QCoreApplication.translate("Client_Status_Dialog", u"EXPORT", None))
        self.import_btn.setText(QCoreApplication.translate("Client_Status_Dialog", u"IMPORT", None))
        self.cancel_btn.setText(QCoreApplication.translate("Client_Status_Dialog", u"Cancel", None))
        self.save_btn.setText(QCoreApplication.translate("Client_Status_Dialog", u"Save", None))
    # retranslateUi

