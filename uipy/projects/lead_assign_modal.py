# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lead_assign_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Lead_Assign_Dialog(object):
    def setupUi(self, Lead_Assign_Dialog):
        if not Lead_Assign_Dialog.objectName():
            Lead_Assign_Dialog.setObjectName(u"Lead_Assign_Dialog")
        Lead_Assign_Dialog.resize(400, 151)
        Lead_Assign_Dialog.setStyleSheet(u"background:transparent")
        self.gridLayout = QGridLayout(Lead_Assign_Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Lead_Assign_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(40, 44, 52);\n"
"border:2px solid rgba(255, 170, 0, 0.5);\n"
"border-radius:10px\n"
"}\n"
"QLabel{\n"
"color: rgb(212, 212, 212);\n"
"border:none\n"
"}\n"
"QPushButton{\n"
"	color: rgb(216, 216, 216);\n"
"background-color: rgb(58, 64, 76);\n"
"border:1px solid  rgb(97, 97, 97);\n"
"border-radius:3px;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"padding-top:5px;\n"
"padding-bottom:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(62, 68, 81);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(52, 57, 68);\n"
"}\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color: rgb(212, 212, 212);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left"
                        "-color: rgba(39, 44, 54, 150);\n"
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
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setVerticalSpacing(17)
        self.gridLayout_2.setContentsMargins(11, 7, 11, 7)
        self.lead_cancel_btn = QPushButton(self.frame)
        self.lead_cancel_btn.setObjectName(u"lead_cancel_btn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lead_cancel_btn.setFont(font)

        self.gridLayout_2.addWidget(self.lead_cancel_btn, 2, 2, 1, 1)

        self.lead_assign_btn = QPushButton(self.frame)
        self.lead_assign_btn.setObjectName(u"lead_assign_btn")
        self.lead_assign_btn.setFont(font)

        self.gridLayout_2.addWidget(self.lead_assign_btn, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.sel_lead_cb = QComboBox(self.frame)
        self.sel_lead_cb.addItem("")
        self.sel_lead_cb.setObjectName(u"sel_lead_cb")
        font1 = QFont()
        font1.setPointSize(10)
        self.sel_lead_cb.setFont(font1)
        self.sel_lead_cb.setStyleSheet(u"border:none")

        self.gridLayout_2.addWidget(self.sel_lead_cb, 1, 0, 1, 3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Lead_Assign_Dialog)

        QMetaObject.connectSlotsByName(Lead_Assign_Dialog)
    # setupUi

    def retranslateUi(self, Lead_Assign_Dialog):
        Lead_Assign_Dialog.setWindowTitle(QCoreApplication.translate("Lead_Assign_Dialog", u"Dialog", None))
        self.lead_cancel_btn.setText(QCoreApplication.translate("Lead_Assign_Dialog", u"Cancel", None))
        self.lead_assign_btn.setText(QCoreApplication.translate("Lead_Assign_Dialog", u"Assign", None))
        self.sel_lead_cb.setItemText(0, QCoreApplication.translate("Lead_Assign_Dialog", u"Select Lead", None))

        self.label.setText(QCoreApplication.translate("Lead_Assign_Dialog", u"Lead Assignments", None))
    # retranslateUi

