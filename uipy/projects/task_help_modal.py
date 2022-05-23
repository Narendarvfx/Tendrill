# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_help_modalPeXhiP.ui'
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

class Ui_TaskHelp_Dialog(object):
    def setupUi(self, TaskHelp_Dialog):
        if not TaskHelp_Dialog.objectName():
            TaskHelp_Dialog.setObjectName(u"TaskHelp_Dialog")
        TaskHelp_Dialog.resize(522, 257)
        TaskHelp_Dialog.setMinimumSize(QSize(431, 220))
        TaskHelp_Dialog.setStyleSheet(u"QDialog{\n"
"background-color: rgb(40, 44, 52);\n"
"border:2px solid rgba(255, 170, 0, 0.5);\n"
"border-radius:10px\n"
"}\n"
"/* TIME EDIT */\n"
"QTimeEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QTimeEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTimeEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"/* DATE EDIT */\n"
"QDateEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QDateEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDateEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px soli"
                        "d rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add"
                        "-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none"
                        ";\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgba(255, 143, 5, 0.5);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgba(255, 143, 5, 0.5);\n"
"	border: 3px solid rgba(255, 143, 5, 0.5);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, "
                        "59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
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
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px"
                        ";\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
""
                        "QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
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
"\n"
"")
        self.gridLayout_2 = QGridLayout(TaskHelp_Dialog)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.frame = QFrame(TaskHelp_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(212, 212, 212);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.shot_md_le = QLineEdit(self.frame)
        self.shot_md_le.setObjectName(u"shot_md_le")
        font = QFont()
        font.setPointSize(10)
        self.shot_md_le.setFont(font)

        self.gridLayout.addWidget(self.shot_md_le, 4, 1, 2, 2)

        self.cancel_pb = QPushButton(self.frame)
        self.cancel_pb.setObjectName(u"cancel_pb")
        self.cancel_pb.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.cancel_pb.setFont(font1)

        self.gridLayout.addWidget(self.cancel_pb, 7, 4, 1, 1)

        self.request_pb = QPushButton(self.frame)
        self.request_pb.setObjectName(u"request_pb")
        self.request_pb.setMinimumSize(QSize(0, 30))
        self.request_pb.setFont(font1)

        self.gridLayout.addWidget(self.request_pb, 7, 3, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 4, 3, 2, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 4, 0, 2, 1)

        self.eta_time = QTimeEdit(self.frame)
        self.eta_time.setObjectName(u"eta_time")
        self.eta_time.setFont(font)

        self.gridLayout.addWidget(self.eta_time, 6, 3, 1, 2)

        self.shot_detail_lb = QLabel(self.frame)
        self.shot_detail_lb.setObjectName(u"shot_detail_lb")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.shot_detail_lb.setFont(font3)
        self.shot_detail_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.shot_detail_lb, 0, 0, 1, 5)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 2, 0, 2, 1)

        self.sel_type_cb = QComboBox(self.frame)
        self.sel_type_cb.addItem("")
        self.sel_type_cb.addItem("")
        self.sel_type_cb.addItem("")
        self.sel_type_cb.addItem("")
        self.sel_type_cb.setObjectName(u"sel_type_cb")
        font4 = QFont()
        font4.setPointSize(9)
        self.sel_type_cb.setFont(font4)

        self.gridLayout.addWidget(self.sel_type_cb, 2, 1, 2, 4)

        self.avl_md_lb = QLabel(self.frame)
        self.avl_md_lb.setObjectName(u"avl_md_lb")
        font5 = QFont()
        font5.setFamily(u"Terminal")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.avl_md_lb.setFont(font5)
        self.avl_md_lb.setStyleSheet(u"padding-top:5px;\n"
"padding-bottom:5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid white;\n"
"border-radius:5px;\n"
"background-color: rgb(207, 121, 0);")
        self.avl_md_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.avl_md_lb, 4, 4, 2, 1)

        self.eta_date = QDateEdit(self.frame)
        self.eta_date.setObjectName(u"eta_date")
        self.eta_date.setFont(font)

        self.gridLayout.addWidget(self.eta_date, 6, 1, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)


        self.retranslateUi(TaskHelp_Dialog)

        QMetaObject.connectSlotsByName(TaskHelp_Dialog)
    # setupUi

    def retranslateUi(self, TaskHelp_Dialog):
        TaskHelp_Dialog.setWindowTitle(QCoreApplication.translate("TaskHelp_Dialog", u"Dialog", None))
        self.shot_md_le.setText("")
        self.shot_md_le.setPlaceholderText(QCoreApplication.translate("TaskHelp_Dialog", u"Enter Bid days", None))
        self.cancel_pb.setText(QCoreApplication.translate("TaskHelp_Dialog", u"Cancel", None))
        self.request_pb.setText(QCoreApplication.translate("TaskHelp_Dialog", u"Request", None))
        self.label_6.setText(QCoreApplication.translate("TaskHelp_Dialog", u"Avail:", None))
        self.label_3.setText(QCoreApplication.translate("TaskHelp_Dialog", u"Bid Days :", None))
        self.shot_detail_lb.setText(QCoreApplication.translate("TaskHelp_Dialog", u"Shot Name", None))
        self.label_2.setText(QCoreApplication.translate("TaskHelp_Dialog", u"Task Type:", None))
        self.sel_type_cb.setItemText(0, QCoreApplication.translate("TaskHelp_Dialog", u"Select Type", None))
        self.sel_type_cb.setItemText(1, QCoreApplication.translate("TaskHelp_Dialog", u"PAINT", None))
        self.sel_type_cb.setItemText(2, QCoreApplication.translate("TaskHelp_Dialog", u"ROTO", None))
        self.sel_type_cb.setItemText(3, QCoreApplication.translate("TaskHelp_Dialog", u"MM", None))

        self.avl_md_lb.setText(QCoreApplication.translate("TaskHelp_Dialog", u"10", None))
        self.label_4.setText(QCoreApplication.translate("TaskHelp_Dialog", u"Eta :", None))
    # retranslateUi

