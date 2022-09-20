# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assign_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Assign_Dialog(object):
    def setupUi(self, Assign_Dialog):
        if not Assign_Dialog.objectName():
            Assign_Dialog.setObjectName(u"Assign_Dialog")
        Assign_Dialog.resize(431, 313)
        Assign_Dialog.setMinimumSize(QSize(431, 220))
        Assign_Dialog.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(Assign_Dialog)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.frame = QFrame(Assign_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 3, 0, 2, 1)

        self.avl_md_lb = QLabel(self.frame)
        self.avl_md_lb.setObjectName(u"avl_md_lb")
        font1 = QFont()
        font1.setFamily(u"HARU BIRU 2")
        font1.setPointSize(48)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.avl_md_lb.setFont(font1)
        self.avl_md_lb.setStyleSheet(u"padding-top:5px;\n"
"padding-bottom:5px;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-radius:35px;\n"
"background-color:rgb(85, 170, 255);\n"
"font: 48pt \"HARU BIRU 2\";")
        self.avl_md_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.avl_md_lb, 3, 3, 5, 2)

        self.sel_Compiler_chckBox = QCheckBox(self.frame)
        self.sel_Compiler_chckBox.setObjectName(u"sel_Compiler_chckBox")
        self.sel_Compiler_chckBox.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(10)
        self.sel_Compiler_chckBox.setFont(font2)
        self.sel_Compiler_chckBox.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sel_Compiler_chckBox, 11, 1, 1, 2)

        self.assign_pb = QPushButton(self.frame)
        self.assign_pb.setObjectName(u"assign_pb")
        self.assign_pb.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.assign_pb.setFont(font3)
        self.assign_pb.setStyleSheet(u"background-color: rgb(85, 170, 0);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.assign_pb, 12, 3, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.shot_md_le = QLineEdit(self.frame)
        self.shot_md_le.setObjectName(u"shot_md_le")
        font4 = QFont()
        font4.setPointSize(10)
        self.shot_md_le.setFont(font4)

        self.gridLayout.addWidget(self.shot_md_le, 3, 1, 2, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)

        self.start_date = QDateEdit(self.frame)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setFont(font4)

        self.gridLayout.addWidget(self.start_date, 5, 1, 1, 1)

        self.sel_artists_cb = QComboBox(self.frame)
        self.sel_artists_cb.addItem("")
        self.sel_artists_cb.setObjectName(u"sel_artists_cb")
        font5 = QFont()
        font5.setPointSize(9)
        self.sel_artists_cb.setFont(font5)

        self.gridLayout.addWidget(self.sel_artists_cb, 1, 1, 2, 4)

        self.eta_date = QDateEdit(self.frame)
        self.eta_date.setObjectName(u"eta_date")
        self.eta_date.setFont(font4)

        self.gridLayout.addWidget(self.eta_date, 7, 1, 1, 1)

        self.shot_detail_lb = QLabel(self.frame)
        self.shot_detail_lb.setObjectName(u"shot_detail_lb")
        font6 = QFont()
        font6.setFamily(u"Arial Black")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(10)
        self.shot_detail_lb.setFont(font6)
        self.shot_detail_lb.setStyleSheet(u"font: 87 14pt \"Arial Black\";")
        self.shot_detail_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.shot_detail_lb, 0, 0, 1, 5)

        self.cancel_pb = QPushButton(self.frame)
        self.cancel_pb.setObjectName(u"cancel_pb")
        self.cancel_pb.setMinimumSize(QSize(0, 30))
        self.cancel_pb.setFont(font3)
        self.cancel_pb.setStyleSheet(u"background-color: rgb(255, 85, 0);")

        self.gridLayout.addWidget(self.cancel_pb, 12, 4, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 75 9pt \"Arial\";")

        self.gridLayout.addWidget(self.label, 9, 3, 1, 2)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Assign_Dialog)

        QMetaObject.connectSlotsByName(Assign_Dialog)
    # setupUi

    def retranslateUi(self, Assign_Dialog):
        Assign_Dialog.setWindowTitle(QCoreApplication.translate("Assign_Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Assign_Dialog", u"Artist :", None))
        self.label_3.setText(QCoreApplication.translate("Assign_Dialog", u"Bid Days :", None))
        self.avl_md_lb.setText(QCoreApplication.translate("Assign_Dialog", u"10", None))
        self.sel_Compiler_chckBox.setText("")
        self.assign_pb.setText(QCoreApplication.translate("Assign_Dialog", u"Assign", None))
        self.label_4.setText(QCoreApplication.translate("Assign_Dialog", u"Eta :", None))
        self.shot_md_le.setText("")
        self.shot_md_le.setPlaceholderText(QCoreApplication.translate("Assign_Dialog", u"Enter Bid days", None))
        self.label_5.setText(QCoreApplication.translate("Assign_Dialog", u"Start date:", None))
        self.label_7.setText(QCoreApplication.translate("Assign_Dialog", u"Compiler", None))
        self.sel_artists_cb.setItemText(0, QCoreApplication.translate("Assign_Dialog", u"Select Artist", None))

        self.shot_detail_lb.setText(QCoreApplication.translate("Assign_Dialog", u"Shot Name", None))
        self.cancel_pb.setText(QCoreApplication.translate("Assign_Dialog", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Assign_Dialog", u"      Total Available bid days", None))
    # retranslateUi

