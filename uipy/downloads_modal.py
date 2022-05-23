# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downloads_modal.ui'
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


class Ui_Downloads_Dialog(object):
    def setupUi(self, Downloads_Dialog):
        if not Downloads_Dialog.objectName():
            Downloads_Dialog.setObjectName(u"Downloads_Dialog")
        Downloads_Dialog.resize(754, 390)
        Downloads_Dialog.setStyleSheet(u"QDialog{\n"
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
        self.gridLayout_3 = QGridLayout(Downloads_Dialog)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Downloads_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.sel_path_btn = QPushButton(self.frame_2)
        self.sel_path_btn.setObjectName(u"sel_path_btn")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        self.sel_path_btn.setFont(font)
        self.sel_path_btn.setStyleSheet(u"padding:5px")

        self.gridLayout.addWidget(self.sel_path_btn, 0, 0, 1, 1)

        self.cancel_btn = QPushButton(self.frame_2)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet(u"padding:5px")

        self.gridLayout.addWidget(self.cancel_btn, 0, 2, 1, 1)

        self.start_btn = QPushButton(self.frame_2)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet(u"padding:5px")

        self.gridLayout.addWidget(self.start_btn, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(7)
        self.gridLayout_4.setContentsMargins(5, 0, 5, 5)
        self.sel_path_text_label = QLabel(self.frame_3)
        self.sel_path_text_label.setObjectName(u"sel_path_text_label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.sel_path_text_label.setFont(font1)
        self.sel_path_text_label.setStyleSheet(u"")
        self.sel_path_text_label.setWordWrap(True)

        self.gridLayout_4.addWidget(self.sel_path_text_label, 0, 1, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.shots_list_widget = QListWidget(self.frame)
        self.shots_list_widget.setObjectName(u"shots_list_widget")
        self.shots_list_widget.setStyleSheet(u"QListWidget{\n"
"background-color: rgb(48, 52, 63);\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.shots_list_widget, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Downloads_Dialog)

        QMetaObject.connectSlotsByName(Downloads_Dialog)
    # setupUi

    def retranslateUi(self, Downloads_Dialog):
        Downloads_Dialog.setWindowTitle(QCoreApplication.translate("Downloads_Dialog", u"Dialog", None))
        self.sel_path_btn.setText(QCoreApplication.translate("Downloads_Dialog", u"Select Folder", None))
        self.cancel_btn.setText(QCoreApplication.translate("Downloads_Dialog", u"Cancel", None))
        self.start_btn.setText(QCoreApplication.translate("Downloads_Dialog", u"Download", None))
        self.sel_path_text_label.setText("")
        self.label.setText(QCoreApplication.translate("Downloads_Dialog", u"Destination:", None))
    # retranslateUi

