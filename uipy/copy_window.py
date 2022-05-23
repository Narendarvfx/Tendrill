# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'copy_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Copy_Dialog(object):
    def setupUi(self, Copy_Dialog):
        if not Copy_Dialog.objectName():
            Copy_Dialog.setObjectName(u"Copy_Dialog")
        Copy_Dialog.resize(761, 526)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Copy_Dialog.sizePolicy().hasHeightForWidth())
        Copy_Dialog.setSizePolicy(sizePolicy)
        Copy_Dialog.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:1px solid rgb(255, 170, 0, 0.5);\n"
"border-radius: 10px;\n"
"color: rgb(208, 208, 208);")
        self.gridLayout = QGridLayout(Copy_Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.label_2 = QLabel(Copy_Dialog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border:none;")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.frame_2 = QFrame(Copy_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.shot_details_textEdit = QTextEdit(self.frame_2)
        self.shot_details_textEdit.setObjectName(u"shot_details_textEdit")
        font1 = QFont()
        font1.setPointSize(10)
        self.shot_details_textEdit.setFont(font1)
        self.shot_details_textEdit.setStyleSheet(u"border:none;")

        self.verticalLayout_2.addWidget(self.shot_details_textEdit)


        self.gridLayout.addWidget(self.frame_2, 4, 0, 1, 2)

        self.copy_abort_btn = QDialogButtonBox(Copy_Dialog)
        self.copy_abort_btn.setObjectName(u"copy_abort_btn")
        self.copy_abort_btn.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"padding-top:5px;\n"
"padding-bottom:5px;\n"
"border-radius:3px;")
        self.copy_abort_btn.setOrientation(Qt.Horizontal)
        self.copy_abort_btn.setStandardButtons(QDialogButtonBox.Abort)

        self.gridLayout.addWidget(self.copy_abort_btn, 0, 1, 1, 1)

        self.label = QLabel(Copy_Dialog)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 170, 0, 0.5);\n"
"border:none")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.frame = QFrame(Copy_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius:10px;\n"
"border:none")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.shot_lbl = QLabel(self.frame)
        self.shot_lbl.setObjectName(u"shot_lbl")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setUnderline(True)
        font3.setWeight(75)
        self.shot_lbl.setFont(font3)
        self.shot_lbl.setStyleSheet(u"color: rgb(139, 139, 139);")
        self.shot_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.shot_lbl)

        self.lbl_src = QLabel(self.frame)
        self.lbl_src.setObjectName(u"lbl_src")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        self.lbl_src.setFont(font4)

        self.verticalLayout.addWidget(self.lbl_src)

        self.lbl_dest = QLabel(self.frame)
        self.lbl_dest.setObjectName(u"lbl_dest")
        self.lbl_dest.setFont(font4)

        self.verticalLayout.addWidget(self.lbl_dest)

        self.pb = QProgressBar(self.frame)
        self.pb.setObjectName(u"pb")
        font5 = QFont()
        font5.setPointSize(14)
        self.pb.setFont(font5)
        self.pb.setStyleSheet(u"QProgressBar\n"
"{\n"
"background-color:  rgba(255, 170, 0, 0.2);\n"
"border-radius: 15px;\n"
"color: rgb(195, 195, 195);\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(255, 170, 0, 0.5);\n"
"border-radius :15px;\n"
"}")
        self.pb.setValue(0)
        self.pb.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.pb)

        self.lbl_rate = QLabel(self.frame)
        self.lbl_rate.setObjectName(u"lbl_rate")
        self.lbl_rate.setFont(font4)

        self.verticalLayout.addWidget(self.lbl_rate)

        self.lbl_time_elapsed = QLabel(self.frame)
        self.lbl_time_elapsed.setObjectName(u"lbl_time_elapsed")
        self.lbl_time_elapsed.setFont(font4)

        self.verticalLayout.addWidget(self.lbl_time_elapsed)

        self.lbl_time_remaining = QLabel(self.frame)
        self.lbl_time_remaining.setObjectName(u"lbl_time_remaining")
        self.lbl_time_remaining.setFont(font4)

        self.verticalLayout.addWidget(self.lbl_time_remaining)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 2)


        self.retranslateUi(Copy_Dialog)
        self.copy_abort_btn.accepted.connect(Copy_Dialog.accept)
        self.copy_abort_btn.rejected.connect(Copy_Dialog.reject)

        QMetaObject.connectSlotsByName(Copy_Dialog)
    # setupUi

    def retranslateUi(self, Copy_Dialog):
        Copy_Dialog.setWindowTitle(QCoreApplication.translate("Copy_Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Copy_Dialog", u"Details:", None))
        self.shot_details_textEdit.setHtml(QCoreApplication.translate("Copy_Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Copy_Dialog", u"  Uploading to File Server.... ", None))
        self.shot_lbl.setText(QCoreApplication.translate("Copy_Dialog", u"Shot", None))
        self.lbl_src.setText(QCoreApplication.translate("Copy_Dialog", u"Source:", None))
        self.lbl_dest.setText(QCoreApplication.translate("Copy_Dialog", u"Dest:", None))
        self.lbl_rate.setText(QCoreApplication.translate("Copy_Dialog", u"Transfer rate:", None))
        self.lbl_time_elapsed.setText(QCoreApplication.translate("Copy_Dialog", u"Time Elapsed:", None))
        self.lbl_time_remaining.setText(QCoreApplication.translate("Copy_Dialog", u"Time Remaining:", None))
    # retranslateUi

