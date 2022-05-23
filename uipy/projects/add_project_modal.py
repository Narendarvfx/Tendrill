# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_project_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Pro_Dialog(object):
    def setupUi(self, Pro_Dialog):
        if not Pro_Dialog.objectName():
            Pro_Dialog.setObjectName(u"Pro_Dialog")
        Pro_Dialog.setWindowModality(Qt.ApplicationModal)
        Pro_Dialog.resize(359, 260)
        Pro_Dialog.setStyleSheet(u"QDialog{\n"
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
        Pro_Dialog.setModal(True)
        self.gridLayout_3 = QGridLayout(Pro_Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(Pro_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color: rgb(255, 170, 0);")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(193, 193, 193);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cli_name_label = QLabel(self.frame)
        self.cli_name_label.setObjectName(u"cli_name_label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.cli_name_label.setFont(font1)
        self.cli_name_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.cli_name_label, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(13)
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.pro_name_text = QLineEdit(self.frame)
        self.pro_name_text.setObjectName(u"pro_name_text")
        font3 = QFont()
        font3.setPointSize(12)
        self.pro_name_text.setFont(font3)
        self.pro_name_text.setStyleSheet(u"padding:5px;")

        self.gridLayout_2.addWidget(self.pro_name_text, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 4, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.frame_2 = QFrame(Pro_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pro_save_btn = QPushButton(self.frame_2)
        self.pro_save_btn.setObjectName(u"pro_save_btn")
        self.pro_save_btn.setMinimumSize(QSize(120, 30))
        font4 = QFont()
        font4.setPointSize(9)
        self.pro_save_btn.setFont(font4)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pro_save_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.pro_save_btn)

        self.pro_cancel_btn = QPushButton(self.frame_2)
        self.pro_cancel_btn.setObjectName(u"pro_cancel_btn")
        self.pro_cancel_btn.setMinimumSize(QSize(120, 30))
        self.pro_cancel_btn.setFont(font4)
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pro_cancel_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pro_cancel_btn)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)


        self.retranslateUi(Pro_Dialog)

        QMetaObject.connectSlotsByName(Pro_Dialog)
    # setupUi

    def retranslateUi(self, Pro_Dialog):
        Pro_Dialog.setWindowTitle(QCoreApplication.translate("Pro_Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Pro_Dialog", u"Add Project", None))
        self.cli_name_label.setText(QCoreApplication.translate("Pro_Dialog", u"clientName", None))
        self.label.setText(QCoreApplication.translate("Pro_Dialog", u"Name", None))
        self.pro_name_text.setPlaceholderText(QCoreApplication.translate("Pro_Dialog", u"Enter Project Name..", None))
        self.pro_save_btn.setText(QCoreApplication.translate("Pro_Dialog", u"Save", None))
        self.pro_cancel_btn.setText(QCoreApplication.translate("Pro_Dialog", u"Cancel", None))
    # retranslateUi

