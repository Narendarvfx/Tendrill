# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc
from PySide2 import QtCore
from PySide2.QtWidgets import QComboBox


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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1468, 860)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/custom/icons/custom/tendril.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setPointSize(10)
        self.centralwidget.setFont(font1)
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralLayout = QGridLayout(self.centralwidget)
        self.centralLayout.setObjectName(u"centralLayout")
        self.centralLayout.setHorizontalSpacing(7)
        self.centralLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFont(font1)
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
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
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 7px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(85, 170, 255, 100);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 10px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77rgb(85, 170, 255));"
                        "\n"
"    width: 10px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 7px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgba(85, 170, 255, 100);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 10px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;"
                        "\n"
"    background: rgb(55, 63, 77);\n"
"     height: 10px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
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
""
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
"	border: 3px solid rgb(52, 59, 72);	\n"
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
" }"
                        "\n"
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
"	margin: 0px;\n"
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
"	background-colo"
                        "r: rgb(55, 62, 76);\n"
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
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_main)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.frame_main)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 65))
        self.top_frame.setMaximumSize(QSize(16777215, 65))
        self.top_frame.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.top_frame)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.top_right_frame = QFrame(self.top_frame)
        self.top_right_frame.setObjectName(u"top_right_frame")
        self.top_right_frame.setStyleSheet(u"background-color: rgb(68, 136, 204);")
        self.top_right_frame.setFrameShape(QFrame.NoFrame)
        self.top_right_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.top_right_frame)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.top_right_frame)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setStyleSheet(u"")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        font2 = QFont()
        font2.setPointSize(8)
        self.frame_label_top_btns.setFont(font2)
        self.frame_label_top_btns.setStyleSheet(u"")
        self.frame_label_top_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(11, 0, -1, 0)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        self.label_title_bar_top.setMaximumSize(QSize(180, 16777215))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_title_bar_top.setFont(font3)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")
        self.label_title_bar_top.setPixmap(QPixmap(u":/custom/icons/custom/tendril.png"))
        self.label_title_bar_top.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_title_bar_top)

        self.frame_42 = QFrame(self.frame_label_top_btns)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_41.setSpacing(5)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_10)

        self.clients_pb = QPushButton(self.frame_42)
        self.clients_pb.setObjectName(u"clients_pb")
        self.clients_pb.setCursor(QCursor(Qt.PointingHandCursor))
        self.clients_pb.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/24x24/icons/twotone_home_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clients_pb.setIcon(icon1)
        self.clients_pb.setIconSize(QSize(32, 32))
        self.clients_pb.setFlat(True)

        self.horizontalLayout_41.addWidget(self.clients_pb)

        self.shots_ingest_pb = QPushButton(self.frame_42)
        self.shots_ingest_pb.setObjectName(u"shots_ingest_pb")
        icon2 = QIcon()
        icon2.addFile(u":/24x24/icons/twotone_get_app_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shots_ingest_pb.setIcon(icon2)
        self.shots_ingest_pb.setIconSize(QSize(32, 32))
        self.shots_ingest_pb.setFlat(True)

        self.horizontalLayout_41.addWidget(self.shots_ingest_pb)

        self.all_shots_pb = QPushButton(self.frame_42)
        self.all_shots_pb.setObjectName(u"all_shots_pb")
        self.all_shots_pb.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/24x24/icons/twotone_line_weight_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.all_shots_pb.setIcon(icon3)
        self.all_shots_pb.setIconSize(QSize(32, 32))
        self.all_shots_pb.setFlat(True)

        self.horizontalLayout_41.addWidget(self.all_shots_pb)

        self.my_task_pb = QPushButton(self.frame_42)
        self.my_task_pb.setObjectName(u"my_task_pb")
        self.my_task_pb.setMinimumSize(QSize(0, 20))
        self.my_task_pb.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/24x24/icons/twotone_military_tech_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.my_task_pb.setIcon(icon4)
        self.my_task_pb.setIconSize(QSize(32, 32))
        self.my_task_pb.setFlat(True)

        self.horizontalLayout_41.addWidget(self.my_task_pb)

        self.refresh_btn = QPushButton(self.frame_42)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/24x24/icons/twotone_change_circle_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_btn.setIcon(icon5)
        self.refresh_btn.setIconSize(QSize(32, 32))
        self.refresh_btn.setFlat(True)

        self.horizontalLayout_41.addWidget(self.refresh_btn)

        self.chng_pwd_pb = QPushButton(self.frame_42)
        self.chng_pwd_pb.setObjectName(u"chng_pwd_pb")
        self.chng_pwd_pb.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/24x24/icons/twotone_password_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chng_pwd_pb.setIcon(icon6)
        self.chng_pwd_pb.setIconSize(QSize(32, 32))
        self.chng_pwd_pb.setFlat(True)

        self.horizontalLayout_41.addWidget(self.chng_pwd_pb)

        self.log_out_btn = QPushButton(self.frame_42)
        self.log_out_btn.setObjectName(u"log_out_btn")
        self.log_out_btn.setMinimumSize(QSize(0, 20))
        self.log_out_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/custom/icons/custom/baseline_logout_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.log_out_btn.setIcon(icon7)
        self.log_out_btn.setIconSize(QSize(32, 32))
        self.log_out_btn.setFlat(True)

        self.horizontalLayout_41.addWidget(self.log_out_btn)


        self.horizontalLayout_9.addWidget(self.frame_42)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_15 = QFrame(self.frame_btns_right)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_15)

        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy1.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 10, 46);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255, 10, 46);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right)


        self.gridLayout_16.addWidget(self.frame_top_btns, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.top_right_frame, 0, 1, 1, 1)

        self.toggle_frame = QFrame(self.top_frame)
        self.toggle_frame.setObjectName(u"toggle_frame")
        self.toggle_frame.setMaximumSize(QSize(70, 16777215))
        self.toggle_frame.setStyleSheet(u"")
        self.toggle_frame.setFrameShape(QFrame.NoFrame)
        self.toggle_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.toggle_frame)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_14.addWidget(self.toggle_frame, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.top_frame, 0, 0, 1, 1)

        self.center_frame = QFrame(self.frame_main)
        self.center_frame.setObjectName(u"center_frame")
        self.center_frame.setFont(font1)
        self.center_frame.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.center_frame.setFrameShape(QFrame.NoFrame)
        self.center_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.center_frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setVerticalSpacing(7)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.center_right_frame = QFrame(self.center_frame)
        self.center_right_frame.setObjectName(u"center_right_frame")
        self.center_right_frame.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.center_right_frame.setFrameShape(QFrame.NoFrame)
        self.center_right_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.center_right_frame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_grip = QFrame(self.center_right_frame)
        self.frame_grip.setObjectName(u"frame_grip")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_grip.sizePolicy().hasHeightForWidth())
        self.frame_grip.setSizePolicy(sizePolicy2)
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        self.label_credits.setFont(font4)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_8.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setFont(font4)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_version)


        self.horizontalLayout_7.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_size_grip)


        self.gridLayout_12.addWidget(self.frame_grip, 1, 0, 1, 1)

        self.content_frame = QFrame(self.center_right_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFont(font1)
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.content_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_3 = QFrame(self.content_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_3)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.clients_page = QWidget()
        self.clients_page.setObjectName(u"clients_page")
        self.gridLayout_2 = QGridLayout(self.clients_page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.clients_frame = QFrame(self.clients_page)
        self.clients_frame.setObjectName(u"clients_frame")
        self.clients_frame.setFont(font1)
        self.clients_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.clients_frame.setFrameShape(QFrame.NoFrame)
        self.clients_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.clients_frame)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.clients_top_frame = QFrame(self.clients_frame)
        self.clients_top_frame.setObjectName(u"clients_top_frame")
        self.clients_top_frame.setStyleSheet(u"QFrame{border-bottom:1px solid  rgb(44, 49, 60);}")
        self.clients_top_frame.setFrameShape(QFrame.StyledPanel)
        self.clients_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.clients_top_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.clients_top_frame)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(12)
        self.label_3.setFont(font5)
        self.label_3.setPixmap(QPixmap(u":/16x16/icons/16x16/cil-user.png"))
        self.label_3.setScaledContents(False)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.clients_label = QLabel(self.clients_top_frame)
        self.clients_label.setObjectName(u"clients_label")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(13)
        self.clients_label.setFont(font6)
        self.clients_label.setStyleSheet(u"QLabel{border:none}")

        self.horizontalLayout_10.addWidget(self.clients_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.cli_add_btn = QPushButton(self.clients_top_frame)
        self.cli_add_btn.setObjectName(u"cli_add_btn")
        self.cli_add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/24x24/baseline_note_add_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cli_add_btn.setIcon(icon11)
        self.cli_add_btn.setIconSize(QSize(24, 24))
        self.cli_add_btn.setFlat(True)

        self.horizontalLayout_10.addWidget(self.cli_add_btn)


        self.gridLayout_18.addWidget(self.clients_top_frame, 0, 0, 1, 1)

        self.cli_table = QTableWidget(self.clients_frame)
        if (self.cli_table.columnCount() < 3):
            self.cli_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.cli_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cli_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cli_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.cli_table.rowCount() < 3):
            self.cli_table.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cli_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cli_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.cli_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.cli_table.setItem(0, 0, __qtablewidgetitem6)
        brush1 = QBrush(QColor(255, 170, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setBackground(brush1);
        self.cli_table.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.cli_table.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.cli_table.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.cli_table.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.cli_table.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.cli_table.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.cli_table.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.cli_table.setItem(2, 2, __qtablewidgetitem14)
        self.cli_table.setObjectName(u"cli_table")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        self.cli_table.setFont(font7)
        self.cli_table.setFocusPolicy(Qt.NoFocus)
        self.cli_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(28, 32, 40);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:h"
                        "orizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"")
        self.cli_table.setFrameShape(QFrame.NoFrame)
        self.cli_table.setFrameShadow(QFrame.Raised)
        self.cli_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.cli_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.cli_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cli_table.setAlternatingRowColors(False)
        self.cli_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.cli_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cli_table.setShowGrid(False)
        self.cli_table.setGridStyle(Qt.DashLine)
        self.cli_table.setSortingEnabled(True)
        self.cli_table.setWordWrap(True)
        self.cli_table.setRowCount(3)
        self.cli_table.horizontalHeader().setDefaultSectionSize(250)
        self.cli_table.verticalHeader().setVisible(False)

        self.gridLayout_18.addWidget(self.cli_table, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.clients_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.clients_page)
        self.projects_page = QWidget()
        self.projects_page.setObjectName(u"projects_page")
        self.projects_page.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.projects_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.projects_frame = QFrame(self.projects_page)
        self.projects_frame.setObjectName(u"projects_frame")
        self.projects_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.projects_frame.setFrameShape(QFrame.StyledPanel)
        self.projects_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.projects_frame)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pro_top_frame = QFrame(self.projects_frame)
        self.pro_top_frame.setObjectName(u"pro_top_frame")
        self.pro_top_frame.setStyleSheet(u"QFrame{border-bottom:1px solid  rgb(44, 49, 60);}")
        self.pro_top_frame.setFrameShape(QFrame.StyledPanel)
        self.pro_top_frame.setFrameShadow(QFrame.Raised)
        self.pro_top_frameLayout = QHBoxLayout(self.pro_top_frame)
        self.pro_top_frameLayout.setSpacing(7)
        self.pro_top_frameLayout.setObjectName(u"pro_top_frameLayout")
        self.pro_top_frameLayout.setContentsMargins(11, 11, 11, 11)
        self.label_4 = QLabel(self.pro_top_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/16x16/icons/16x16/cil-3d.png"))

        self.pro_top_frameLayout.addWidget(self.label_4)

        self.pro_label = QLabel(self.pro_top_frame)
        self.pro_label.setObjectName(u"pro_label")
        self.pro_label.setFont(font6)
        self.pro_label.setStyleSheet(u"QLabel{border:none}")

        self.pro_top_frameLayout.addWidget(self.pro_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.pro_top_frameLayout.addItem(self.horizontalSpacer_5)

        self.pro_add_btn = QPushButton(self.pro_top_frame)
        self.pro_add_btn.setObjectName(u"pro_add_btn")
        self.pro_add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/24x24/icons/24x24/cil-medical-cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pro_add_btn.setIcon(icon12)
        self.pro_add_btn.setIconSize(QSize(24, 24))
        self.pro_add_btn.setFlat(True)

        self.pro_top_frameLayout.addWidget(self.pro_add_btn)


        self.gridLayout_20.addWidget(self.pro_top_frame, 0, 0, 1, 1)

        self.pro_table = QTableWidget(self.projects_frame)
        if (self.pro_table.columnCount() < 2):
            self.pro_table.setColumnCount(2)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.pro_table.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.pro_table.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        self.pro_table.setObjectName(u"pro_table")
        self.pro_table.setFont(font5)
        self.pro_table.setFocusPolicy(Qt.NoFocus)
        self.pro_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(28, 32, 40);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
""
                        "	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"")
        self.pro_table.setFrameShape(QFrame.NoFrame)
        self.pro_table.setFrameShadow(QFrame.Raised)
        self.pro_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pro_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pro_table.setShowGrid(False)
        self.pro_table.setSortingEnabled(True)
        self.pro_table.setColumnCount(2)
        self.pro_table.verticalHeader().setVisible(False)

        self.gridLayout_20.addWidget(self.pro_table, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.projects_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.projects_page)
        self.shot_details_page = QWidget()
        self.shot_details_page.setObjectName(u"shot_details_page")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.shot_details_page.sizePolicy().hasHeightForWidth())
        self.shot_details_page.setSizePolicy(sizePolicy3)
        self.shot_details_page.setFont(font1)
        self.shot_details_page_2 = QGridLayout(self.shot_details_page)
        self.shot_details_page_2.setObjectName(u"shot_details_page_2")
        self.shot_details_page_2.setHorizontalSpacing(0)
        self.shot_details_page_2.setContentsMargins(0, 0, 0, 0)
        self.shot_details_main_frame = QFrame(self.shot_details_page)
        self.shot_details_main_frame.setObjectName(u"shot_details_main_frame")
        self.shot_details_main_frame.setFont(font1)
        self.shot_details_main_frame.setFrameShape(QFrame.StyledPanel)
        self.shot_details_main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.shot_details_main_frame)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.shot_details_top_frame = QFrame(self.shot_details_main_frame)
        self.shot_details_top_frame.setObjectName(u"shot_details_top_frame")
        self.shot_details_top_frame.setStyleSheet(u"QFrame{background-color: rgb(30, 34, 42);}\n"
"")
        self.shot_details_top_frame.setFrameShape(QFrame.StyledPanel)
        self.shot_details_top_frame.setFrameShadow(QFrame.Raised)
        self.shot_details_top_frame.setMidLineWidth(0)
        self.gridLayout = QGridLayout(self.shot_details_top_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.shot_details_top_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QPushButton{\n"
"background:none\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_17)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_7 = QFrame(self.frame_17)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(100, 0))
        self.frame_7.setMaximumSize(QSize(200, 16777215))
        self.frame_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(167, 167, 167);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_17.setFont(font8)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.shotName_lbl = QLabel(self.frame_7)
        self.shotName_lbl.setObjectName(u"shotName_lbl")
        self.shotName_lbl.setFont(font1)
        self.shotName_lbl.setStyleSheet(u"QLabel{\n"
"	color: rgb(167, 167, 167);\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.shotName_lbl)

        self.line_7 = QFrame(self.frame_7)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(1, 16777215))
        font9 = QFont()
        font9.setPointSize(11)
        self.line_7.setFont(font9)
        self.line_7.setStyleSheet(u"background-color: rgb(45, 51, 63);")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.line_7)

        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font8)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_22)

        self.status_btn = QPushButton(self.frame_7)
        self.status_btn.setObjectName(u"status_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.status_btn.sizePolicy().hasHeightForWidth())
        self.status_btn.setSizePolicy(sizePolicy4)
        font10 = QFont()
        font10.setFamily(u"MS Shell Dlg 2")
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setWeight(50)
        self.status_btn.setFont(font10)
        self.status_btn.setLayoutDirection(Qt.LeftToRight)
        self.status_btn.setStyleSheet(u"")
        self.status_btn.setFlat(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.status_btn)

        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font8)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_23)

        self.clientName_lbl = QLabel(self.frame_7)
        self.clientName_lbl.setObjectName(u"clientName_lbl")
        self.clientName_lbl.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.clientName_lbl)

        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font8)
        self.label_27.setCursor(QCursor(Qt.ArrowCursor))

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_27)

        self.eta_lbl = QLabel(self.frame_7)
        self.eta_lbl.setObjectName(u"eta_lbl")
        self.eta_lbl.setFont(font1)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.eta_lbl)

        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font8)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_29)

        self.projectName_lbl = QLabel(self.frame_7)
        self.projectName_lbl.setObjectName(u"projectName_lbl")
        self.projectName_lbl.setFont(font1)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.projectName_lbl)

        self.label_30 = QLabel(self.frame_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font8)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_30)

        self.startDate_lbl = QLabel(self.frame_7)
        self.startDate_lbl.setObjectName(u"startDate_lbl")
        self.startDate_lbl.setFont(font1)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.startDate_lbl)

        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font8)

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_31)

        self.endDate_lbl = QLabel(self.frame_7)
        self.endDate_lbl.setObjectName(u"endDate_lbl")
        self.endDate_lbl.setFont(font1)

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.endDate_lbl)

        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font8)

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.label_33)

        self.totalBids_lbl = QLabel(self.frame_7)
        self.totalBids_lbl.setObjectName(u"totalBids_lbl")
        self.totalBids_lbl.setFont(font1)

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.totalBids_lbl)

        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font8)

        self.formLayout_2.setWidget(16, QFormLayout.LabelRole, self.label_34)

        self.seqName_lbl = QLabel(self.frame_7)
        self.seqName_lbl.setObjectName(u"seqName_lbl")
        self.seqName_lbl.setFont(font1)

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.seqName_lbl)

        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setWeight(75)
        self.label_35.setFont(font11)

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.label_35)

        self.frameIn_lbl = QLabel(self.frame_7)
        self.frameIn_lbl.setObjectName(u"frameIn_lbl")
        self.frameIn_lbl.setFont(font1)

        self.formLayout_2.setWidget(18, QFormLayout.FieldRole, self.frameIn_lbl)

        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font8)

        self.formLayout_2.setWidget(20, QFormLayout.LabelRole, self.label_36)

        self.frameOut_lbl = QLabel(self.frame_7)
        self.frameOut_lbl.setObjectName(u"frameOut_lbl")
        self.frameOut_lbl.setFont(font1)

        self.formLayout_2.setWidget(20, QFormLayout.FieldRole, self.frameOut_lbl)

        self.label_38 = QLabel(self.frame_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font8)

        self.formLayout_2.setWidget(22, QFormLayout.LabelRole, self.label_38)

        self.totalFrames_lbl = QLabel(self.frame_7)
        self.totalFrames_lbl.setObjectName(u"totalFrames_lbl")
        self.totalFrames_lbl.setFont(font1)

        self.formLayout_2.setWidget(22, QFormLayout.FieldRole, self.totalFrames_lbl)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.shot_details_tabWidget = QTabWidget(self.frame_17)
        self.shot_details_tabWidget.setObjectName(u"shot_details_tabWidget")
        self.shot_details_tabWidget.setFont(font)
        self.shot_details_tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 2px solidrgb(85, 170, 255);\n"
