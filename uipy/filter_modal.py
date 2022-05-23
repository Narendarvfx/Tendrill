# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CustomComboBox, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self._changed = False

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)
        self._changed = True

    def hidePopup(self):
        if not self._changed:
            super(CustomComboBox, self).hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == QtCore.Qt.Checked

    def setItemChecked(self, index, checked=True):
        item = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)

class Ui_Filters_Panel_Dialog(object):
    def setupUi(self, Filters_Panel_Dialog):
        if not Filters_Panel_Dialog.objectName():
            Filters_Panel_Dialog.setObjectName(u"Filters_Panel_Dialog")
        Filters_Panel_Dialog.setWindowModality(Qt.ApplicationModal)
        Filters_Panel_Dialog.resize(297, 435)
        Filters_Panel_Dialog.setStyleSheet(u"QDialog{\n"
"background-color: rgb(44, 49, 60);\n"
"	background-color: rgb(65, 72, 88);\n"
"border:1px solid rgba(255, 170, 0,0.5);\n"
"border-radius:5px}\n"
"\n"
"QPushButton {\n"
"	border: 2px solid rgb(29, 33, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	background-color: rgb(29, 33, 40);\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(38, 43, 52);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
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
"	border-left-color: rgba(39, 4"
                        "4, 54, 150);\n"
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
        Filters_Panel_Dialog.setModal(True)
        self.gridLayout_3 = QGridLayout(Filters_Panel_Dialog)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Filters_Panel_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.apply_filter_btn = QPushButton(self.frame_2)
        self.apply_filter_btn.setObjectName(u"apply_filter_btn")
        self.apply_filter_btn.setMinimumSize(QSize(80, 30))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.apply_filter_btn.setFont(font)
        self.apply_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/24x24/icons/24x24/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.apply_filter_btn.setIcon(icon)
        self.apply_filter_btn.setIconSize(QSize(13, 13))

        self.horizontalLayout.addWidget(self.apply_filter_btn)

        self.clear_filter_btn = QPushButton(self.frame_2)
        self.clear_filter_btn.setObjectName(u"clear_filter_btn")
        self.clear_filter_btn.setMinimumSize(QSize(80, 30))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.clear_filter_btn.setFont(font1)
        self.clear_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/24x24/icons/24x24/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_filter_btn.setIcon(icon1)
        self.clear_filter_btn.setIconSize(QSize(13, 13))

        self.horizontalLayout.addWidget(self.clear_filter_btn)

        self.set_default_btn = QPushButton(self.frame_2)
        self.set_default_btn.setObjectName(u"set_default_btn")
        self.set_default_btn.setMinimumSize(QSize(30, 30))
        self.set_default_btn.setFont(font)
        self.set_default_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/24x24/icons/24x24/cil-camera-roll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.set_default_btn.setIcon(icon2)
        self.set_default_btn.setIconSize(QSize(13, 13))

        self.horizontalLayout.addWidget(self.set_default_btn)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(Filters_Panel_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(193, 193, 193);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setContentsMargins(7, 0, 7, 0)
        self.project_label_frame = QFrame(self.frame)
        self.project_label_frame.setObjectName(u"project_label_frame")
        self.project_label_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(59, 65, 80);\n"
"border : 1px solid rgb(22, 22, 22);\n"
"border-radius : 5px\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"padding : 2px;\n"
"	background-color: rgb(22, 22, 22);\n"
"border : 1px solid rgb(22, 22, 22);\n"
"border-radius : 5px\n"
"}")
        self.project_label_frame.setFrameShape(QFrame.StyledPanel)
        self.project_label_frame.setFrameShadow(QFrame.Raised)
        self.project_layout = QGridLayout(self.project_label_frame)
        self.project_layout.setObjectName(u"project_layout")

        self.gridLayout.addWidget(self.project_label_frame, 5, 0, 1, 1)

        self.stat_filter_cb = CustomComboBox(self.frame)
        self.stat_filter_cb.addItem("")
        self.stat_filter_cb.addItem("")
        self.stat_filter_cb.addItem("")
        self.stat_filter_cb.setObjectName(u"stat_filter_cb")
        font2 = QFont()
        font2.setPointSize(10)
        self.stat_filter_cb.setFont(font2)

        self.gridLayout.addWidget(self.stat_filter_cb, 6, 0, 1, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.client_label_frame = QFrame(self.frame)
        self.client_label_frame.setObjectName(u"client_label_frame")
        self.client_label_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(59, 65, 80);\n"
"border : 1px solid rgb(22, 22, 22);\n"
"border-radius : 5px\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"padding : 2px;\n"
"	background-color: rgb(109, 109, 109);\n"
"border : 1px solid rgb(22, 22, 22);\n"
"border-radius : 5px\n"
"}")
        self.client_label_frame.setFrameShape(QFrame.StyledPanel)
        self.client_label_frame.setFrameShadow(QFrame.Raised)
        self.client_layout = QGridLayout(self.client_label_frame)
        self.client_layout.setObjectName(u"client_layout")

        self.gridLayout.addWidget(self.client_label_frame, 3, 0, 1, 1)

        self.pro_filter_cb = CustomComboBox(self.frame)
        self.pro_filter_cb.addItem("")
        self.pro_filter_cb.addItem("")
        self.pro_filter_cb.addItem("")
        self.pro_filter_cb.setObjectName(u"pro_filter_cb")
        self.pro_filter_cb.setFont(font2)

        self.gridLayout.addWidget(self.pro_filter_cb, 4, 0, 1, 1)

        self.cli_filter_cb = CustomComboBox(self.frame)
        self.cli_filter_cb.addItem("")
        self.cli_filter_cb.addItem("")
        self.cli_filter_cb.addItem("")
        self.cli_filter_cb.setObjectName(u"cli_filter_cb")
        self.cli_filter_cb.setFont(font2)

        self.gridLayout.addWidget(self.cli_filter_cb, 2, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 9, 0, 1, 1)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)

        self.status_label_frame = QFrame(self.frame)
        self.status_label_frame.setObjectName(u"status_label_frame")
        self.status_label_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(59, 65, 80);\n"
