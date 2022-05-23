# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_percentage_modal.ui'
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

class Ui_Percentage_Dialog(object):
    def setupUi(self, Percentage_Dialog):
        if not Percentage_Dialog.objectName():
            Percentage_Dialog.setObjectName(u"Percentage_Dialog")
        Percentage_Dialog.setWindowModality(Qt.ApplicationModal)
        Percentage_Dialog.resize(359, 159)
        Percentage_Dialog.setStyleSheet(u"QDialog{\n"
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
        Percentage_Dialog.setModal(True)
        self.gridLayout_3 = QGridLayout(Percentage_Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(Percentage_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.per_save_btn = QPushButton(self.frame_2)
        self.per_save_btn.setObjectName(u"per_save_btn")
        self.per_save_btn.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(9)
        self.per_save_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.per_save_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.per_save_btn)

        self.per_cancel_btn = QPushButton(self.frame_2)
        self.per_cancel_btn.setObjectName(u"per_cancel_btn")
        self.per_cancel_btn.setMinimumSize(QSize(120, 30))
        self.per_cancel_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.per_cancel_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.per_cancel_btn)


        self.gridLayout_3.addWidget(self.frame_2, 3, 0, 1, 1)

        self.per_spin_box = QSpinBox(Percentage_Dialog)
        self.per_spin_box.setObjectName(u"per_spin_box")
        self.per_spin_box.setMinimumSize(QSize(0, 42))
        font1 = QFont()
        font1.setPointSize(22)
        self.per_spin_box.setFont(font1)
        self.per_spin_box.setStyleSheet(u"QSpinBox{\n"
"background-color: rgb(44, 49, 60);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.per_spin_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.per_spin_box.setMaximum(100)

        self.gridLayout_3.addWidget(self.per_spin_box, 1, 0, 1, 1)

        self.per_name_label = QLabel(Percentage_Dialog)
        self.per_name_label.setObjectName(u"per_name_label")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.per_name_label.setFont(font2)
        self.per_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.per_name_label, 0, 0, 1, 1)


        self.retranslateUi(Percentage_Dialog)

        QMetaObject.connectSlotsByName(Percentage_Dialog)
    # setupUi

    def retranslateUi(self, Percentage_Dialog):
        Percentage_Dialog.setWindowTitle(QCoreApplication.translate("Percentage_Dialog", u"Dialog", None))
        self.per_save_btn.setText(QCoreApplication.translate("Percentage_Dialog", u"Submit", None))
        self.per_cancel_btn.setText(QCoreApplication.translate("Percentage_Dialog", u"Cancel", None))
        self.per_name_label.setText(QCoreApplication.translate("Percentage_Dialog", u"Add <strong style=\"color:rgb(232, 147, 10)\">SHOT</strong> Percentage", None))
    # retranslateUi