"}\n"
"QTabWidget::tab-bar {\n"
"left:3px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"border-top-left-radius: 2px;\n"
"border-top-right-radius: 2px;\n"
"padding: 10px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"color: rgb(85, 170, 255);\n"
"border-bottom: 2px solid rgb(85, 170, 255); /* same as pane color */ \n"
"}\n"
"QTabBar::tab:hover {\n"
"color: rgba(191, 127, 0,0.5);\n"
"border-bottom: 1px solid rgba(247, 128, 23,0.2); /* same as pane color */ \n"
"}\n"
"")
        self.shot_details_tabWidget.setTabPosition(QTabWidget.North)
        self.shot_details_tabWidget.setTabShape(QTabWidget.Rounded)
        self.shot_details_tabWidget.setIconSize(QSize(20, 20))
        self.shot_details_tabWidget.setElideMode(Qt.ElideNone)
        self.shot_details_tabWidget.setUsesScrollButtons(True)
        self.shot_details_tabWidget.setDocumentMode(False)
        self.shot_details_tabWidget.setTabsClosable(False)
        self.shot_details_tabWidget.setMovable(True)
        self.shot_details_tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_12 = QHBoxLayout(self.tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_label_2 = QLabel(self.tab)
        self.input_label_2.setObjectName(u"input_label_2")
        self.input_label_2.setMinimumSize(QSize(10, 0))
        font12 = QFont()
        font12.setPointSize(16)
        font12.setBold(True)
        font12.setWeight(75)
        self.input_label_2.setFont(font12)
        self.input_label_2.setLayoutDirection(Qt.LeftToRight)
        self.input_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.input_label_2)

        self.taskann = QListWidget(self.tab)
        self.taskann.setObjectName(u"taskann")
        self.taskann.setMinimumSize(QSize(200, 0))
        self.taskann.setFont(font1)
        self.taskann.setFrameShape(QFrame.NoFrame)
        self.taskann.setFrameShadow(QFrame.Sunken)
        self.taskann.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)

        self.verticalLayout_2.addWidget(self.taskann)


        self.horizontalLayout_12.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.input_label_3 = QLabel(self.tab)
        self.input_label_3.setObjectName(u"input_label_3")
        self.input_label_3.setMinimumSize(QSize(10, 0))
        self.input_label_3.setFont(font12)
        self.input_label_3.setLayoutDirection(Qt.LeftToRight)
        self.input_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.input_label_3)

        self.feedbackann = QListView(self.tab)
        self.feedbackann.setObjectName(u"feedbackann")
        self.feedbackann.setMinimumSize(QSize(200, 0))
        self.feedbackann.setFont(font1)
        self.feedbackann.setFrameShape(QFrame.NoFrame)
        self.feedbackann.setFrameShadow(QFrame.Sunken)
        self.feedbackann.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)

        self.verticalLayout_6.addWidget(self.feedbackann)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)

        self.line_12 = QFrame(self.tab)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setMaximumSize(QSize(16777215, 2))
        self.line_12.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_12)

        self.shot_details_tabWidget.addTab(self.tab, "")
        self.assests = QWidget()
        self.assests.setObjectName(u"assests")
        self.gridLayout_4 = QGridLayout(self.assests)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(8, 8, 8, 8)
        self.assets_main_frame = QFrame(self.assests)
        self.assets_main_frame.setObjectName(u"assets_main_frame")
        sizePolicy3.setHeightForWidth(self.assets_main_frame.sizePolicy().hasHeightForWidth())
        self.assets_main_frame.setSizePolicy(sizePolicy3)
        self.assets_main_frame.setFrameShape(QFrame.StyledPanel)
        self.assets_main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.assets_main_frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.assests_dep_frame = QFrame(self.assets_main_frame)
        self.assests_dep_frame.setObjectName(u"assests_dep_frame")
        sizePolicy3.setHeightForWidth(self.assests_dep_frame.sizePolicy().hasHeightForWidth())
        self.assests_dep_frame.setSizePolicy(sizePolicy3)
        self.assests_dep_frame.setStyleSheet(u"")
        self.assests_dep_frame.setFrameShape(QFrame.StyledPanel)
        self.assests_dep_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.assests_dep_frame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dep_tabWidget = QTabWidget(self.assests_dep_frame)
        self.dep_tabWidget.setObjectName(u"dep_tabWidget")
        self.dep_tabWidget.setFont(font1)
        self.paint_tab = QWidget()
        self.paint_tab.setObjectName(u"paint_tab")
        self.gridLayout_19 = QGridLayout(self.paint_tab)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 8, 0, 0)
        self.scripts_pre_frame = QFrame(self.paint_tab)
        self.scripts_pre_frame.setObjectName(u"scripts_pre_frame")
        sizePolicy3.setHeightForWidth(self.scripts_pre_frame.sizePolicy().hasHeightForWidth())
        self.scripts_pre_frame.setSizePolicy(sizePolicy3)
        self.scripts_pre_frame.setFrameShape(QFrame.NoFrame)
        self.scripts_pre_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.scripts_pre_frame)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 8, 0)
        self.scripts_frame = QFrame(self.scripts_pre_frame)
        self.scripts_frame.setObjectName(u"scripts_frame")
        self.scripts_frame.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.scripts_frame.setFrameShape(QFrame.NoFrame)
        self.scripts_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.scripts_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 8, 0, 8)
        self.scripts_label_frame = QFrame(self.scripts_frame)
        self.scripts_label_frame.setObjectName(u"scripts_label_frame")
        self.scripts_label_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.scripts_label_frame.setFrameShape(QFrame.NoFrame)
        self.scripts_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.scripts_label_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(7, 0, 7, 0)
        self.scripts_label = QLabel(self.scripts_label_frame)
        self.scripts_label.setObjectName(u"scripts_label")
        self.scripts_label.setFont(font9)
        self.scripts_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.scripts_label)


        self.horizontalLayout_13.addWidget(self.scripts_label_frame)

        self.Pscripts_treeWid = QTreeWidget(self.scripts_frame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(6, u"7");
        __qtreewidgetitem.setText(5, u"6");
        self.Pscripts_treeWid.setHeaderItem(__qtreewidgetitem)
        self.Pscripts_treeWid.setObjectName(u"Pscripts_treeWid")
        self.Pscripts_treeWid.setFont(font1)
        self.Pscripts_treeWid.setStyleSheet(u"alternate-background-color: rgb(32, 36, 45);")
        self.Pscripts_treeWid.setFrameShape(QFrame.NoFrame)
        self.Pscripts_treeWid.setFrameShadow(QFrame.Raised)
        self.Pscripts_treeWid.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Pscripts_treeWid.setAutoScroll(True)
        self.Pscripts_treeWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Pscripts_treeWid.setAlternatingRowColors(True)
        self.Pscripts_treeWid.setAnimated(True)
        self.Pscripts_treeWid.setColumnCount(7)
        self.Pscripts_treeWid.header().setVisible(False)

        self.horizontalLayout_13.addWidget(self.Pscripts_treeWid)

        self.Pscripts_treeWid.raise_()
        self.scripts_label_frame.raise_()

        self.verticalLayout_3.addWidget(self.scripts_frame)

        self.line_10 = QFrame(self.scripts_pre_frame)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_10)

        self.output_frame = QFrame(self.scripts_pre_frame)
        self.output_frame.setObjectName(u"output_frame")
        self.output_frame.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.output_frame.setFrameShape(QFrame.NoFrame)
        self.output_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.output_frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 8, 0, 8)
        self.preren_label_frame = QFrame(self.output_frame)
        self.preren_label_frame.setObjectName(u"preren_label_frame")
        self.preren_label_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.preren_label_frame.setFrameShape(QFrame.NoFrame)
        self.preren_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.preren_label_frame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(7, 0, 7, 0)
        self.preren_label = QLabel(self.preren_label_frame)
        self.preren_label.setObjectName(u"preren_label")
        self.preren_label.setFont(font9)
        self.preren_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.preren_label)


        self.horizontalLayout_17.addWidget(self.preren_label_frame)

        self.Poutput_treeWid = QTreeWidget(self.output_frame)
        self.Poutput_treeWid.setObjectName(u"Poutput_treeWid")
        self.Poutput_treeWid.setStyleSheet(u"alternate-background-color: rgb(32, 36, 45);")
        self.Poutput_treeWid.setFrameShape(QFrame.NoFrame)
        self.Poutput_treeWid.setFrameShadow(QFrame.Raised)
        self.Poutput_treeWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Poutput_treeWid.setAlternatingRowColors(True)
        self.Poutput_treeWid.setAnimated(True)
        self.Poutput_treeWid.setColumnCount(5)
        self.Poutput_treeWid.header().setVisible(False)

        self.horizontalLayout_17.addWidget(self.Poutput_treeWid)

        self.Poutput_treeWid.raise_()
        self.preren_label_frame.raise_()

        self.verticalLayout_3.addWidget(self.output_frame)


        self.gridLayout_19.addWidget(self.scripts_pre_frame, 0, 0, 1, 1)

        self.ou_qc_frame = QFrame(self.paint_tab)
        self.ou_qc_frame.setObjectName(u"ou_qc_frame")
        self.ou_qc_frame.setFrameShape(QFrame.StyledPanel)
        self.ou_qc_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.ou_qc_frame)
        self.verticalLayout_10.setSpacing(8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 8, 0)

        self.gridLayout_19.addWidget(self.ou_qc_frame, 0, 1, 1, 1)

        self.dep_tabWidget.addTab(self.paint_tab, "")
        self.roto_tab = QWidget()
        self.roto_tab.setObjectName(u"roto_tab")
        self.gridLayout_27 = QGridLayout(self.roto_tab)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 8, 0, 0)
        self.scripts_pre_frame_2 = QFrame(self.roto_tab)
        self.scripts_pre_frame_2.setObjectName(u"scripts_pre_frame_2")
        sizePolicy3.setHeightForWidth(self.scripts_pre_frame_2.sizePolicy().hasHeightForWidth())
        self.scripts_pre_frame_2.setSizePolicy(sizePolicy3)
        self.scripts_pre_frame_2.setFrameShape(QFrame.NoFrame)
        self.scripts_pre_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.scripts_pre_frame_2)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 8, 0)
        self.scripts_frame_2 = QFrame(self.scripts_pre_frame_2)
        self.scripts_frame_2.setObjectName(u"scripts_frame_2")
        self.scripts_frame_2.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.scripts_frame_2.setFrameShape(QFrame.NoFrame)
        self.scripts_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.scripts_frame_2)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 8, 0, 8)
        self.scripts_label_frame_2 = QFrame(self.scripts_frame_2)
        self.scripts_label_frame_2.setObjectName(u"scripts_label_frame_2")
        self.scripts_label_frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.scripts_label_frame_2.setFrameShape(QFrame.NoFrame)
        self.scripts_label_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.scripts_label_frame_2)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(7, 0, 7, 0)
        self.scripts_label_2 = QLabel(self.scripts_label_frame_2)
        self.scripts_label_2.setObjectName(u"scripts_label_2")
        self.scripts_label_2.setFont(font9)
        self.scripts_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.scripts_label_2)


        self.horizontalLayout_25.addWidget(self.scripts_label_frame_2)

        self.Rscripts_treeWid = QTreeWidget(self.scripts_frame_2)
        self.Rscripts_treeWid.setObjectName(u"Rscripts_treeWid")
        self.Rscripts_treeWid.setFont(font1)
        self.Rscripts_treeWid.setStyleSheet(u"alternate-background-color: rgb(32, 36, 45);")
        self.Rscripts_treeWid.setFrameShape(QFrame.NoFrame)
        self.Rscripts_treeWid.setFrameShadow(QFrame.Raised)
        self.Rscripts_treeWid.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Rscripts_treeWid.setAutoScroll(True)
        self.Rscripts_treeWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rscripts_treeWid.setAlternatingRowColors(True)
        self.Rscripts_treeWid.setAnimated(True)
        self.Rscripts_treeWid.setColumnCount(5)
        self.Rscripts_treeWid.header().setVisible(False)

        self.horizontalLayout_25.addWidget(self.Rscripts_treeWid)


        self.verticalLayout_4.addWidget(self.scripts_frame_2)

        self.preren_frame_2 = QFrame(self.scripts_pre_frame_2)
        self.preren_frame_2.setObjectName(u"preren_frame_2")
        self.preren_frame_2.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.preren_frame_2.setFrameShape(QFrame.NoFrame)
        self.preren_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.preren_frame_2)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 8, 0, 8)
        self.preren_label_frame_2 = QFrame(self.preren_frame_2)
        self.preren_label_frame_2.setObjectName(u"preren_label_frame_2")
        self.preren_label_frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.preren_label_frame_2.setFrameShape(QFrame.NoFrame)
        self.preren_label_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.preren_label_frame_2)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(7, 0, 7, 0)
        self.preren_label_2 = QLabel(self.preren_label_frame_2)
        self.preren_label_2.setObjectName(u"preren_label_2")
        self.preren_label_2.setFont(font9)
        self.preren_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.preren_label_2)


        self.horizontalLayout_27.addWidget(self.preren_label_frame_2)

        self.Routput_treeWid = QTreeWidget(self.preren_frame_2)
        self.Routput_treeWid.setObjectName(u"Routput_treeWid")
        self.Routput_treeWid.setStyleSheet(u"alternate-background-color: rgb(32, 36, 45);")
        self.Routput_treeWid.setFrameShape(QFrame.NoFrame)
        self.Routput_treeWid.setFrameShadow(QFrame.Raised)
        self.Routput_treeWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Routput_treeWid.setAlternatingRowColors(True)
        self.Routput_treeWid.setAnimated(True)
        self.Routput_treeWid.setColumnCount(5)
        self.Routput_treeWid.header().setVisible(False)

        self.horizontalLayout_27.addWidget(self.Routput_treeWid)


        self.verticalLayout_4.addWidget(self.preren_frame_2)


        self.gridLayout_27.addWidget(self.scripts_pre_frame_2, 0, 0, 1, 1)

        self.ou_qc_frame_2 = QFrame(self.roto_tab)
        self.ou_qc_frame_2.setObjectName(u"ou_qc_frame_2")
        self.ou_qc_frame_2.setFrameShape(QFrame.StyledPanel)
        self.ou_qc_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.ou_qc_frame_2)
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 8, 0)

        self.gridLayout_27.addWidget(self.ou_qc_frame_2, 0, 1, 1, 1)

        self.dep_tabWidget.addTab(self.roto_tab, "")
        self.mm_tab = QWidget()
        self.mm_tab.setObjectName(u"mm_tab")
        self.gridLayout_26 = QGridLayout(self.mm_tab)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 8, 0, 0)
        self.scripts_pre_frame_3 = QFrame(self.mm_tab)
        self.scripts_pre_frame_3.setObjectName(u"scripts_pre_frame_3")
        sizePolicy3.setHeightForWidth(self.scripts_pre_frame_3.sizePolicy().hasHeightForWidth())
        self.scripts_pre_frame_3.setSizePolicy(sizePolicy3)
        self.scripts_pre_frame_3.setFrameShape(QFrame.NoFrame)
        self.scripts_pre_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.scripts_pre_frame_3)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 8, 0)
        self.scripts_frame_3 = QFrame(self.scripts_pre_frame_3)
        self.scripts_frame_3.setObjectName(u"scripts_frame_3")
        self.scripts_frame_3.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.scripts_frame_3.setFrameShape(QFrame.NoFrame)
        self.scripts_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.scripts_frame_3)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 8, 0, 8)
        self.scripts_label_frame_3 = QFrame(self.scripts_frame_3)
        self.scripts_label_frame_3.setObjectName(u"scripts_label_frame_3")
        self.scripts_label_frame_3.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.scripts_label_frame_3.setFrameShape(QFrame.NoFrame)
        self.scripts_label_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.scripts_label_frame_3)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(7, 0, 7, 0)
        self.scripts_label_3 = QLabel(self.scripts_label_frame_3)
        self.scripts_label_3.setObjectName(u"scripts_label_3")
        self.scripts_label_3.setFont(font9)
        self.scripts_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.scripts_label_3)


        self.horizontalLayout_33.addWidget(self.scripts_label_frame_3)

        self.Mscripts_treeWid = QTreeWidget(self.scripts_frame_3)
        self.Mscripts_treeWid.setObjectName(u"Mscripts_treeWid")
        self.Mscripts_treeWid.setFont(font1)
        self.Mscripts_treeWid.setStyleSheet(u"alternate-background-color: rgb(32, 36, 45);")
        self.Mscripts_treeWid.setFrameShape(QFrame.NoFrame)
        self.Mscripts_treeWid.setFrameShadow(QFrame.Raised)
        self.Mscripts_treeWid.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Mscripts_treeWid.setAutoScroll(True)
        self.Mscripts_treeWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Mscripts_treeWid.setAlternatingRowColors(True)
        self.Mscripts_treeWid.setAnimated(True)
        self.Mscripts_treeWid.setColumnCount(5)
        self.Mscripts_treeWid.header().setVisible(False)

        self.horizontalLayout_33.addWidget(self.Mscripts_treeWid)


        self.verticalLayout_5.addWidget(self.scripts_frame_3)

        self.preren_frame_3 = QFrame(self.scripts_pre_frame_3)
        self.preren_frame_3.setObjectName(u"preren_frame_3")
        self.preren_frame_3.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.preren_frame_3.setFrameShape(QFrame.NoFrame)
        self.preren_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.preren_frame_3)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 8, 0, 8)
        self.preren_label_frame_3 = QFrame(self.preren_frame_3)
        self.preren_label_frame_3.setObjectName(u"preren_label_frame_3")
        self.preren_label_frame_3.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.preren_label_frame_3.setFrameShape(QFrame.NoFrame)
        self.preren_label_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.preren_label_frame_3)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(7, 0, 7, 0)
        self.preren_label_3 = QLabel(self.preren_label_frame_3)
        self.preren_label_3.setObjectName(u"preren_label_3")
        self.preren_label_3.setFont(font9)
        self.preren_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.preren_label_3)


        self.horizontalLayout_35.addWidget(self.preren_label_frame_3)

        self.Moutput_treeWid = QTreeWidget(self.preren_frame_3)
        self.Moutput_treeWid.setObjectName(u"Moutput_treeWid")
        self.Moutput_treeWid.setStyleSheet(u"alternate-background-color: rgb(32, 36, 45);")
        self.Moutput_treeWid.setFrameShape(QFrame.NoFrame)
        self.Moutput_treeWid.setFrameShadow(QFrame.Raised)
        self.Moutput_treeWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Moutput_treeWid.setAlternatingRowColors(True)
        self.Moutput_treeWid.setAnimated(True)
        self.Moutput_treeWid.setColumnCount(5)
        self.Moutput_treeWid.header().setVisible(False)

        self.horizontalLayout_35.addWidget(self.Moutput_treeWid)


        self.verticalLayout_5.addWidget(self.preren_frame_3)


        self.gridLayout_26.addWidget(self.scripts_pre_frame_3, 0, 0, 1, 1)

        self.ou_qc_frame_3 = QFrame(self.mm_tab)
        self.ou_qc_frame_3.setObjectName(u"ou_qc_frame_3")
        self.ou_qc_frame_3.setFrameShape(QFrame.StyledPanel)
        self.ou_qc_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.ou_qc_frame_3)
        self.verticalLayout_12.setSpacing(8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 8, 0)

        self.gridLayout_26.addWidget(self.ou_qc_frame_3, 0, 1, 1, 1)

        self.dep_tabWidget.addTab(self.mm_tab, "")

        self.gridLayout_7.addWidget(self.dep_tabWidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.assests_dep_frame, 1, 0, 1, 1)

        self.inputs_frame = QFrame(self.assets_main_frame)
        self.inputs_frame.setObjectName(u"inputs_frame")
        self.inputs_frame.setMaximumSize(QSize(16777215, 171))
        self.inputs_frame.setStyleSheet(u"")
        self.inputs_frame.setFrameShape(QFrame.StyledPanel)
        self.inputs_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.inputs_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 8, 0)
        self.intput_treeWid_frame = QFrame(self.inputs_frame)
        self.intput_treeWid_frame.setObjectName(u"intput_treeWid_frame")
        self.intput_treeWid_frame.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.intput_treeWid_frame.setFrameShape(QFrame.StyledPanel)
        self.intput_treeWid_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.intput_treeWid_frame)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 8, 0, 8)
        self.input_label_frame = QFrame(self.intput_treeWid_frame)
        self.input_label_frame.setObjectName(u"input_label_frame")
        self.input_label_frame.setMinimumSize(QSize(10, 0))
        self.input_label_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.input_label_frame.setFrameShape(QFrame.StyledPanel)
        self.input_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.input_label_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.input_label = QLabel(self.input_label_frame)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMinimumSize(QSize(10, 0))
        self.input_label.setFont(font9)
        self.input_label.setLayoutDirection(Qt.LeftToRight)
        self.input_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.input_label)


        self.gridLayout_21.addWidget(self.input_label_frame, 0, 0, 1, 1)

        self.input_TreeWid = QTreeWidget(self.intput_treeWid_frame)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(2, u"3");
        __qtreewidgetitem1.setText(1, u"2");
        __qtreewidgetitem1.setText(0, u"1");
        self.input_TreeWid.setHeaderItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.input_TreeWid)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.input_TreeWid)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.input_TreeWid.setObjectName(u"input_TreeWid")
        self.input_TreeWid.setMinimumSize(QSize(200, 0))
        self.input_TreeWid.setFont(font1)
        self.input_TreeWid.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-top: 1px solid red;\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1p"
                        "x solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.input_TreeWid.setFrameShape(QFrame.NoFrame)
        self.input_TreeWid.setFrameShadow(QFrame.Sunken)
        self.input_TreeWid.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.input_TreeWid.setColumnCount(3)
        self.input_TreeWid.header().setVisible(False)
        self.input_TreeWid.header().setCascadingSectionResizes(False)

        self.gridLayout_21.addWidget(self.input_TreeWid, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.intput_treeWid_frame)


        self.gridLayout_5.addWidget(self.inputs_frame, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.assets_main_frame, 0, 0, 1, 1)

        self.discussion_frame = QFrame(self.assests)
        self.discussion_frame.setObjectName(u"discussion_frame")
        self.discussion_frame.setMinimumSize(QSize(350, 0))
        self.discussion_frame.setMaximumSize(QSize(450, 16777215))
        self.discussion_frame.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.discussion_frame.setFrameShape(QFrame.StyledPanel)
        self.discussion_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.discussion_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(7)
        self.gridLayout_8.setContentsMargins(8, 0, 8, 0)
        self.text_type_frame = QFrame(self.discussion_frame)
        self.text_type_frame.setObjectName(u"text_type_frame")
        self.text_type_frame.setMaximumSize(QSize(16777215, 60))
        self.text_type_frame.setFrameShape(QFrame.StyledPanel)
        self.text_type_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.text_type_frame)
        self.horizontalLayout_20.setSpacing(3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 0, 2, 2)
        self.text_type_edit = QTextEdit(self.text_type_frame)
        self.text_type_edit.setObjectName(u"text_type_edit")
        self.text_type_edit.setFont(font1)
        self.text_type_edit.setStyleSheet(u"border: 1px solid rgba(39, 44, 54, 0.5);")
        self.text_type_edit.setLineWrapColumnOrWidth(1)

        self.horizontalLayout_20.addWidget(self.text_type_edit)

        self.send_btn = QToolButton(self.text_type_frame)
        self.send_btn.setObjectName(u"send_btn")
        icon13 = QIcon()
        icon13.addFile(u":/20x20/icons/20x20/cil-cursor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_btn.setIcon(icon13)

        self.horizontalLayout_20.addWidget(self.send_btn)


        self.gridLayout_8.addWidget(self.text_type_frame, 2, 0, 1, 1)

        self.dis_label_frame = QFrame(self.discussion_frame)
        self.dis_label_frame.setObjectName(u"dis_label_frame")
        self.dis_label_frame.setStyleSheet(u"background-color: rgba(0, 97, 145, 0.5);")
        self.dis_label_frame.setFrameShape(QFrame.NoFrame)
        self.dis_label_frame.setFrameShadow(QFrame.Raised)
        self.dis_label_frame.setLineWidth(1)
        self.gridLayout_9 = QGridLayout(self.dis_label_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 5, 0, 5)
        self.dis_label = QLabel(self.dis_label_frame)
        self.dis_label.setObjectName(u"dis_label")
        self.dis_label.setFont(font5)
        self.dis_label.setStyleSheet(u"background:none;")
        self.dis_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.dis_label, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.dis_label_frame, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.discussion_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFont(font1)
        self.scrollArea.setStyleSheet(u"border:none;")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.chat_area_widget = QWidget()
        self.chat_area_widget.setObjectName(u"chat_area_widget")
        self.chat_area_widget.setGeometry(QRect(0, 0, 434, 554))
        self.chat_area_widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.chat_area_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.scrollArea.setWidget(self.chat_area_widget)

        self.gridLayout_8.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.discussion_frame, 0, 1, 1, 1)

        self.shot_details_tabWidget.addTab(self.assests, "")
        self.versions_page = QWidget()
        self.versions_page.setObjectName(u"versions_page")
        self.gridLayout_37 = QGridLayout(self.versions_page)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.versions_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_12)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(0)
        self.gridLayout_31.setVerticalSpacing(10)
        self.gridLayout_31.setContentsMargins(8, 0, 8, 0)
        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_11)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 8, 0, 8)
        self.label_39 = QLabel(self.frame_11)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font7)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.label_39, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frame_11, 0, 0, 1, 1)

        self.int_tabWid = QTableWidget(self.frame_12)
        if (self.int_tabWid.columnCount() < 6):
            self.int_tabWid.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.int_tabWid.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.int_tabWid.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.int_tabWid.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.int_tabWid.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.int_tabWid.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.int_tabWid.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        self.int_tabWid.setObjectName(u"int_tabWid")
        self.int_tabWid.setFocusPolicy(Qt.NoFocus)
        self.int_tabWid.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-top: 1px solid red;\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1p"
                        "x solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.int_tabWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.int_tabWid.setShowGrid(False)
        self.int_tabWid.verticalHeader().setVisible(False)

        self.gridLayout_31.addWidget(self.int_tabWid, 1, 0, 1, 1)


        self.horizontalLayout_40.addWidget(self.frame_12)

        self.frame_38 = QFrame(self.frame_2)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(30, 34, 42);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_38)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setHorizontalSpacing(0)
        self.gridLayout_33.setVerticalSpacing(10)
        self.gridLayout_33.setContentsMargins(8, 0, 8, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_39)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 8, 0, 8)
        self.label_40 = QLabel(self.frame_39)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font7)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.label_40, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.frame_39, 0, 0, 1, 1)

        self.qc_tabWid = QTableWidget(self.frame_38)
        if (self.qc_tabWid.columnCount() < 6):
            self.qc_tabWid.setColumnCount(6)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.qc_tabWid.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.qc_tabWid.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.qc_tabWid.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.qc_tabWid.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.qc_tabWid.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.qc_tabWid.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        self.qc_tabWid.setObjectName(u"qc_tabWid")
        self.qc_tabWid.setFocusPolicy(Qt.NoFocus)
        self.qc_tabWid.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-top: 1px solid red;\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1p"
                        "x solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.qc_tabWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.qc_tabWid.setShowGrid(False)
        self.qc_tabWid.verticalHeader().setVisible(False)

        self.gridLayout_33.addWidget(self.qc_tabWid, 1, 0, 1, 1)


        self.horizontalLayout_40.addWidget(self.frame_38)


        self.gridLayout_37.addWidget(self.frame_2, 0, 0, 1, 1)

        self.shot_details_tabWidget.addTab(self.versions_page, "")
        self.team = QWidget()
        self.team.setObjectName(u"team")
        self.gridLayout_40 = QGridLayout(self.team)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.team)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_15)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_16)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.team_tableWid = QTableWidget(self.frame_16)
        if (self.team_tableWid.columnCount() < 10):
            self.team_tableWid.setColumnCount(10)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(8, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.team_tableWid.setHorizontalHeaderItem(9, __qtablewidgetitem38)
        self.team_tableWid.setObjectName(u"team_tableWid")
        self.team_tableWid.setFocusPolicy(Qt.NoFocus)
        self.team_tableWid.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	alternate-background-color: rgb(42, 48, 59);\n"
"}\n"
"QTableWidget::item{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(28, 32, 40);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:hor"
                        "izontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"")
        self.team_tableWid.setFrameShape(QFrame.NoFrame)
        self.team_tableWid.setFrameShadow(QFrame.Raised)
        self.team_tableWid.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.team_tableWid.setAlternatingRowColors(True)
        self.team_tableWid.setShowGrid(False)
        self.team_tableWid.verticalHeader().setVisible(False)

        self.gridLayout_38.addWidget(self.team_tableWid, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_16, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.frame_15, 0, 0, 1, 1)

        self.shot_details_tabWidget.addTab(self.team, "")

        self.horizontalLayout_6.addWidget(self.shot_details_tabWidget)


        self.gridLayout_22.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_17, 1, 0, 1, 1)


        self.gridLayout_25.addWidget(self.shot_details_top_frame, 0, 0, 1, 1)


        self.shot_details_page_2.addWidget(self.shot_details_main_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.shot_details_page)
        self.shot_upload_page = QWidget()
        self.shot_upload_page.setObjectName(u"shot_upload_page")
        self.gridLayout_43 = QGridLayout(self.shot_upload_page)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.shot_upload_frame = QFrame(self.shot_upload_page)
        self.shot_upload_frame.setObjectName(u"shot_upload_frame")
        self.shot_upload_frame.setFrameShape(QFrame.StyledPanel)
        self.shot_upload_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.shot_upload_frame)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.shot_upload_top_frame = QFrame(self.shot_upload_frame)
        self.shot_upload_top_frame.setObjectName(u"shot_upload_top_frame")
        self.shot_upload_top_frame.setFrameShape(QFrame.StyledPanel)
        self.shot_upload_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.shot_upload_top_frame)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 8, 10, 8)
        self.line_2 = QFrame(self.shot_upload_top_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(1, 16777215))
        self.line_2.setStyleSheet(u"background-color: rgb(54, 60, 74);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.sh_up_Project = QComboBox(self.shot_upload_top_frame)
        self.sh_up_Project.addItem("")
        self.sh_up_Project.setObjectName(u"sh_up_Project")
        self.sh_up_Project.setFont(font1)

        self.horizontalLayout_3.addWidget(self.sh_up_Project)

        self.line_3 = QFrame(self.shot_upload_top_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(1, 16777215))
        self.line_3.setStyleSheet(u"background-color: rgb(54, 60, 74);")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.sh_file_btn = QPushButton(self.shot_upload_top_frame)
        self.sh_file_btn.setObjectName(u"sh_file_btn")
        self.sh_file_btn.setEnabled(False)
        self.sh_file_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/16x16/icons/16x16/cil-paperclip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sh_file_btn.setIcon(icon14)
        self.sh_file_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.sh_file_btn)

        self.sh_selected_file_name = QLabel(self.shot_upload_top_frame)
        self.sh_selected_file_name.setObjectName(u"sh_selected_file_name")
        self.sh_selected_file_name.setFont(font1)

        self.horizontalLayout_3.addWidget(self.sh_selected_file_name)

        self.line_5 = QFrame(self.shot_upload_top_frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(1, 16777215))
        self.line_5.setStyleSheet(u"background-color: rgb(54, 60, 74);")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.sel_all_shots_chkBox = QCheckBox(self.shot_upload_top_frame)
        self.sel_all_shots_chkBox.setObjectName(u"sel_all_shots_chkBox")

        self.horizontalLayout_3.addWidget(self.sel_all_shots_chkBox)

        self.line_6 = QFrame(self.shot_upload_top_frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMaximumSize(QSize(1, 16777215))
        self.line_6.setStyleSheet(u"background-color: rgb(54, 60, 74);")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)

        self.sh_upload_btn = QPushButton(self.shot_upload_top_frame)
        self.sh_upload_btn.setObjectName(u"sh_upload_btn")
        self.sh_upload_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/custom/icons/custom/addtodb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sh_upload_btn.setIcon(icon15)
        self.sh_upload_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.sh_upload_btn)

        self.line_8 = QFrame(self.shot_upload_top_frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMaximumSize(QSize(1, 16777215))
        self.line_8.setStyleSheet(u"background-color: rgb(54, 60, 74);")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.sh_import_progressBar = QProgressBar(self.shot_upload_top_frame)
        self.sh_import_progressBar.setObjectName(u"sh_import_progressBar")
        self.sh_import_progressBar.setEnabled(True)
        self.sh_import_progressBar.setMinimumSize(QSize(0, 20))
        self.sh_import_progressBar.setMaximumSize(QSize(16777215, 30))
        font13 = QFont()
        font13.setFamily(u"Nirmala UI")
        font13.setPointSize(16)
        font13.setBold(True)
        font13.setWeight(75)
        self.sh_import_progressBar.setFont(font13)
        self.sh_import_progressBar.setAutoFillBackground(False)
        self.sh_import_progressBar.setStyleSheet(u"QProgressBar::chunk {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	min-height: 12px;\n"
"	max-height: 12px;\n"
"    background-color:rgb(255, 170, 0);\n"
"    width: 10px; \n"
"    margin: 1.5px;\n"
"\n"
"	border-radius: 6px;\n"
"}")
        self.sh_import_progressBar.setValue(0)
        self.sh_import_progressBar.setTextVisible(False)
        self.sh_import_progressBar.setOrientation(Qt.Horizontal)
        self.sh_import_progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_3.addWidget(self.sh_import_progressBar)


        self.gridLayout_42.addWidget(self.shot_upload_top_frame, 0, 0, 1, 1)

        self.divider = QFrame(self.shot_upload_frame)
        self.divider.setObjectName(u"divider")
        self.divider.setMaximumSize(QSize(16777215, 2))
        self.divider.setStyleSheet(u"background-color: rgb(54, 60, 74);")
        self.divider.setFrameShape(QFrame.HLine)
        self.divider.setFrameShadow(QFrame.Sunken)

        self.gridLayout_42.addWidget(self.divider, 1, 0, 1, 1)

        self.shot_upload_table_frame = QFrame(self.shot_upload_frame)
        self.shot_upload_table_frame.setObjectName(u"shot_upload_table_frame")
        self.shot_upload_table_frame.setStyleSheet(u"")
        self.shot_upload_table_frame.setFrameShape(QFrame.StyledPanel)
        self.shot_upload_table_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.shot_upload_table_frame)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.shot_import_table = QTableWidget(self.shot_upload_table_frame)
        if (self.shot_import_table.columnCount() < 13):
            self.shot_import_table.setColumnCount(13)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(6, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(7, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(8, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(9, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(10, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(11, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.shot_import_table.setHorizontalHeaderItem(12, __qtablewidgetitem51)
        self.shot_import_table.setObjectName(u"shot_import_table")
        self.shot_import_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-top: 1px solid red;\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1p"
                        "x solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.shot_import_table.setFrameShape(QFrame.NoFrame)
        self.shot_import_table.setFrameShadow(QFrame.Raised)
        self.shot_import_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.shot_import_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.shot_import_table.setShowGrid(False)
        self.shot_import_table.setSortingEnabled(True)
        self.shot_import_table.verticalHeader().setVisible(False)

        self.gridLayout_41.addWidget(self.shot_import_table, 0, 0, 1, 1)


        self.gridLayout_42.addWidget(self.shot_upload_table_frame, 2, 0, 1, 1)


        self.gridLayout_43.addWidget(self.shot_upload_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.shot_upload_page)
        self.all_shots_page = QWidget()
        self.all_shots_page.setObjectName(u"all_shots_page")
        self.gridLayout_46 = QGridLayout(self.all_shots_page)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.all_shots_page)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_20)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setHorizontalSpacing(7)
        self.gridLayout_45.setVerticalSpacing(0)
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.filter_frame = QFrame(self.frame_20)
        self.filter_frame.setObjectName(u"filter_frame")
        self.filter_frame.setMinimumSize(QSize(300, 0))
        self.filter_frame.setMaximumSize(QSize(500, 16777215))
        self.filter_frame.setStyleSheet(u"QFrame#filter_frame {border:2px solid  rgb(54, 60, 74);\n"
"border-radius:5px;\n"
"}")
        self.filter_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_65 = QGridLayout(self.filter_frame)
        self.gridLayout_65.setSpacing(0)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(5, 5, 5, 5)
        self.frame_43 = QFrame(self.filter_frame)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"color: rgb(193, 193, 193);")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_43)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(0)
        self.gridLayout_17.setVerticalSpacing(7)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_44)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setHorizontalSpacing(0)
        self.gridLayout_44.setVerticalSpacing(5)
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.sel_all_shtTable_chkBox = QCheckBox(self.frame_44)
        self.sel_all_shtTable_chkBox.setObjectName(u"sel_all_shtTable_chkBox")
        self.sel_all_shtTable_chkBox.setFont(font1)

        self.gridLayout_44.addWidget(self.sel_all_shtTable_chkBox, 1, 0, 1, 1)

        self.assign_leads_btn = QPushButton(self.frame_44)
        self.assign_leads_btn.setObjectName(u"assign_leads_btn")
        self.assign_leads_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.assign_leads_btn.setStyleSheet(u"QPushButton{\n"
"padding:5px;\n"
"background-color: rgb(230, 123, 0);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(230, 149, 9);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(208, 111, 0);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/24x24/icons/24x24/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.assign_leads_btn.setIcon(icon16)
        self.assign_leads_btn.setIconSize(QSize(20, 20))
        self.assign_leads_btn.setFlat(True)

        self.gridLayout_44.addWidget(self.assign_leads_btn, 1, 1, 1, 1)

        self.shot_search_lineEdit = QLineEdit(self.frame_44)
        self.shot_search_lineEdit.setObjectName(u"shot_search_lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.shot_search_lineEdit.sizePolicy().hasHeightForWidth())
        self.shot_search_lineEdit.setSizePolicy(sizePolicy5)
        self.shot_search_lineEdit.setMinimumSize(QSize(0, 34))
        self.shot_search_lineEdit.setFont(font5)
        self.shot_search_lineEdit.setFrame(True)

        self.gridLayout_44.addWidget(self.shot_search_lineEdit, 0, 0, 1, 2)


        self.gridLayout_17.addWidget(self.frame_44, 0, 0, 1, 1)

        self.line_9 = QFrame(self.frame_43)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_17.addWidget(self.line_9, 5, 0, 1, 1)

        self.stat_filter_cb = CustomComboBox(self.frame_43)
        self.stat_filter_cb.addItem("")
        self.stat_filter_cb.addItem("")
        self.stat_filter_cb.addItem("")
        self.stat_filter_cb.setObjectName(u"stat_filter_cb")
        self.stat_filter_cb.setFont(font1)

        self.gridLayout_17.addWidget(self.stat_filter_cb, 7, 0, 1, 1)

        self.line_14 = QFrame(self.frame_43)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_17.addWidget(self.line_14, 9, 0, 1, 1)

        self.pro_filter_cb = CustomComboBox(self.frame_43)
        self.pro_filter_cb.addItem("")
        self.pro_filter_cb.addItem("")
        self.pro_filter_cb.addItem("")
        self.pro_filter_cb.setObjectName(u"pro_filter_cb")
        self.pro_filter_cb.setFont(font1)

        self.gridLayout_17.addWidget(self.pro_filter_cb, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_4, 8, 0, 1, 1)


        self.gridLayout_65.addWidget(self.frame_43, 0, 0, 1, 1)

        self.frame_45 = QFrame(self.filter_frame)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_45)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setVerticalSpacing(7)
        self.gridLayout_29.setContentsMargins(5, 5, 5, 5)
        self.set_default_btn = QPushButton(self.frame_45)
        self.set_default_btn.setObjectName(u"set_default_btn")
        self.set_default_btn.setMinimumSize(QSize(30, 30))
        font14 = QFont()
        font14.setFamily(u"Segoe UI")
        font14.setPointSize(8)
        font14.setBold(True)
        font14.setWeight(75)
        self.set_default_btn.setFont(font14)
        self.set_default_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/24x24/icons/24x24/cil-camera-roll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.set_default_btn.setIcon(icon17)
        self.set_default_btn.setIconSize(QSize(13, 13))

        self.gridLayout_29.addWidget(self.set_default_btn, 1, 0, 1, 2)

        self.clear_filter_btn = QPushButton(self.frame_45)
        self.clear_filter_btn.setObjectName(u"clear_filter_btn")
        self.clear_filter_btn.setMinimumSize(QSize(80, 30))
        font15 = QFont()
        font15.setPointSize(8)
        font15.setBold(True)
        font15.setWeight(75)
        self.clear_filter_btn.setFont(font15)
        self.clear_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/24x24/icons/24x24/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_filter_btn.setIcon(icon18)
        self.clear_filter_btn.setIconSize(QSize(13, 13))

        self.gridLayout_29.addWidget(self.clear_filter_btn, 0, 1, 1, 1)

        self.apply_filter_btn = QPushButton(self.frame_45)
        self.apply_filter_btn.setObjectName(u"apply_filter_btn")
        self.apply_filter_btn.setMinimumSize(QSize(80, 30))
        self.apply_filter_btn.setFont(font14)
        self.apply_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/24x24/icons/24x24/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.apply_filter_btn.setIcon(icon19)
        self.apply_filter_btn.setIconSize(QSize(13, 13))

        self.gridLayout_29.addWidget(self.apply_filter_btn, 0, 0, 1, 1)


        self.gridLayout_65.addWidget(self.frame_45, 1, 0, 1, 1)


        self.gridLayout_45.addWidget(self.filter_frame, 1, 1, 1, 1)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_22)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.all_shots_tbWidget = QTableWidget(self.frame_22)
        if (self.all_shots_tbWidget.columnCount() < 17):
            self.all_shots_tbWidget.setColumnCount(17)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(5, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(6, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(7, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(8, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(9, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(10, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(11, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(12, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(13, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(14, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(15, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.all_shots_tbWidget.setHorizontalHeaderItem(16, __qtablewidgetitem68)
        self.all_shots_tbWidget.setObjectName(u"all_shots_tbWidget")
        self.all_shots_tbWidget.setFont(font1)
        self.all_shots_tbWidget.setFocusPolicy(Qt.NoFocus)
        self.all_shots_tbWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	alternate-background-color: rgb(42, 48, 59);\n"
"}\n"
"QTableWidget::item{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(94, 94, 94);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
""
                        "}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"")
        self.all_shots_tbWidget.setFrameShape(QFrame.NoFrame)
        self.all_shots_tbWidget.setFrameShadow(QFrame.Sunken)
        self.all_shots_tbWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.all_shots_tbWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.all_shots_tbWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.all_shots_tbWidget.setAlternatingRowColors(True)
        self.all_shots_tbWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.all_shots_tbWidget.setShowGrid(False)
        self.all_shots_tbWidget.setSortingEnabled(False)
        self.all_shots_tbWidget.verticalHeader().setVisible(False)
        self.all_shots_tbWidget.verticalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_32.addWidget(self.all_shots_tbWidget, 0, 0, 1, 1)


        self.gridLayout_45.addWidget(self.frame_22, 0, 0, 2, 1)


        self.gridLayout_46.addWidget(self.frame_20, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.all_shots_page)
        self.my_task_page = QWidget()
        self.my_task_page.setObjectName(u"my_task_page")
        self.gridLayout_50 = QGridLayout(self.my_task_page)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.my_task_page)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_23)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.all_shots_topFrame_2 = QFrame(self.frame_23)
        self.all_shots_topFrame_2.setObjectName(u"all_shots_topFrame_2")
        self.all_shots_topFrame_2.setFrameShape(QFrame.StyledPanel)
        self.all_shots_topFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.all_shots_topFrame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.t_cli_sel_cb = QComboBox(self.all_shots_topFrame_2)
        self.t_cli_sel_cb.addItem("")
        self.t_cli_sel_cb.setObjectName(u"t_cli_sel_cb")
        self.t_cli_sel_cb.setFont(font1)

        self.horizontalLayout_11.addWidget(self.t_cli_sel_cb)

        self.t_pro_sel_cb = QComboBox(self.all_shots_topFrame_2)
        self.t_pro_sel_cb.addItem("")
        self.t_pro_sel_cb.setObjectName(u"t_pro_sel_cb")
        self.t_pro_sel_cb.setFont(font1)

        self.horizontalLayout_11.addWidget(self.t_pro_sel_cb)

        self.t_status_sel_cb = QComboBox(self.all_shots_topFrame_2)
        self.t_status_sel_cb.addItem("")
        self.t_status_sel_cb.setObjectName(u"t_status_sel_cb")
        self.t_status_sel_cb.setMinimumSize(QSize(150, 0))
        self.t_status_sel_cb.setFont(font1)

        self.horizontalLayout_11.addWidget(self.t_status_sel_cb)

        self.task_search_lineEdit = QLineEdit(self.all_shots_topFrame_2)
        self.task_search_lineEdit.setObjectName(u"task_search_lineEdit")
        self.task_search_lineEdit.setMinimumSize(QSize(0, 34))
        self.task_search_lineEdit.setFont(font5)
        self.task_search_lineEdit.setStyleSheet(u"")
        self.task_search_lineEdit.setFrame(True)

        self.horizontalLayout_11.addWidget(self.task_search_lineEdit)

        self.task_search_btn = QPushButton(self.all_shots_topFrame_2)
        self.task_search_btn.setObjectName(u"task_search_btn")
        self.task_search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u":/16x16/icons/16x16/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_search_btn.setIcon(icon20)
        self.task_search_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.task_search_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)


        self.gridLayout_49.addWidget(self.all_shots_topFrame_2, 0, 0, 1, 1)

        self.line_11 = QFrame(self.frame_23)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMaximumSize(QSize(16777215, 2))
        self.line_11.setStyleSheet(u"background-color: rgb(54, 60, 74);")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_49.addWidget(self.line_11, 1, 0, 1, 1)

        self.task_tabWid = QTabWidget(self.frame_23)
        self.task_tabWid.setObjectName(u"task_tabWid")
        self.task_tabWid.setFont(font1)
        self.task_tabWid.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 2px solid rgb(44, 49, 60);\n"
"}\n"
"QTabWidget::tab-bar {\n"
"left:5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"border-top-left-radius: 2px;\n"
"border-top-right-radius: 2px;\n"
"padding: 10px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"color: rgb(191, 127, 0);\n"
"border-bottom: 1px solid rgba(247, 128, 23,0.5); /* same as pane color */ \n"
"}\n"
"QTabBar::tab:hover {\n"
"color: rgba(191, 127, 0,0.5);\n"
"border-bottom: 1px solid rgba(247, 128, 23,0.2); /* same as pane color */ \n"
"}\n"
"")
        self.pending_task = QWidget()
        self.pending_task.setObjectName(u"pending_task")
        self.gridLayout_48 = QGridLayout(self.pending_task)
        self.gridLayout_48.setSpacing(0)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.task_pending_tableWid = QTableWidget(self.pending_task)
        if (self.task_pending_tableWid.columnCount() < 12):
            self.task_pending_tableWid.setColumnCount(12)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(3, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(4, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(5, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(6, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(7, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(8, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(9, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(10, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.task_pending_tableWid.setHorizontalHeaderItem(11, __qtablewidgetitem80)
        self.task_pending_tableWid.setObjectName(u"task_pending_tableWid")
        self.task_pending_tableWid.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	alternate-background-color: rgb(42, 48, 59);\n"
"}\n"
"QTableWidget::item{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(28, 32, 40);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:hor"
                        "izontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"")
        self.task_pending_tableWid.setFrameShape(QFrame.NoFrame)
        self.task_pending_tableWid.setFrameShadow(QFrame.Raised)
        self.task_pending_tableWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.task_pending_tableWid.setAlternatingRowColors(True)
        self.task_pending_tableWid.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.task_pending_tableWid.setShowGrid(False)
        self.task_pending_tableWid.setSortingEnabled(True)
        self.task_pending_tableWid.horizontalHeader().setCascadingSectionResizes(True)
        self.task_pending_tableWid.horizontalHeader().setStretchLastSection(True)
        self.task_pending_tableWid.verticalHeader().setVisible(False)

        self.gridLayout_48.addWidget(self.task_pending_tableWid, 0, 0, 1, 1)

        self.task_tabWid.addTab(self.pending_task, "")
        self.completed = QWidget()
        self.completed.setObjectName(u"completed")
        self.gridLayout_52 = QGridLayout(self.completed)
        self.gridLayout_52.setSpacing(0)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.task_completed_tableWid = QTableWidget(self.completed)
        if (self.task_completed_tableWid.columnCount() < 12):
            self.task_completed_tableWid.setColumnCount(12)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(2, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(3, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(4, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(5, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(6, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(7, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(8, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(9, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(10, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.task_completed_tableWid.setHorizontalHeaderItem(11, __qtablewidgetitem92)
        self.task_completed_tableWid.setObjectName(u"task_completed_tableWid")
        self.task_completed_tableWid.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	alternate-background-color: rgb(42, 48, 59);\n"
"}\n"
"QTableWidget::item{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(28, 32, 40);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:hor"
                        "izontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"")
        self.task_completed_tableWid.setFrameShape(QFrame.NoFrame)
        self.task_completed_tableWid.setFrameShadow(QFrame.Raised)
        self.task_completed_tableWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.task_completed_tableWid.setAlternatingRowColors(True)
        self.task_completed_tableWid.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.task_completed_tableWid.setShowGrid(False)
        self.task_completed_tableWid.setSortingEnabled(True)
        self.task_completed_tableWid.verticalHeader().setVisible(False)

        self.gridLayout_52.addWidget(self.task_completed_tableWid, 0, 0, 1, 1)

        self.task_tabWid.addTab(self.completed, "")

        self.gridLayout_49.addWidget(self.task_tabWid, 2, 0, 1, 1)


        self.gridLayout_50.addWidget(self.frame_23, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.my_task_page)
        self.reports_page = QWidget()
        self.reports_page.setObjectName(u"reports_page")
        self.gridLayout_28 = QGridLayout(self.reports_page)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.browser_layout = QGridLayout()
        self.browser_layout.setObjectName(u"browser_layout")
        self.browser_layout.setContentsMargins(7, 7, 7, 7)
        self.frame_6 = QFrame(self.reports_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(216, 143, 80);\n"
"	background-color: rgb(243, 159, 90);\n"
"	border-radius:10px;\n"
"	margin:5px;\n"
"}\n"
"QLabel{\n"
"	background-color:None;\n"
"	border:0px;\n"
"	color:white\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(11, -1, -1, -1)
        self.sr_shows_lbl = QLabel(self.frame_6)
        self.sr_shows_lbl.setObjectName(u"sr_shows_lbl")
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        font16.setPointSize(59)
        self.sr_shows_lbl.setFont(font16)
        self.sr_shows_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.sr_shows_lbl)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font6)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_21)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_20)


        self.browser_layout.addWidget(self.frame_6, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.browser_layout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.frame_30 = QFrame(self.reports_page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(144, 96, 0);\n"
"	border-radius:10px;\n"
"	margin:5px;\n"
"}\n"
"QLabel{\n"
"	background-color:None;\n"
"	border:0px;\n"
"	color:white\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_30)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sr_delta_lbl = QLabel(self.frame_30)
        self.sr_delta_lbl.setObjectName(u"sr_delta_lbl")
        self.sr_delta_lbl.setFont(font16)
        self.sr_delta_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.sr_delta_lbl)

        self.label_32 = QLabel(self.frame_30)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font6)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_32)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_15.addItem(self.horizontalSpacer_24)


        self.browser_layout.addWidget(self.frame_30, 1, 5, 1, 1)

        self.frame_29 = QFrame(self.reports_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(189, 126, 94);\n"
"	border-radius:10px;\n"
"	margin:5px;\n"
"}\n"
"QLabel{\n"
"	background-color:None;\n"
"	border:0px;\n"
"	color:white\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_29)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sr_ach_mandays_lbl = QLabel(self.frame_29)
        self.sr_ach_mandays_lbl.setObjectName(u"sr_ach_mandays_lbl")
        self.sr_ach_mandays_lbl.setFont(font16)
        self.sr_ach_mandays_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.sr_ach_mandays_lbl)

        self.label_28 = QLabel(self.frame_29)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font6)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_28.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_28)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_14.addItem(self.horizontalSpacer_23)


        self.browser_layout.addWidget(self.frame_29, 1, 4, 1, 1)

        self.frame_4 = QFrame(self.reports_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(157, 137, 211);\n"
"	background-color: rgb(170, 149, 229);\n"
"	border-radius:10px;\n"
"	margin:5px;\n"
"}\n"
"QLabel{\n"
"	background-color:None;\n"
"	border:0px;\n"
"	color:white\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sr_clients_lbl = QLabel(self.frame_4)
        self.sr_clients_lbl.setObjectName(u"sr_clients_lbl")
        self.sr_clients_lbl.setFont(font16)
        self.sr_clients_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.sr_clients_lbl)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_11)


        self.browser_layout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.reports_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(97, 152, 114);\n"
"	border-radius:10px;\n"
"	margin:5px;\n"
"}\n"
"QLabel{\n"
"	background-color:None;\n"
"	border:0px;\n"
"	color:white\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sr_actmandays_lbl = QLabel(self.frame_10)
        self.sr_actmandays_lbl.setObjectName(u"sr_actmandays_lbl")
        self.sr_actmandays_lbl.setFont(font16)
        self.sr_actmandays_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.sr_actmandays_lbl)

        self.label_26 = QLabel(self.frame_10)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font6)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_26)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_22)


        self.browser_layout.addWidget(self.frame_10, 1, 3, 1, 1)

        self.frame_34 = QFrame(self.reports_page)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_31 = QFrame(self.frame_34)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_31)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.frame_31)
        self.label_13.setObjectName(u"label_13")
        font17 = QFont()
        font17.setFamily(u"Segoe UI")
        font17.setPointSize(13)
        font17.setBold(True)
        font17.setWeight(75)
        self.label_13.setFont(font17)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_13)

        self.sr_yts_lbl = QLabel(self.frame_31)
        self.sr_yts_lbl.setObjectName(u"sr_yts_lbl")
        font18 = QFont()
        font18.setFamily(u"Segoe UI")
        font18.setPointSize(30)
        self.sr_yts_lbl.setFont(font18)
        self.sr_yts_lbl.setStyleSheet(u"color: rgb(85, 85, 255);")
        self.sr_yts_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.sr_yts_lbl)


        self.horizontalLayout_38.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_34)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_32)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_18 = QLabel(self.frame_32)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font17)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_18)

        self.sr_wip_lbl = QLabel(self.frame_32)
        self.sr_wip_lbl.setObjectName(u"sr_wip_lbl")
        self.sr_wip_lbl.setFont(font18)
        self.sr_wip_lbl.setStyleSheet(u"color: rgb(255, 170, 0);")
        self.sr_wip_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.sr_wip_lbl)


        self.horizontalLayout_38.addWidget(self.frame_32)

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_35)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_20 = QLabel(self.frame_35)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font17)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_20)

        self.sr_rtk_lbl = QLabel(self.frame_35)
        self.sr_rtk_lbl.setObjectName(u"sr_rtk_lbl")
        self.sr_rtk_lbl.setFont(font18)
        self.sr_rtk_lbl.setStyleSheet(u"color: rgb(222, 54, 20);")
        self.sr_rtk_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.sr_rtk_lbl)


        self.horizontalLayout_38.addWidget(self.frame_35)

        self.frame_33 = QFrame(self.frame_34)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_33)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_19 = QLabel(self.frame_33)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font17)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_19)

        self.sr_cmp_lbl = QLabel(self.frame_33)
        self.sr_cmp_lbl.setObjectName(u"sr_cmp_lbl")
        self.sr_cmp_lbl.setFont(font18)
        self.sr_cmp_lbl.setStyleSheet(u"color: rgb(85, 170, 0);")
        self.sr_cmp_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.sr_cmp_lbl)


        self.horizontalLayout_38.addWidget(self.frame_33)


        self.browser_layout.addWidget(self.frame_34, 2, 0, 1, 6)

        self.frame_9 = QFrame(self.reports_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(76, 115, 173);\n"
"	border-radius:10px;\n"
"	margin:5px;\n"
"}\n"
"QLabel{\n"
"	background-color:None;\n"
"	border:0px;\n"
"	color:white\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.sr_shots_lbl = QLabel(self.frame_9)
        self.sr_shots_lbl.setObjectName(u"sr_shots_lbl")
        self.sr_shots_lbl.setFont(font16)
        self.sr_shots_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.sr_shots_lbl)

        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_24)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_21)


        self.browser_layout.addWidget(self.frame_9, 1, 2, 1, 1)

        self.frame_36 = QFrame(self.reports_page)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 100))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_37 = QLabel(self.frame_36)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font18)

        self.horizontalLayout_39.addWidget(self.label_37)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_3)

        self.sr_download_btn = QPushButton(self.frame_36)
        self.sr_download_btn.setObjectName(u"sr_download_btn")
        font19 = QFont()
        font19.setPointSize(10)
        font19.setBold(True)
        font19.setWeight(75)
        self.sr_download_btn.setFont(font19)
        self.sr_download_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sr_download_btn.setStyleSheet(u"QPushButton{\n"
"padding:8px;\n"
"background-color: rgb(230, 123, 0);\n"
"color:white\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(230, 149, 9);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(208, 111, 0);\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/20x20/icons/20x20/cil-arrow-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sr_download_btn.setIcon(icon21)

        self.horizontalLayout_39.addWidget(self.sr_download_btn)


        self.browser_layout.addWidget(self.frame_36, 0, 0, 1, 6)


        self.gridLayout_28.addLayout(self.browser_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.reports_page)
        self.change_password_page = QWidget()
        self.change_password_page.setObjectName(u"change_password_page")
        self.gridLayout_36 = QGridLayout(self.change_password_page)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.frame_40 = QFrame(self.change_password_page)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(751, 341))
        self.frame_40.setMaximumSize(QSize(751, 341))
        self.frame_40.setCursor(QCursor(Qt.OpenHandCursor))
        self.frame_40.setStyleSheet(u"QFrame{border:2px solid orange; border-radius:5px}")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_63 = QGridLayout(self.frame_40)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(411, 291))
        self.frame_41.setMaximumSize(QSize(411, 291))
        self.frame_41.setStyleSheet(u"QFrame{border:None;}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_41)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.new_pwd1_le = QLineEdit(self.frame_41)
        self.new_pwd1_le.setObjectName(u"new_pwd1_le")
        self.new_pwd1_le.setMinimumSize(QSize(0, 40))
        self.new_pwd1_le.setFont(font5)
        self.new_pwd1_le.setEchoMode(QLineEdit.Password)

        self.gridLayout_35.addWidget(self.new_pwd1_le, 5, 1, 1, 3)

        self.new_pwd2_le = QLineEdit(self.frame_41)
        self.new_pwd2_le.setObjectName(u"new_pwd2_le")
        self.new_pwd2_le.setMinimumSize(QSize(0, 40))
        self.new_pwd2_le.setFont(font5)
        self.new_pwd2_le.setEchoMode(QLineEdit.Password)

        self.gridLayout_35.addWidget(self.new_pwd2_le, 6, 1, 1, 3)

        self.change_butt = QPushButton(self.frame_41)
        self.change_butt.setObjectName(u"change_butt")
        self.change_butt.setMaximumSize(QSize(231, 28))
        self.change_butt.setFont(font5)
        self.change_butt.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_butt.setStyleSheet(u"background-color: rgb(214, 71, 0);")

        self.gridLayout_35.addWidget(self.change_butt, 7, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_35.addItem(self.verticalSpacer_2, 8, 2, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_28, 7, 1, 1, 1)

        self.label_25 = QLabel(self.frame_41)
        self.label_25.setObjectName(u"label_25")
        font20 = QFont()
        font20.setPointSize(14)
        self.label_25.setFont(font20)
        self.label_25.setStyleSheet(u"border: None;")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_35.addWidget(self.label_25, 0, 2, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_25, 7, 0, 1, 1)

        self.old_pwd_le = QLineEdit(self.frame_41)
        self.old_pwd_le.setObjectName(u"old_pwd_le")
        self.old_pwd_le.setMinimumSize(QSize(0, 40))
        self.old_pwd_le.setFont(font5)
        self.old_pwd_le.setEchoMode(QLineEdit.Password)

        self.gridLayout_35.addWidget(self.old_pwd_le, 2, 1, 1, 3)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_26, 7, 3, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_27, 7, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_35.addItem(self.verticalSpacer_3, 1, 2, 1, 1)


        self.gridLayout_63.addWidget(self.frame_41, 0, 0, 1, 1)


        self.gridLayout_36.addWidget(self.frame_40, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.change_password_page)

        self.gridLayout_13.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.content_frame, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.center_right_frame, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.center_frame, 1, 0, 1, 1)


        self.centralLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.shot_details_tabWidget.setCurrentIndex(0)
        self.dep_tabWidget.setCurrentIndex(0)
        self.task_tabWid.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TENDRILL", None))
        self.label_title_bar_top.setText("")
#if QT_CONFIG(tooltip)
        self.clients_pb.setToolTip(QCoreApplication.translate("MainWindow", u"Clients", None))
#endif // QT_CONFIG(tooltip)
        self.clients_pb.setText("")
#if QT_CONFIG(tooltip)
        self.shots_ingest_pb.setToolTip(QCoreApplication.translate("MainWindow", u"Shots Ingest", None))
#endif // QT_CONFIG(tooltip)
        self.shots_ingest_pb.setText("")
#if QT_CONFIG(tooltip)
        self.all_shots_pb.setToolTip(QCoreApplication.translate("MainWindow", u"All Shots", None))
#endif // QT_CONFIG(tooltip)
        self.all_shots_pb.setText("")
#if QT_CONFIG(tooltip)
        self.my_task_pb.setToolTip(QCoreApplication.translate("MainWindow", u"My Task", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.refresh_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_btn.setText("")
#if QT_CONFIG(tooltip)
        self.chng_pwd_pb.setToolTip(QCoreApplication.translate("MainWindow", u"Change Password", None))
#endif // QT_CONFIG(tooltip)
        self.chng_pwd_pb.setText("")
#if QT_CONFIG(tooltip)
        self.log_out_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Log Out", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"V03.5262", None))
        self.label_3.setText("")
        self.clients_label.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
#if QT_CONFIG(tooltip)
        self.cli_add_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Add Client", None))
#endif // QT_CONFIG(tooltip)
        self.cli_add_btn.setText("")
        ___qtablewidgetitem = self.cli_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem1 = self.cli_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"COUNTRY", None));
        ___qtablewidgetitem2 = self.cli_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOCALITY", None));
        ___qtablewidgetitem3 = self.cli_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.cli_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.cli_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.cli_table.isSortingEnabled()
        self.cli_table.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.cli_table.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qtablewidgetitem7 = self.cli_table.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qtablewidgetitem8 = self.cli_table.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qtablewidgetitem9 = self.cli_table.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qtablewidgetitem10 = self.cli_table.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qtablewidgetitem11 = self.cli_table.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qtablewidgetitem12 = self.cli_table.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qtablewidgetitem13 = self.cli_table.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qtablewidgetitem14 = self.cli_table.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        self.cli_table.setSortingEnabled(__sortingEnabled)

        self.label_4.setText("")
        self.pro_label.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
#if QT_CONFIG(tooltip)
        self.pro_add_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Add Project", None))
#endif // QT_CONFIG(tooltip)
        self.pro_add_btn.setText("")
        ___qtablewidgetitem15 = self.pro_table.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"CLIENT", None));
        ___qtablewidgetitem16 = self.pro_table.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"PROJECT", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Shot:", None))
        self.shotName_lbl.setText(QCoreApplication.translate("MainWindow", u"Shot name", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.status_btn.setText(QCoreApplication.translate("MainWindow", u"WIP", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Client:", None))
        self.clientName_lbl.setText(QCoreApplication.translate("MainWindow", u"client", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"ETA:", None))
        self.eta_lbl.setText(QCoreApplication.translate("MainWindow", u"eta", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Project:", None))
        self.projectName_lbl.setText(QCoreApplication.translate("MainWindow", u"project", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Start Date:", None))
        self.startDate_lbl.setText(QCoreApplication.translate("MainWindow", u"start date       ", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"End Date:", None))
        self.endDate_lbl.setText(QCoreApplication.translate("MainWindow", u"end date", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Total Bids:", None))
        self.totalBids_lbl.setText(QCoreApplication.translate("MainWindow", u"total Bids", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Sequence:", None))
        self.seqName_lbl.setText(QCoreApplication.translate("MainWindow", u"sequence", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Frame In:", None))
        self.frameIn_lbl.setText(QCoreApplication.translate("MainWindow", u"frame in", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Frame Out:", None))
        self.frameOut_lbl.setText(QCoreApplication.translate("MainWindow", u"frame out", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.totalFrames_lbl.setText(QCoreApplication.translate("MainWindow", u"total", None))
        self.input_label_2.setText(QCoreApplication.translate("MainWindow", u"Task Annotations", None))
        self.input_label_3.setText(QCoreApplication.translate("MainWindow", u"Feedback Annotations", None))
        self.shot_details_tabWidget.setTabText(self.shot_details_tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"ANNOTATIONS", None))
        self.scripts_label.setText(QCoreApplication.translate("MainWindow", u"S\n"
"C\n"
"R\n"
"I\n"
"P\n"
"T\n"
"S", None))
        ___qtreewidgetitem = self.Pscripts_treeWid.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.preren_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>O</p><p>U</p><p>T</p><p>P</p><p>U</p><p>T</p></body></html>", None))
        ___qtreewidgetitem1 = self.Poutput_treeWid.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.dep_tabWidget.setTabText(self.dep_tabWidget.indexOf(self.paint_tab), QCoreApplication.translate("MainWindow", u"PAINT", None))
        self.scripts_label_2.setText(QCoreApplication.translate("MainWindow", u"S\n"
"C\n"
"R\n"
"I\n"
"P\n"
"T\n"
"S", None))
        ___qtreewidgetitem2 = self.Rscripts_treeWid.headerItem()
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.preren_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>O</p><p>U</p><p>T</p><p>P</p><p>U</p><p>T</p></body></html>", None))
        ___qtreewidgetitem3 = self.Routput_treeWid.headerItem()
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.dep_tabWidget.setTabText(self.dep_tabWidget.indexOf(self.roto_tab), QCoreApplication.translate("MainWindow", u"ROTO", None))
        self.scripts_label_3.setText(QCoreApplication.translate("MainWindow", u"S\n"
"C\n"
"R\n"
"I\n"
"P\n"
"T\n"
"S", None))
        ___qtreewidgetitem4 = self.Mscripts_treeWid.headerItem()
        ___qtreewidgetitem4.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.preren_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>O</p><p>U</p><p>T</p><p>P</p><p>U</p><p>T</p></body></html>", None))
        ___qtreewidgetitem5 = self.Moutput_treeWid.headerItem()
        ___qtreewidgetitem5.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.dep_tabWidget.setTabText(self.dep_tabWidget.indexOf(self.mm_tab), QCoreApplication.translate("MainWindow", u"MM", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"I\n"
"N\n"
"P\n"
"U\n"
"T\n"
"S", None))

        __sortingEnabled1 = self.input_TreeWid.isSortingEnabled()
        self.input_TreeWid.setSortingEnabled(False)
        ___qtreewidgetitem6 = self.input_TreeWid.topLevelItem(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"news", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"fsdjfhh", None));
        ___qtreewidgetitem8 = self.input_TreeWid.topLevelItem(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"slkjfkjf", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"sdgsdg", None));
        self.input_TreeWid.setSortingEnabled(__sortingEnabled1)

        self.text_type_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here...", None))
        self.send_btn.setText("")
        self.dis_label.setText(QCoreApplication.translate("MainWindow", u"CHAT BOX", None))
        self.shot_details_tabWidget.setTabText(self.shot_details_tabWidget.indexOf(self.assests), QCoreApplication.translate("MainWindow", u"FILES MANAGER", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Lead Version", None))
        ___qtablewidgetitem17 = self.int_tabWid.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"VERSION", None));
        ___qtablewidgetitem18 = self.int_tabWid.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"SENT BY", None));
        ___qtablewidgetitem19 = self.int_tabWid.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"SENT DATE", None));
        ___qtablewidgetitem20 = self.int_tabWid.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem21 = self.int_tabWid.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"VERIFIED BY", None));
        ___qtablewidgetitem22 = self.int_tabWid.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"VERIFIED DATE", None));
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Qc Version", None))
        ___qtablewidgetitem23 = self.qc_tabWid.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"VERSION", None));
        ___qtablewidgetitem24 = self.qc_tabWid.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"SENT BY", None));
        ___qtablewidgetitem25 = self.qc_tabWid.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"SENT DATE", None));
        ___qtablewidgetitem26 = self.qc_tabWid.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem27 = self.qc_tabWid.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"VERIFIED BY", None));
        ___qtablewidgetitem28 = self.qc_tabWid.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"VERIFIED DATE", None));
        self.shot_details_tabWidget.setTabText(self.shot_details_tabWidget.indexOf(self.versions_page), QCoreApplication.translate("MainWindow", u"VERSIONS", None))
        ___qtablewidgetitem29 = self.team_tableWid.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"ARTIST", None));
        ___qtablewidgetitem30 = self.team_tableWid.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem31 = self.team_tableWid.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"BID DAYS", None));
        ___qtablewidgetitem32 = self.team_tableWid.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"PROGRESS", None));
        ___qtablewidgetitem33 = self.team_tableWid.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"COMPILER", None));
        ___qtablewidgetitem34 = self.team_tableWid.horizontalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"ASSIGNED DATE", None));
        ___qtablewidgetitem35 = self.team_tableWid.horizontalHeaderItem(6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
        ___qtablewidgetitem36 = self.team_tableWid.horizontalHeaderItem(7)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"START DATE", None));
        ___qtablewidgetitem37 = self.team_tableWid.horizontalHeaderItem(8)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"COMPLETED DATE", None));
        ___qtablewidgetitem38 = self.team_tableWid.horizontalHeaderItem(9)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"ACTIONS", None));
        self.shot_details_tabWidget.setTabText(self.shot_details_tabWidget.indexOf(self.team), QCoreApplication.translate("MainWindow", u"ASSIGNEES", None))
        self.sh_up_Project.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Project", None))

