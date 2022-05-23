# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_client_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Cli_Dialog(object):
    def setupUi(self, Cli_Dialog):
        if not Cli_Dialog.objectName():
            Cli_Dialog.setObjectName(u"Cli_Dialog")
        Cli_Dialog.setWindowModality(Qt.ApplicationModal)
        Cli_Dialog.resize(571, 362)
        Cli_Dialog.setStyleSheet(u"QDialog{\n"
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
        Cli_Dialog.setModal(True)
        self.gridLayout_3 = QGridLayout(Cli_Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(Cli_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 0, 10, 0)
        self.cli_name_text = QLineEdit(self.frame)
        self.cli_name_text.setObjectName(u"cli_name_text")
        font1 = QFont()
        font1.setPointSize(12)
        self.cli_name_text.setFont(font1)
        self.cli_name_text.setStyleSheet(u"padding:5px;")

        self.gridLayout_2.addWidget(self.cli_name_text, 1, 0, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(13)
        self.label_2.setFont(font2)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.cli_country_text = QLineEdit(self.frame)
        self.cli_country_text.setObjectName(u"cli_country_text")
        self.cli_country_text.setFont(font1)
        self.cli_country_text.setStyleSheet(u"padding:5px;")

        self.gridLayout_2.addWidget(self.cli_country_text, 3, 0, 1, 2)

        self.cli_locality_cb = QComboBox(self.frame)
        self.cli_locality_cb.setObjectName(u"cli_locality_cb")
        self.cli_locality_cb.setFont(font1)
        self.cli_locality_cb.setStyleSheet(u"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(44, 49, 60);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.gridLayout_2.addWidget(self.cli_locality_cb, 6, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.frame_2 = QFrame(Cli_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cli_save_btn = QPushButton(self.frame_2)
        self.cli_save_btn.setObjectName(u"cli_save_btn")
        self.cli_save_btn.setMinimumSize(QSize(120, 30))
        font3 = QFont()
        font3.setPointSize(9)
        self.cli_save_btn.setFont(font3)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cli_save_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.cli_save_btn)

        self.cli_cancel_btn = QPushButton(self.frame_2)
        self.cli_cancel_btn.setObjectName(u"cli_cancel_btn")
        self.cli_cancel_btn.setMinimumSize(QSize(120, 30))
        self.cli_cancel_btn.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cli_cancel_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.cli_cancel_btn)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)


        self.retranslateUi(Cli_Dialog)

        QMetaObject.connectSlotsByName(Cli_Dialog)
    # setupUi

    def retranslateUi(self, Cli_Dialog):
        Cli_Dialog.setWindowTitle(QCoreApplication.translate("Cli_Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Cli_Dialog", u"Add Client", None))
        self.cli_name_text.setPlaceholderText(QCoreApplication.translate("Cli_Dialog", u"Enter Client Name...", None))
        self.label_2.setText(QCoreApplication.translate("Cli_Dialog", u"Country:", None))
        self.label.setText(QCoreApplication.translate("Cli_Dialog", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("Cli_Dialog", u"Locality:", None))
        self.cli_country_text.setPlaceholderText(QCoreApplication.translate("Cli_Dialog", u"Enter Country Name...", None))
        self.cli_locality_cb.setPlaceholderText(QCoreApplication.translate("Cli_Dialog", u"Select", None))
        self.cli_save_btn.setText(QCoreApplication.translate("Cli_Dialog", u"Save", None))
        self.cli_cancel_btn.setText(QCoreApplication.translate("Cli_Dialog", u"Cancel", None))
    # retranslateUi

