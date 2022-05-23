# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_shot_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Shots_Edit_Dialog(object):
    def setupUi(self, Shots_Edit_Dialog):
        if not Shots_Edit_Dialog.objectName():
            Shots_Edit_Dialog.setObjectName(u"Shots_Edit_Dialog")
        Shots_Edit_Dialog.setWindowModality(Qt.ApplicationModal)
        Shots_Edit_Dialog.resize(524, 315)
        Shots_Edit_Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(27, 29, 35);\n"
"border:1px solid rgba(255, 170, 0,0.5);\n"
"border-radius:5px}\n"
"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(44, 49, 60);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(193, 193, 193);\n"
"    padding:3px;\n"
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
"/* DATE EDIT */\n"
"QDateEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDateEdit:hove"
                        "r {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDateEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        Shots_Edit_Dialog.setModal(True)
        self.gridLayout_3 = QGridLayout(Shots_Edit_Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(Shots_Edit_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.update_btn = QPushButton(self.frame_2)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(9)
        self.update_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.update_btn)

        self.cancel_btn = QPushButton(self.frame_2)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(120, 30))
        self.cancel_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(Shots_Edit_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(193, 193, 193);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_in_le = QLineEdit(self.frame)
        self.frame_in_le.setObjectName(u"frame_in_le")
        font1 = QFont()
        font1.setPointSize(10)
        self.frame_in_le.setFont(font1)

        self.gridLayout.addWidget(self.frame_in_le, 3, 4, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(13)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)

        self.frame_out_le = QLineEdit(self.frame)
        self.frame_out_le.setObjectName(u"frame_out_le")
        self.frame_out_le.setFont(font1)

        self.gridLayout.addWidget(self.frame_out_le, 4, 4, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 3)

        self.shot_label = QLabel(self.frame)
        self.shot_label.setObjectName(u"shot_label")
        font3 = QFont()
        font3.setPointSize(11)
        self.shot_label.setFont(font3)
        self.shot_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.shot_label, 0, 0, 1, 5)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 4)

        self.bid_days_le = QLineEdit(self.frame)
        self.bid_days_le.setObjectName(u"bid_days_le")
        self.bid_days_le.setFont(font1)
        self.bid_days_le.setStyleSheet(u"")

        self.gridLayout.addWidget(self.bid_days_le, 2, 4, 1, 1)

        self.tyep_cb = QComboBox(self.frame)
        self.tyep_cb.addItem("")
        self.tyep_cb.addItem("")
        self.tyep_cb.addItem("")
        self.tyep_cb.setObjectName(u"tyep_cb")
        self.tyep_cb.setStyleSheet(u"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(193, 193, 193);\n"
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
"}\n"
"")

        self.gridLayout.addWidget(self.tyep_cb, 1, 4, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.eta_edit = QDateEdit(self.frame)
        self.eta_edit.setObjectName(u"eta_edit")
        self.eta_edit.setFont(font1)

        self.gridLayout.addWidget(self.eta_edit, 5, 4, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Shots_Edit_Dialog)

        QMetaObject.connectSlotsByName(Shots_Edit_Dialog)
    # setupUi

    def retranslateUi(self, Shots_Edit_Dialog):
        Shots_Edit_Dialog.setWindowTitle(QCoreApplication.translate("Shots_Edit_Dialog", u"Dialog", None))
        self.update_btn.setText(QCoreApplication.translate("Shots_Edit_Dialog", u"Update", None))
        self.cancel_btn.setText(QCoreApplication.translate("Shots_Edit_Dialog", u"Cancel", None))
        self.frame_in_le.setPlaceholderText(QCoreApplication.translate("Shots_Edit_Dialog", u"ENTER FRAME IN", None))
        self.label.setText(QCoreApplication.translate("Shots_Edit_Dialog", u"BID DAYS:", None))
        self.frame_out_le.setPlaceholderText(QCoreApplication.translate("Shots_Edit_Dialog", u"ENTER FRAME OUT", None))
        self.label_3.setText(QCoreApplication.translate("Shots_Edit_Dialog", u"FRAME IN :", None))
        self.shot_label.setText(QCoreApplication.translate("Shots_Edit_Dialog", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Shots_Edit_Dialog", u"FRAME OUT :", None))
        self.bid_days_le.setPlaceholderText(QCoreApplication.translate("Shots_Edit_Dialog", u"ENTER BIDS DAYS", None))
        self.tyep_cb.setItemText(0, QCoreApplication.translate("Shots_Edit_Dialog", u"NEW", None))
        self.tyep_cb.setItemText(1, QCoreApplication.translate("Shots_Edit_Dialog", u"RETAKE", None))
        self.tyep_cb.setItemText(2, QCoreApplication.translate("Shots_Edit_Dialog", u"ADDITIONAL", None))

        self.label_2.setText(QCoreApplication.translate("Shots_Edit_Dialog", u"TYPE :", None))
        self.label_5.setText(QCoreApplication.translate("Shots_Edit_Dialog", u"ETA :", None))
    # retranslateUi