#if QT_CONFIG(tooltip)
        self.sh_up_Project.setToolTip(QCoreApplication.translate("MainWindow", u"Select Project", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sh_file_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
#endif // QT_CONFIG(tooltip)
        self.sh_file_btn.setText("")
        self.sh_selected_file_name.setText("")
#if QT_CONFIG(tooltip)
        self.sel_all_shots_chkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Select All Shots", None))
#endif // QT_CONFIG(tooltip)
        self.sel_all_shots_chkBox.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
#if QT_CONFIG(tooltip)
        self.sh_upload_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Add data to DB", None))
#endif // QT_CONFIG(tooltip)
        self.sh_upload_btn.setText("")
        ___qtablewidgetitem39 = self.shot_import_table.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"SEQUENCE", None));
        ___qtablewidgetitem40 = self.shot_import_table.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"SHOT", None));
        ___qtablewidgetitem41 = self.shot_import_table.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        ___qtablewidgetitem42 = self.shot_import_table.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"FRAME IN", None));
        ___qtablewidgetitem43 = self.shot_import_table.horizontalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"FRAME OUT", None));
        ___qtablewidgetitem44 = self.shot_import_table.horizontalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"TOTAL FRAMES", None));
        ___qtablewidgetitem45 = self.shot_import_table.horizontalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
        ___qtablewidgetitem46 = self.shot_import_table.horizontalHeaderItem(8)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"BID DAYS", None));
        ___qtablewidgetitem47 = self.shot_import_table.horizontalHeaderItem(9)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"PACKAGE ID", None));
        ___qtablewidgetitem48 = self.shot_import_table.horizontalHeaderItem(10)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"ESTIMATE ID", None));
        ___qtablewidgetitem49 = self.shot_import_table.horizontalHeaderItem(11)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"ESTIMATE DATE", None));
        ___qtablewidgetitem50 = self.shot_import_table.horizontalHeaderItem(12)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"RESULT", None));
        self.sel_all_shtTable_chkBox.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