"border : 1px solid rgb(22, 22, 22);\n"
"border-radius : 5px\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"padding : 2px;\n"
"	background-color: rgb(22, 22, 22);\n"
"border : 1px solid rgb(22, 22, 22);\n"
"border-radius : 5px\n"
"}")
        self.status_label_frame.setFrameShape(QFrame.StyledPanel)
        self.status_label_frame.setFrameShadow(QFrame.Raised)
        self.status_layout = QGridLayout(self.status_label_frame)
        self.status_layout.setObjectName(u"status_layout")

        self.gridLayout.addWidget(self.status_label_frame, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Filters_Panel_Dialog)

        QMetaObject.connectSlotsByName(Filters_Panel_Dialog)
    # setupUi

    def retranslateUi(self, Filters_Panel_Dialog):
        Filters_Panel_Dialog.setWindowTitle(QCoreApplication.translate("Filters_Panel_Dialog", u"Dialog", None))
        self.apply_filter_btn.setText(QCoreApplication.translate("Filters_Panel_Dialog", u"Apply Filters", None))
        self.clear_filter_btn.setText(QCoreApplication.translate("Filters_Panel_Dialog", u"Clear Filters", None))
        self.set_default_btn.setText(QCoreApplication.translate("Filters_Panel_Dialog", u"Set Defaults", None))
        self.stat_filter_cb.setItemText(0, QCoreApplication.translate("Filters_Panel_Dialog", u"Status", None))
        self.stat_filter_cb.setItemText(1, QCoreApplication.translate("Filters_Panel_Dialog", u"Status2", None))
        self.stat_filter_cb.setItemText(2, QCoreApplication.translate("Filters_Panel_Dialog", u"Status3", None))

        self.pro_filter_cb.setItemText(0, QCoreApplication.translate("Filters_Panel_Dialog", u"Project01", None))
        self.pro_filter_cb.setItemText(1, QCoreApplication.translate("Filters_Panel_Dialog", u"Project02", None))
        self.pro_filter_cb.setItemText(2, QCoreApplication.translate("Filters_Panel_Dialog", u"Project03", None))

        self.cli_filter_cb.setItemText(0, QCoreApplication.translate("Filters_Panel_Dialog", u"Client1", None))
        self.cli_filter_cb.setItemText(1, QCoreApplication.translate("Filters_Panel_Dialog", u"Client2", None))
        self.cli_filter_cb.setItemText(2, QCoreApplication.translate("Filters_Panel_Dialog", u"Client3", None))

        self.label_6.setText(QCoreApplication.translate("Filters_Panel_Dialog", u"FILTERS PANEL", None))
    # retranslateUi

