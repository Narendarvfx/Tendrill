# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output_path_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Output_Path_Dialog(object):
    def setupUi(self, Output_Path_Dialog):
        if not Output_Path_Dialog.objectName():
            Output_Path_Dialog.setObjectName(u"Output_Path_Dialog")
        Output_Path_Dialog.setWindowModality(Qt.ApplicationModal)
        Output_Path_Dialog.resize(524, 318)
        Output_Path_Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(27, 29, 35);\n"
"border:1px solid rgba(255, 170, 0,0.5);\n"
"border-radius:5px}\n"
"/* LINE EDIT */\n"
"QTextEdit {\n"
"	background-color: rgb(44, 49, 60);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(193, 193, 193);\n"
"    padding:3px;\n"
"	padding-left: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
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
        Output_Path_Dialog.setModal(True)
        self.gridLayout_3 = QGridLayout(Output_Path_Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(Output_Path_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(self.frame_2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(9)
        self.save_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.save_btn)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(Output_Path_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(193, 193, 193);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.title_label.setFont(font1)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 2)

        self.output_path_textEdit = QTextEdit(self.frame)
        self.output_path_textEdit.setObjectName(u"output_path_textEdit")
        self.output_path_textEdit.setFont(font1)

        self.gridLayout.addWidget(self.output_path_textEdit, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Output_Path_Dialog)

        QMetaObject.connectSlotsByName(Output_Path_Dialog)
    # setupUi

    def retranslateUi(self, Output_Path_Dialog):
        Output_Path_Dialog.setWindowTitle(QCoreApplication.translate("Output_Path_Dialog", u"Dialog", None))
        self.save_btn.setText(QCoreApplication.translate("Output_Path_Dialog", u"Save", None))
        self.title_label.setText(QCoreApplication.translate("Output_Path_Dialog", u"Enter Output Path:", None))
    # retranslateUi