#if QT_CONFIG(tooltip)
        self.assign_leads_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Assign to Leads", None))
#endif // QT_CONFIG(tooltip)
        self.assign_leads_btn.setText("")
        self.shot_search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Shot Name...", None))
        self.stat_filter_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Status", None))
        self.stat_filter_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Status2", None))
        self.stat_filter_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"Status3", None))

        self.pro_filter_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Project01", None))
        self.pro_filter_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Project02", None))
        self.pro_filter_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"Project03", None))

        self.set_default_btn.setText(QCoreApplication.translate("MainWindow", u"Set Defaults", None))
        self.clear_filter_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.apply_filter_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        ___qtablewidgetitem51 = self.all_shots_tbWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"CLIENT", None));
        ___qtablewidgetitem52 = self.all_shots_tbWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"PROJECT", None));
        ___qtablewidgetitem53 = self.all_shots_tbWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"SEQUENCE", None));
        ___qtablewidgetitem54 = self.all_shots_tbWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"SHOT", None));
        ___qtablewidgetitem55 = self.all_shots_tbWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"DEPT", None));
        ___qtablewidgetitem56 = self.all_shots_tbWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem57 = self.all_shots_tbWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"ARTIST", None));
        ___qtablewidgetitem58 = self.all_shots_tbWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"TEAM LEAD", None));
        ___qtablewidgetitem59 = self.all_shots_tbWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"CUT IN", None));
        ___qtablewidgetitem60 = self.all_shots_tbWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"CUT OUT", None));
        ___qtablewidgetitem61 = self.all_shots_tbWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"DURATION", None));
        ___qtablewidgetitem62 = self.all_shots_tbWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"BIDS", None));
        ___qtablewidgetitem63 = self.all_shots_tbWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
        self.t_cli_sel_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Client", None))

#if QT_CONFIG(tooltip)
        self.t_cli_sel_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Select Client", None))
#endif // QT_CONFIG(tooltip)
        self.t_pro_sel_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Project", None))

#if QT_CONFIG(tooltip)
        self.t_pro_sel_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Select Project", None))
#endif // QT_CONFIG(tooltip)
        self.t_status_sel_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Status", None))

#if QT_CONFIG(tooltip)
        self.t_status_sel_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Select Status", None))
#endif // QT_CONFIG(tooltip)
        self.task_search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Shot Name...", None))
        self.task_search_btn.setText("")
#if QT_CONFIG(shortcut)
        self.task_search_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem64 = self.task_pending_tableWid.horizontalHeaderItem(0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"CLIENT", None));
        ___qtablewidgetitem65 = self.task_pending_tableWid.horizontalHeaderItem(1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"PROJECT", None));
        ___qtablewidgetitem66 = self.task_pending_tableWid.horizontalHeaderItem(2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"SEQUENCE", None));
        ___qtablewidgetitem67 = self.task_pending_tableWid.horizontalHeaderItem(3)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"SHOT", None));
        ___qtablewidgetitem68 = self.task_pending_tableWid.horizontalHeaderItem(4)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        ___qtablewidgetitem69 = self.task_pending_tableWid.horizontalHeaderItem(5)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"FRAME IN", None));
        ___qtablewidgetitem70 = self.task_pending_tableWid.horizontalHeaderItem(6)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"FRAME OUT", None));
        ___qtablewidgetitem71 = self.task_pending_tableWid.horizontalHeaderItem(7)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"TOTAL FRAMES", None));
        ___qtablewidgetitem72 = self.task_pending_tableWid.horizontalHeaderItem(8)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem73 = self.task_pending_tableWid.horizontalHeaderItem(9)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"BIDS", None));
        ___qtablewidgetitem74 = self.task_pending_tableWid.horizontalHeaderItem(10)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"PROGRESS", None));
        ___qtablewidgetitem75 = self.task_pending_tableWid.horizontalHeaderItem(11)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
        self.task_tabWid.setTabText(self.task_tabWid.indexOf(self.pending_task), QCoreApplication.translate("MainWindow", u"Pending", None))
        ___qtablewidgetitem76 = self.task_completed_tableWid.horizontalHeaderItem(0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"CLIENT", None));
        ___qtablewidgetitem77 = self.task_completed_tableWid.horizontalHeaderItem(1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"PROJECT", None));
        ___qtablewidgetitem78 = self.task_completed_tableWid.horizontalHeaderItem(2)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"SEQUENCE", None));
        ___qtablewidgetitem79 = self.task_completed_tableWid.horizontalHeaderItem(3)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"SHOT", None));
        ___qtablewidgetitem80 = self.task_completed_tableWid.horizontalHeaderItem(4)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        ___qtablewidgetitem81 = self.task_completed_tableWid.horizontalHeaderItem(5)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"FRAME IN", None));
        ___qtablewidgetitem82 = self.task_completed_tableWid.horizontalHeaderItem(6)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"FRAME OUT", None));
        ___qtablewidgetitem83 = self.task_completed_tableWid.horizontalHeaderItem(7)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"TOTAL FRAMES", None));
        ___qtablewidgetitem84 = self.task_completed_tableWid.horizontalHeaderItem(8)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem85 = self.task_completed_tableWid.horizontalHeaderItem(9)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"BIDS", None));
        ___qtablewidgetitem86 = self.task_completed_tableWid.horizontalHeaderItem(10)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"PROGRESS", None));
        ___qtablewidgetitem87 = self.task_completed_tableWid.horizontalHeaderItem(11)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
        self.task_tabWid.setTabText(self.task_tabWid.indexOf(self.completed), QCoreApplication.translate("MainWindow", u"Completed", None))
        self.sr_shows_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total Shows", None))
        self.sr_delta_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Actual vs Achieved", None))
        self.sr_ach_mandays_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Achieved ManDays", None))
        self.sr_clients_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Clients", None))
        self.sr_actmandays_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Actual Mandays", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Yet To Start", None))
        self.sr_yts_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"WIP", None))
        self.sr_wip_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Retakes", None))
        self.sr_rtk_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.sr_cmp_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.sr_shots_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Total Shots", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Studio Report", None))
        self.sr_download_btn.setText(QCoreApplication.translate("MainWindow", u"Download Report", None))
        self.new_pwd1_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Password", None))
        self.new_pwd2_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Re Enter New Password", None))
        self.change_butt.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Change Password Form", None))
        self.old_pwd_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Current Password", None))
    # retranslateUi

