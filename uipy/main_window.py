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
        MainWindow.resize(1593, 888)
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
        icon.addFile(u":/custom/icons/custom/tendril_logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.centralLayout = QGridLayout(self.centralwidget)
        self.centralLayout.setObjectName(u"centralLayout")
        self.centralLayout.setHorizontalSpacing(7)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFont(font)
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
        font1 = QFont()
        font1.setPointSize(8)
        self.frame_label_top_btns.setFont(font1)
        self.frame_label_top_btns.setStyleSheet(u"border-color:rgb(85, 170, 127);")
        self.frame_label_top_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, 0)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        self.label_title_bar_top.setMaximumSize(QSize(180, 16777215))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_title_bar_top.setFont(font2)
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
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_10)

        self.projects_pb = QPushButton(self.frame_42)
        self.projects_pb.setObjectName(u"projects_pb")
        self.projects_pb.setCursor(QCursor(Qt.PointingHandCursor))
        self.projects_pb.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/24x24/icons/twotone_home_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.projects_pb.setIcon(icon1)
        self.projects_pb.setIconSize(QSize(32, 32))
        self.projects_pb.setFlat(True)

        self.horizontalLayout_41.addWidget(self.projects_pb)

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

        self.toggle_pb = QPushButton(self.frame_42)
        self.toggle_pb.setObjectName(u"toggle_pb")
        icon8 = QIcon()
        icon8.addFile(u":/custom/icons/custom/dark_mode.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_pb.setIcon(icon8)
        self.toggle_pb.setIconSize(QSize(32, 32))
        self.toggle_pb.setCheckable(True)
        self.toggle_pb.setFlat(True)

        self.horizontalLayout_41.addWidget(self.toggle_pb)


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
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon9)

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
        icon10 = QIcon()
        icon10.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon10)

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
        icon11 = QIcon()
        icon11.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon11)

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
        self.center_frame.setFont(font)
        self.center_frame.setFrameShape(QFrame.NoFrame)
        self.center_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.center_frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setVerticalSpacing(7)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.center_right_frame = QFrame(self.center_frame)
        self.center_right_frame.setObjectName(u"center_right_frame")
        self.center_right_frame.setFrameShape(QFrame.NoFrame)
        self.center_right_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.center_right_frame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.center_right_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFont(font)
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
        self.stackedWidget.setFont(font)
        self.clients_page = QWidget()
        self.clients_page.setObjectName(u"clients_page")
        self.gridLayout_2 = QGridLayout(self.clients_page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.clients_frame = QFrame(self.clients_page)
        self.clients_frame.setObjectName(u"clients_frame")
        self.clients_frame.setFont(font)
        self.clients_frame.setFrameShape(QFrame.NoFrame)
        self.clients_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.clients_frame)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.clients_top_frame = QFrame(self.clients_frame)
        self.clients_top_frame.setObjectName(u"clients_top_frame")
        self.clients_top_frame.setFrameShape(QFrame.StyledPanel)
        self.clients_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.clients_top_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.clients_top_frame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.label_3.setFont(font3)
        self.label_3.setPixmap(QPixmap(u":/16x16/icons/16x16/cil-user.png"))
        self.label_3.setScaledContents(False)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.clients_label = QLabel(self.clients_top_frame)
        self.clients_label.setObjectName(u"clients_label")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(13)
        self.clients_label.setFont(font4)

        self.horizontalLayout_10.addWidget(self.clients_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.cli_add_btn = QPushButton(self.clients_top_frame)
        self.cli_add_btn.setObjectName(u"cli_add_btn")
        self.cli_add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/24x24/baseline_note_add_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cli_add_btn.setIcon(icon12)
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
        self.cli_table.setFont(font3)
        self.cli_table.setFocusPolicy(Qt.NoFocus)
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
        self.projects_page.setFont(font)
        self.gridLayout_3 = QGridLayout(self.projects_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.projects_frame = QFrame(self.projects_page)
        self.projects_frame.setObjectName(u"projects_frame")
        self.projects_frame.setFrameShape(QFrame.StyledPanel)
        self.projects_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.projects_frame)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pro_top_frame = QFrame(self.projects_frame)
        self.pro_top_frame.setObjectName(u"pro_top_frame")
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
        self.pro_label.setFont(font4)
        self.pro_label.setStyleSheet(u"QLabel{border:none}")

        self.pro_top_frameLayout.addWidget(self.pro_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.pro_top_frameLayout.addItem(self.horizontalSpacer_5)

        self.pro_add_btn = QPushButton(self.pro_top_frame)
        self.pro_add_btn.setObjectName(u"pro_add_btn")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.pro_add_btn.setFont(font5)
        self.pro_add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/24x24/icons/24x24/cil-medical-cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pro_add_btn.setIcon(icon13)
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
        self.pro_table.setFont(font)
        self.pro_table.setFocusPolicy(Qt.NoFocus)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.shot_details_page.sizePolicy().hasHeightForWidth())
        self.shot_details_page.setSizePolicy(sizePolicy2)
        self.shot_details_page.setFont(font)
        self.shot_details_page_2 = QGridLayout(self.shot_details_page)
        self.shot_details_page_2.setObjectName(u"shot_details_page_2")
        self.shot_details_page_2.setHorizontalSpacing(0)
        self.shot_details_page_2.setContentsMargins(0, 0, 0, 0)
        self.shot_details_main_frame = QFrame(self.shot_details_page)
        self.shot_details_main_frame.setObjectName(u"shot_details_main_frame")
        self.shot_details_main_frame.setFont(font)
        self.shot_details_main_frame.setFrameShape(QFrame.StyledPanel)
        self.shot_details_main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.shot_details_main_frame)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.shot_details_top_frame = QFrame(self.shot_details_main_frame)
        self.shot_details_top_frame.setObjectName(u"shot_details_top_frame")
        self.shot_details_top_frame.setFrameShape(QFrame.StyledPanel)
        self.shot_details_top_frame.setFrameShadow(QFrame.Raised)
        self.shot_details_top_frame.setMidLineWidth(0)
        self.gridLayout = QGridLayout(self.shot_details_top_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.shot_details_top_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_17)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_7 = QFrame(self.frame_17)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(120, 0))
        self.frame_7.setMaximumSize(QSize(210, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(5)
        self.formLayout_2.setContentsMargins(0, -1, 0, 0)
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_17)

        self.shotName_lbl = QLabel(self.frame_7)
        self.shotName_lbl.setObjectName(u"shotName_lbl")
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(10)
        self.shotName_lbl.setFont(font6)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.shotName_lbl)

        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)
        self.label_27.setCursor(QCursor(Qt.ArrowCursor))

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_27)

        self.eta_lbl = QLabel(self.frame_7)
        self.eta_lbl.setObjectName(u"eta_lbl")
        self.eta_lbl.setFont(font)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.eta_lbl)

        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font5)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_29)

        self.projectName_lbl = QLabel(self.frame_7)
        self.projectName_lbl.setObjectName(u"projectName_lbl")
        self.projectName_lbl.setFont(font)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.projectName_lbl)

        self.label_30 = QLabel(self.frame_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_30)

        self.startDate_lbl = QLabel(self.frame_7)
        self.startDate_lbl.setObjectName(u"startDate_lbl")
        self.startDate_lbl.setFont(font)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.startDate_lbl)

        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font5)

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_31)

        self.endDate_lbl = QLabel(self.frame_7)
        self.endDate_lbl.setObjectName(u"endDate_lbl")
        self.endDate_lbl.setFont(font)

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.endDate_lbl)

        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font5)

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.label_33)

        self.totalBids_lbl = QLabel(self.frame_7)
        self.totalBids_lbl.setObjectName(u"totalBids_lbl")
        self.totalBids_lbl.setFont(font)

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.totalBids_lbl)

        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)

        self.formLayout_2.setWidget(16, QFormLayout.LabelRole, self.label_34)

        self.seqName_lbl = QLabel(self.frame_7)
        self.seqName_lbl.setObjectName(u"seqName_lbl")
        self.seqName_lbl.setFont(font)

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.seqName_lbl)

        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(75)
        self.label_35.setFont(font7)

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.label_35)

        self.frameIn_lbl = QLabel(self.frame_7)
        self.frameIn_lbl.setObjectName(u"frameIn_lbl")
        self.frameIn_lbl.setFont(font)

        self.formLayout_2.setWidget(18, QFormLayout.FieldRole, self.frameIn_lbl)

        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font5)

        self.formLayout_2.setWidget(20, QFormLayout.LabelRole, self.label_36)

        self.frameOut_lbl = QLabel(self.frame_7)
        self.frameOut_lbl.setObjectName(u"frameOut_lbl")
        self.frameOut_lbl.setFont(font)

        self.formLayout_2.setWidget(20, QFormLayout.FieldRole, self.frameOut_lbl)

        self.label_38 = QLabel(self.frame_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font5)

        self.formLayout_2.setWidget(22, QFormLayout.LabelRole, self.label_38)

        self.totalFrames_lbl = QLabel(self.frame_7)
        self.totalFrames_lbl.setObjectName(u"totalFrames_lbl")
        self.totalFrames_lbl.setFont(font)

        self.formLayout_2.setWidget(22, QFormLayout.FieldRole, self.totalFrames_lbl)

        self.thumbnail = QFrame(self.frame_7)
        self.thumbnail.setObjectName(u"thumbnail")
        self.thumbnail.setMinimumSize(QSize(200, 150))
        self.thumbnail.setMaximumSize(QSize(210, 150))
        self.thumbnail.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.thumbnail.setFrameShape(QFrame.StyledPanel)
        self.thumbnail.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.thumbnail)
        self.gridLayout_24.setObjectName(u"gridLayout_24")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.thumbnail)

        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font5)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_22)

        self.status_btn = QPushButton(self.frame_7)
        self.status_btn.setObjectName(u"status_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.status_btn.sizePolicy().hasHeightForWidth())
        self.status_btn.setSizePolicy(sizePolicy3)
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.status_btn.setFont(font8)
        self.status_btn.setLayoutDirection(Qt.LeftToRight)
        self.status_btn.setFlat(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.status_btn)

        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(200, 5))
        self.line.setMaximumSize(QSize(210, 5))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.line)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.shot_details_tabWidget = QTabWidget(self.frame_17)
        self.shot_details_tabWidget.setObjectName(u"shot_details_tabWidget")
        self.shot_details_tabWidget.setFont(font)
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
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(16)
        font9.setBold(True)
        font9.setWeight(75)
        self.input_label_2.setFont(font9)
        self.input_label_2.setLayoutDirection(Qt.LeftToRight)
        self.input_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.input_label_2)

        self.taskann = QListWidget(self.tab)
        self.taskann.setObjectName(u"taskann")
        self.taskann.setMinimumSize(QSize(200, 0))
        self.taskann.setFont(font)
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
        self.input_label_3.setFont(font9)
        self.input_label_3.setLayoutDirection(Qt.LeftToRight)
        self.input_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.input_label_3)

        self.feedbackann = QListView(self.tab)
        self.feedbackann.setObjectName(u"feedbackann")
        self.feedbackann.setMinimumSize(QSize(200, 0))
        self.feedbackann.setFont(font)
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
        sizePolicy2.setHeightForWidth(self.assets_main_frame.sizePolicy().hasHeightForWidth())
        self.assets_main_frame.setSizePolicy(sizePolicy2)
        self.assets_main_frame.setFrameShape(QFrame.StyledPanel)
        self.assets_main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.assets_main_frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.assests_dep_frame = QFrame(self.assets_main_frame)
        self.assests_dep_frame.setObjectName(u"assests_dep_frame")
        sizePolicy2.setHeightForWidth(self.assests_dep_frame.sizePolicy().hasHeightForWidth())
        self.assests_dep_frame.setSizePolicy(sizePolicy2)
        self.assests_dep_frame.setStyleSheet(u"")
        self.assests_dep_frame.setFrameShape(QFrame.StyledPanel)
        self.assests_dep_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.assests_dep_frame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dep_tabWidget = QTabWidget(self.assests_dep_frame)
        self.dep_tabWidget.setObjectName(u"dep_tabWidget")
        self.dep_tabWidget.setFont(font)
        self.paint_tab = QWidget()
        self.paint_tab.setObjectName(u"paint_tab")
        self.gridLayout_19 = QGridLayout(self.paint_tab)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 8, 0, 0)
        self.scripts_pre_frame = QFrame(self.paint_tab)
        self.scripts_pre_frame.setObjectName(u"scripts_pre_frame")
        sizePolicy2.setHeightForWidth(self.scripts_pre_frame.sizePolicy().hasHeightForWidth())
        self.scripts_pre_frame.setSizePolicy(sizePolicy2)
        self.scripts_pre_frame.setFrameShape(QFrame.NoFrame)
        self.scripts_pre_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.scripts_pre_frame)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 8, 0)
        self.scripts_frame = QFrame(self.scripts_pre_frame)
        self.scripts_frame.setObjectName(u"scripts_frame")
        self.scripts_frame.setFrameShape(QFrame.NoFrame)
        self.scripts_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.scripts_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 8, 0, 8)
        self.Pscripts_treeWid = QTreeWidget(self.scripts_frame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(6, u"7");
        __qtreewidgetitem.setText(5, u"6");
        self.Pscripts_treeWid.setHeaderItem(__qtreewidgetitem)
        self.Pscripts_treeWid.setObjectName(u"Pscripts_treeWid")
        self.Pscripts_treeWid.setFont(font)
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


        self.verticalLayout_3.addWidget(self.scripts_frame)

        self.output_frame = QFrame(self.scripts_pre_frame)
        self.output_frame.setObjectName(u"output_frame")
        self.output_frame.setFrameShape(QFrame.NoFrame)
        self.output_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.output_frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 8, 0, 8)
        self.Poutput_treeWid = QTreeWidget(self.output_frame)
        self.Poutput_treeWid.setObjectName(u"Poutput_treeWid")
        self.Poutput_treeWid.setFrameShape(QFrame.NoFrame)
        self.Poutput_treeWid.setFrameShadow(QFrame.Raised)
        self.Poutput_treeWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Poutput_treeWid.setAlternatingRowColors(True)
        self.Poutput_treeWid.setAnimated(True)
        self.Poutput_treeWid.setColumnCount(5)
        self.Poutput_treeWid.header().setVisible(False)

        self.horizontalLayout_17.addWidget(self.Poutput_treeWid)


        self.verticalLayout_3.addWidget(self.output_frame)


        self.gridLayout_19.addWidget(self.scripts_pre_frame, 0, 0, 1, 1)

        self.dep_tabWidget.addTab(self.paint_tab, "")
        self.roto_tab = QWidget()
        self.roto_tab.setObjectName(u"roto_tab")
        self.gridLayout_27 = QGridLayout(self.roto_tab)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 8, 0, 0)
        self.scripts_pre_frame_2 = QFrame(self.roto_tab)
        self.scripts_pre_frame_2.setObjectName(u"scripts_pre_frame_2")
        sizePolicy2.setHeightForWidth(self.scripts_pre_frame_2.sizePolicy().hasHeightForWidth())
        self.scripts_pre_frame_2.setSizePolicy(sizePolicy2)
        self.scripts_pre_frame_2.setFrameShape(QFrame.NoFrame)
        self.scripts_pre_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.scripts_pre_frame_2)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 8, 0)
        self.scripts_frame_2 = QFrame(self.scripts_pre_frame_2)
        self.scripts_frame_2.setObjectName(u"scripts_frame_2")
        self.scripts_frame_2.setFrameShape(QFrame.NoFrame)
        self.scripts_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.scripts_frame_2)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 8, 0, 8)
        self.Rscripts_treeWid = QTreeWidget(self.scripts_frame_2)
        self.Rscripts_treeWid.setObjectName(u"Rscripts_treeWid")
        self.Rscripts_treeWid.setFont(font)
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
        self.preren_frame_2.setFrameShape(QFrame.NoFrame)
        self.preren_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.preren_frame_2)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 8, 0, 8)
        self.Routput_treeWid = QTreeWidget(self.preren_frame_2)
        self.Routput_treeWid.setObjectName(u"Routput_treeWid")
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
        sizePolicy2.setHeightForWidth(self.scripts_pre_frame_3.sizePolicy().hasHeightForWidth())
        self.scripts_pre_frame_3.setSizePolicy(sizePolicy2)
        self.scripts_pre_frame_3.setFrameShape(QFrame.NoFrame)
        self.scripts_pre_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.scripts_pre_frame_3)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 8, 0)
        self.scripts_frame_3 = QFrame(self.scripts_pre_frame_3)
        self.scripts_frame_3.setObjectName(u"scripts_frame_3")
        self.scripts_frame_3.setFrameShape(QFrame.NoFrame)
        self.scripts_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.scripts_frame_3)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 8, 0, 8)
        self.Mscripts_treeWid = QTreeWidget(self.scripts_frame_3)
        self.Mscripts_treeWid.setObjectName(u"Mscripts_treeWid")
        self.Mscripts_treeWid.setFont(font)
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
        self.preren_frame_3.setFrameShape(QFrame.NoFrame)
        self.preren_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.preren_frame_3)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 8, 0, 8)
        self.Moutput_treeWid = QTreeWidget(self.preren_frame_3)
        self.Moutput_treeWid.setObjectName(u"Moutput_treeWid")
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
        self.inputs_frame.setFrameShape(QFrame.StyledPanel)
        self.inputs_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.inputs_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 8, 0)
        self.intput_treeWid_frame = QFrame(self.inputs_frame)
        self.intput_treeWid_frame.setObjectName(u"intput_treeWid_frame")
        self.intput_treeWid_frame.setFrameShape(QFrame.StyledPanel)
        self.intput_treeWid_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.intput_treeWid_frame)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 8, 0, 8)
        self.input_TreeWid = QTreeWidget(self.intput_treeWid_frame)
        self.input_TreeWid.setObjectName(u"input_TreeWid")
        self.input_TreeWid.setMinimumSize(QSize(200, 0))
        self.input_TreeWid.setFont(font)
        self.input_TreeWid.setFrameShape(QFrame.NoFrame)
        self.input_TreeWid.setFrameShadow(QFrame.Sunken)
        self.input_TreeWid.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.input_TreeWid.setColumnCount(0)
        self.input_TreeWid.header().setVisible(False)
        self.input_TreeWid.header().setCascadingSectionResizes(False)

        self.gridLayout_21.addWidget(self.input_TreeWid, 1, 1, 1, 1)

        self.input_label_frame = QFrame(self.intput_treeWid_frame)
        self.input_label_frame.setObjectName(u"input_label_frame")
        self.input_label_frame.setMinimumSize(QSize(10, 0))
        self.input_label_frame.setFrameShape(QFrame.StyledPanel)
        self.input_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.input_label_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.input_label = QLabel(self.input_label_frame)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMinimumSize(QSize(10, 0))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(11)
        self.input_label.setFont(font10)
        self.input_label.setLayoutDirection(Qt.LeftToRight)
        self.input_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.input_label)


        self.gridLayout_21.addWidget(self.input_label_frame, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.intput_treeWid_frame)


        self.gridLayout_5.addWidget(self.inputs_frame, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.assets_main_frame, 0, 0, 1, 1)

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
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_12)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(0)
        self.gridLayout_31.setVerticalSpacing(10)
        self.gridLayout_31.setContentsMargins(8, 0, 8, 0)
        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_11)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 8, 0, 8)
        self.label_39 = QLabel(self.frame_11)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)
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
        self.int_tabWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.int_tabWid.setShowGrid(False)
        self.int_tabWid.verticalHeader().setVisible(False)

        self.gridLayout_31.addWidget(self.int_tabWid, 1, 0, 1, 1)


        self.horizontalLayout_40.addWidget(self.frame_12)

        self.frame_38 = QFrame(self.frame_2)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_38)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setHorizontalSpacing(0)
        self.gridLayout_33.setVerticalSpacing(10)
        self.gridLayout_33.setContentsMargins(8, 0, 8, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_39)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 8, 0, 8)
        self.label_40 = QLabel(self.frame_39)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)
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
        self.sh_up_Project.setFont(font)

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
        self.sh_selected_file_name.setFont(font)

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
        font11 = QFont()
        font11.setFamily(u"Nirmala UI")
        font11.setPointSize(16)
        font11.setBold(True)
        font11.setWeight(75)
        self.sh_import_progressBar.setFont(font11)
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
        self.filter_frame.setStyleSheet(u"")
        self.filter_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_65 = QGridLayout(self.filter_frame)
        self.gridLayout_65.setSpacing(0)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(5, 5, 5, 5)
        self.frame_43 = QFrame(self.filter_frame)
        self.frame_43.setObjectName(u"frame_43")
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
        self.sel_all_shtTable_chkBox.setFont(font)

        self.gridLayout_44.addWidget(self.sel_all_shtTable_chkBox, 1, 0, 1, 1)

        self.assign_leads_btn = QPushButton(self.frame_44)
        self.assign_leads_btn.setObjectName(u"assign_leads_btn")
        self.assign_leads_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/24x24/icons/24x24/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.assign_leads_btn.setIcon(icon16)
        self.assign_leads_btn.setIconSize(QSize(20, 20))
        self.assign_leads_btn.setFlat(True)

        self.gridLayout_44.addWidget(self.assign_leads_btn, 1, 1, 1, 1)

        self.shot_search_lineEdit = QLineEdit(self.frame_44)
        self.shot_search_lineEdit.setObjectName(u"shot_search_lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.shot_search_lineEdit.sizePolicy().hasHeightForWidth())
        self.shot_search_lineEdit.setSizePolicy(sizePolicy4)
        self.shot_search_lineEdit.setMinimumSize(QSize(0, 34))
        self.shot_search_lineEdit.setFont(font3)
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
        self.stat_filter_cb.setFont(font)

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
        self.pro_filter_cb.setFont(font)

        self.gridLayout_17.addWidget(self.pro_filter_cb, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_4, 8, 0, 1, 1)


        self.gridLayout_65.addWidget(self.frame_43, 0, 0, 1, 1)

        self.frame_45 = QFrame(self.filter_frame)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_45)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setVerticalSpacing(7)
        self.gridLayout_29.setContentsMargins(5, 5, 5, 5)
        self.apply_filter_btn = QPushButton(self.frame_45)
        self.apply_filter_btn.setObjectName(u"apply_filter_btn")
        self.apply_filter_btn.setMinimumSize(QSize(80, 30))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(8)
        font12.setBold(True)
        font12.setWeight(75)
        self.apply_filter_btn.setFont(font12)
        self.apply_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/24x24/icons/24x24/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.apply_filter_btn.setIcon(icon17)
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
        if (self.all_shots_tbWidget.columnCount() < 16):
            self.all_shots_tbWidget.setColumnCount(16)
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
        self.all_shots_tbWidget.setObjectName(u"all_shots_tbWidget")
        self.all_shots_tbWidget.setFont(font)
        self.all_shots_tbWidget.setFocusPolicy(Qt.NoFocus)
        self.all_shots_tbWidget.setFrameShape(QFrame.NoFrame)
        self.all_shots_tbWidget.setFrameShadow(QFrame.Sunken)
        self.all_shots_tbWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.all_shots_tbWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.all_shots_tbWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.all_shots_tbWidget.setAlternatingRowColors(True)
        self.all_shots_tbWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.all_shots_tbWidget.setShowGrid(True)
        self.all_shots_tbWidget.setSortingEnabled(True)
        self.all_shots_tbWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.all_shots_tbWidget.horizontalHeader().setMinimumSectionSize(60)
        self.all_shots_tbWidget.horizontalHeader().setDefaultSectionSize(120)
        self.all_shots_tbWidget.horizontalHeader().setStretchLastSection(True)
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
        self.gridLayout_23 = QGridLayout(self.frame_23)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_23)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(300, 0))
        self.frame_5.setMaximumSize(QSize(350, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.task_search_lineEdit = QLineEdit(self.frame_5)
        self.task_search_lineEdit.setObjectName(u"task_search_lineEdit")
        self.task_search_lineEdit.setMinimumSize(QSize(0, 34))
        self.task_search_lineEdit.setFont(font3)
        self.task_search_lineEdit.setStyleSheet(u"")
        self.task_search_lineEdit.setFrame(True)

        self.horizontalLayout_8.addWidget(self.task_search_lineEdit)

        self.task_search_btn = QPushButton(self.frame_5)
        self.task_search_btn.setObjectName(u"task_search_btn")
        self.task_search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/16x16/icons/16x16/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_search_btn.setIcon(icon18)
        self.task_search_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.task_search_btn)


        self.verticalLayout_23.addLayout(self.horizontalLayout_8)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(330, 0))
        self.frame_8.setMaximumSize(QSize(250, 16777215))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"border:1px solid grey\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_8)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 10, 0)
        self.toolBox = QToolBox(self.frame_8)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(240, 0))
        self.toolBox.setMaximumSize(QSize(300, 16777215))
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(9)
        font13.setBold(True)
        font13.setWeight(75)
        self.toolBox.setFont(font13)
        self.toolBox.setFocusPolicy(Qt.NoFocus)
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"border:None;\n"
"}QToolBox::Tab{\n"
"	border: 2px solid rgb(0, 96, 144);\n"
"	border-radius: 6px;\n"
"	color: rgb(235, 157, 0);\n"
"}\n"
"QToolBox::Tab:active{\n"
"	border-bottom: None;\n"
"}\n"
"QFrame{\n"
"border:none\n"
"}")
        self.filters = QWidget()
        self.filters.setObjectName(u"filters")
        self.filters.setGeometry(QRect(0, 0, 300, 619))
        self.filters.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.filters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.t_pro_sel_cb = QComboBox(self.filters)
        self.t_pro_sel_cb.addItem("")
        self.t_pro_sel_cb.setObjectName(u"t_pro_sel_cb")
        font14 = QFont()
        font14.setFamily(u"Myriad Pro Light")
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(7)
        self.t_pro_sel_cb.setFont(font14)
        self.t_pro_sel_cb.setStyleSheet(u"font: 63 15t \"Myriad Pro Light\";\n"
"color: rgb(85, 170, 255);")

        self.verticalLayout.addWidget(self.t_pro_sel_cb)

        self.t_status_sel_cb = QComboBox(self.filters)
        self.t_status_sel_cb.addItem("")
        self.t_status_sel_cb.setObjectName(u"t_status_sel_cb")
        self.t_status_sel_cb.setMinimumSize(QSize(150, 0))
        self.t_status_sel_cb.setFont(font14)
        self.t_status_sel_cb.setStyleSheet(u"font: 63 15t \"Myriad Pro Light\";\n"
"color: rgb(85, 170, 255);")

        self.verticalLayout.addWidget(self.t_status_sel_cb)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        icon19 = QIcon()
        icon19.addFile(u":/16x16/icons/16x16/cil-cursor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.filters, icon19, u"FILTERS")
        self.user_profile = QWidget()
        self.user_profile.setObjectName(u"user_profile")
        self.user_profile.setGeometry(QRect(0, 0, 300, 619))
        self.user_profile.setStyleSheet(u"border: None;\n"
"")
        self.formLayout = QFormLayout(self.user_profile)
        self.formLayout.setObjectName(u"formLayout")
        self.label_46 = QLabel(self.user_profile)
        self.label_46.setObjectName(u"label_46")
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        font15.setPointSize(12)
        font15.setBold(False)
        font15.setWeight(50)
        self.label_46.setFont(font15)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_46)

        self.label_15 = QLabel(self.user_profile)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_15)

        self.name_lbl = QLabel(self.user_profile)
        self.name_lbl.setObjectName(u"name_lbl")
        font16 = QFont()
        font16.setPointSize(10)
        self.name_lbl.setFont(font16)
        self.name_lbl.setStyleSheet(u"color: rgb(166, 166, 166);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_lbl)

        self.label_44 = QLabel(self.user_profile)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_44)

        self.label_43 = QLabel(self.user_profile)
        self.label_43.setObjectName(u"label_43")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_43)

        self.emp_id_lbl = QLabel(self.user_profile)
        self.emp_id_lbl.setObjectName(u"emp_id_lbl")
        self.emp_id_lbl.setFont(font16)
        self.emp_id_lbl.setStyleSheet(u"color: rgb(166, 166, 166);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.emp_id_lbl)

        self.label_14 = QLabel(self.user_profile)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_14)

        self.label_45 = QLabel(self.user_profile)
        self.label_45.setObjectName(u"label_45")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_45)

        self.dep_lbl = QLabel(self.user_profile)
        self.dep_lbl.setObjectName(u"dep_lbl")
        self.dep_lbl.setFont(font16)
        self.dep_lbl.setStyleSheet(u"color: rgb(166, 166, 166);")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.dep_lbl)

        self.label_23 = QLabel(self.user_profile)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_23)

        self.label_42 = QLabel(self.user_profile)
        self.label_42.setObjectName(u"label_42")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_42)

        self.desg_lbl = QLabel(self.user_profile)
        self.desg_lbl.setObjectName(u"desg_lbl")
        self.desg_lbl.setFont(font16)
        self.desg_lbl.setStyleSheet(u"color: rgb(166, 166, 166);")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.desg_lbl)

        self.label_25 = QLabel(self.user_profile)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_25)

        self.label_62 = QLabel(self.user_profile)
        self.label_62.setObjectName(u"label_62")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_62)

        self.tl_lbl = QLabel(self.user_profile)
        self.tl_lbl.setObjectName(u"tl_lbl")
        self.tl_lbl.setFont(font16)
        self.tl_lbl.setStyleSheet(u"color: rgb(166, 166, 166);")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.tl_lbl)

        self.label_41 = QLabel(self.user_profile)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_41)

        self.label_47 = QLabel(self.user_profile)
        self.label_47.setObjectName(u"label_47")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.label_47)

        self.sup_lbl = QLabel(self.user_profile)
        self.sup_lbl.setObjectName(u"sup_lbl")
        self.sup_lbl.setFont(font16)
        self.sup_lbl.setStyleSheet(u"color: rgb(166, 166, 166);")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.sup_lbl)

        icon20 = QIcon()
        icon20.addFile(u":/16x16/icons/16x16/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        icon20.addFile(u":/16x16/icons/16x16/cil-chevron-bottom.png", QSize(), QIcon.Active, QIcon.On)
        self.toolBox.addItem(self.user_profile, icon20, u"USER PROFILE")
        self.overviewdashboard = QWidget()
        self.overviewdashboard.setObjectName(u"overviewdashboard")
        self.overviewdashboard.setGeometry(QRect(0, 0, 314, 602))
        self.overviewdashboard.setStyleSheet(u"border:None;")
        self.gridLayout_9 = QGridLayout(self.overviewdashboard)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(10, 0, 10, 5)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.toolButton = QToolButton(self.overviewdashboard)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(92, 40))
        self.toolButton.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"Border-radius: 10px;")

        self.verticalLayout_20.addWidget(self.toolButton)

        self.label_2 = QLabel(self.overviewdashboard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.toolButton_2 = QToolButton(self.overviewdashboard)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(92, 40))
        self.toolButton_2.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"Border-radius: 10px;")

        self.verticalLayout_21.addWidget(self.toolButton_2)

        self.label_5 = QLabel(self.overviewdashboard)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.RightToLeft)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.toolButton_3 = QToolButton(self.overviewdashboard)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(92, 40))
        self.toolButton_3.setStyleSheet(u"background-color: rgb(85, 170, 0);\n"
"Border-radius: 10px;")

        self.verticalLayout_22.addWidget(self.toolButton_3)

        self.label_6 = QLabel(self.overviewdashboard)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_22)


        self.gridLayout_9.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        icon21 = QIcon()
        icon21.addFile(u":/16x16/icons/16x16/cil-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.overviewdashboard, icon21, u"OVERVIEW DASHBOARD")
        self.dcc_tools = QWidget()
        self.dcc_tools.setObjectName(u"dcc_tools")
        self.dcc_tools.setGeometry(QRect(0, 0, 300, 619))
        self.dcc_tools.setStyleSheet(u"border:None")
        self.gridLayout_47 = QGridLayout(self.dcc_tools)
        self.gridLayout_47.setSpacing(0)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.dcc_tools)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border:None;")
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_13)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 301, 209))
        self.gridLayout_8 = QGridLayout(self.layoutWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.nukeX_btn = QPushButton(self.layoutWidget)
        self.nukeX_btn.setObjectName(u"nukeX_btn")
        self.nukeX_btn.setMinimumSize(QSize(65, 65))
        self.nukeX_btn.setMaximumSize(QSize(70, 16777215))
        self.nukeX_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.nukeX_btn.setStyleSheet(u"QPushButton::hover{\n"
"border:3px solid white\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/custom/icons/custom/nkX.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nukeX_btn.setIcon(icon22)
        self.nukeX_btn.setIconSize(QSize(64, 64))

        self.gridLayout_8.addWidget(self.nukeX_btn, 0, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(65, 65))
        self.pushButton_5.setMaximumSize(QSize(70, 16777215))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton::hover{\n"
"border:3px solid white\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/custom/icons/custom/maya-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon23)
        self.pushButton_5.setIconSize(QSize(64, 64))

        self.gridLayout_8.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.photoshop_btn = QPushButton(self.layoutWidget)
        self.photoshop_btn.setObjectName(u"photoshop_btn")
        self.photoshop_btn.setMinimumSize(QSize(65, 65))
        self.photoshop_btn.setMaximumSize(QSize(70, 16777215))
        self.photoshop_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.photoshop_btn.setStyleSheet(u"QPushButton::hover{\n"
"border:3px solid white\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/custom/icons/custom/psd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.photoshop_btn.setIcon(icon24)
        self.photoshop_btn.setIconSize(QSize(64, 64))
        self.photoshop_btn.setFlat(True)

        self.gridLayout_8.addWidget(self.photoshop_btn, 0, 0, 1, 1)

        self.shilloute_btn = QPushButton(self.layoutWidget)
        self.shilloute_btn.setObjectName(u"shilloute_btn")
        self.shilloute_btn.setMinimumSize(QSize(65, 65))
        self.shilloute_btn.setMaximumSize(QSize(70, 16777215))
        self.shilloute_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.shilloute_btn.setStyleSheet(u"QPushButton::hover{\n"
"border:3px solid white\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/custom/icons/custom/sfx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shilloute_btn.setIcon(icon25)
        self.shilloute_btn.setIconSize(QSize(64, 64))

        self.gridLayout_8.addWidget(self.shilloute_btn, 0, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(65, 65))
        self.pushButton_6.setMaximumSize(QSize(70, 16777215))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton::hover{\n"
"border:3px solid white\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u":/custom/icons/custom/blender_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon26)
        self.pushButton_6.setIconSize(QSize(64, 64))

        self.gridLayout_8.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.RV_btn = QPushButton(self.layoutWidget)
        self.RV_btn.setObjectName(u"RV_btn")
        self.RV_btn.setMinimumSize(QSize(65, 65))
        self.RV_btn.setMaximumSize(QSize(70, 16777215))
        self.RV_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.RV_btn.setStyleSheet(u"QPushButton::hover{\n"
"border:3px solid white\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u":/custom/C:/Users/admin/Desktop/rv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RV_btn.setIcon(icon27)
        self.RV_btn.setIconSize(QSize(64, 64))
        self.RV_btn.setFlat(True)

        self.gridLayout_8.addWidget(self.RV_btn, 1, 0, 1, 1)


        self.gridLayout_47.addWidget(self.frame_13, 0, 0, 1, 1)

        icon28 = QIcon()
        icon28.addFile(u":/16x16/icons/16x16/cil-chevron-right.png", QSize(), QIcon.Normal, QIcon.Off)
        icon28.addFile(u":/16x16/icons/16x16/cil-chevron-bottom.png", QSize(), QIcon.Active, QIcon.On)
        self.toolBox.addItem(self.dcc_tools, icon28, u"DCC $ DEV TOOLS")

        self.gridLayout_35.addWidget(self.toolBox, 0, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_8)


        self.gridLayout_23.addWidget(self.frame_5, 0, 3, 1, 1)

        self.mytask_tableWid = QTableWidget(self.frame_23)
        if (self.mytask_tableWid.columnCount() < 11):
            self.mytask_tableWid.setColumnCount(11)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(5, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(6, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(7, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(8, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(9, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.mytask_tableWid.setHorizontalHeaderItem(10, __qtablewidgetitem78)
        self.mytask_tableWid.setObjectName(u"mytask_tableWid")
        self.mytask_tableWid.setFrameShape(QFrame.Box)
        self.mytask_tableWid.setFrameShadow(QFrame.Raised)
        self.mytask_tableWid.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.mytask_tableWid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mytask_tableWid.setDragEnabled(False)
        self.mytask_tableWid.setDragDropOverwriteMode(False)
        self.mytask_tableWid.setAlternatingRowColors(True)
        self.mytask_tableWid.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mytask_tableWid.setShowGrid(True)
        self.mytask_tableWid.setGridStyle(Qt.SolidLine)
        self.mytask_tableWid.setSortingEnabled(True)
        self.mytask_tableWid.horizontalHeader().setCascadingSectionResizes(False)
        self.mytask_tableWid.horizontalHeader().setStretchLastSection(False)
        self.mytask_tableWid.verticalHeader().setVisible(False)

        self.gridLayout_23.addWidget(self.mytask_tableWid, 0, 0, 1, 1)

        self.line_13 = QFrame(self.frame_23)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_23.addWidget(self.line_13, 0, 2, 1, 1)


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
        font17 = QFont()
        font17.setFamily(u"Segoe UI")
        font17.setPointSize(59)
        self.sr_shows_lbl.setFont(font17)
        self.sr_shows_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.sr_shows_lbl)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font4)
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
        self.sr_delta_lbl.setFont(font17)
        self.sr_delta_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.sr_delta_lbl)

        self.label_32 = QLabel(self.frame_30)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font4)
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
        self.sr_ach_mandays_lbl.setFont(font17)
        self.sr_ach_mandays_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.sr_ach_mandays_lbl)

        self.label_28 = QLabel(self.frame_29)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font4)
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
        self.sr_clients_lbl.setFont(font17)
        self.sr_clients_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.sr_clients_lbl)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
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
        self.sr_actmandays_lbl.setFont(font17)
        self.sr_actmandays_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.sr_actmandays_lbl)

        self.label_26 = QLabel(self.frame_10)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font4)
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
        font18 = QFont()
        font18.setFamily(u"Segoe UI")
        font18.setPointSize(13)
        font18.setBold(True)
        font18.setWeight(75)
        self.label_13.setFont(font18)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_13)

        self.sr_yts_lbl = QLabel(self.frame_31)
        self.sr_yts_lbl.setObjectName(u"sr_yts_lbl")
        font19 = QFont()
        font19.setFamily(u"Segoe UI")
        font19.setPointSize(30)
        self.sr_yts_lbl.setFont(font19)
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
        self.label_18.setFont(font18)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_18)

        self.sr_wip_lbl = QLabel(self.frame_32)
        self.sr_wip_lbl.setObjectName(u"sr_wip_lbl")
        self.sr_wip_lbl.setFont(font19)
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
        self.label_20.setFont(font18)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_20)

        self.sr_rtk_lbl = QLabel(self.frame_35)
        self.sr_rtk_lbl.setObjectName(u"sr_rtk_lbl")
        self.sr_rtk_lbl.setFont(font19)
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
        self.label_19.setFont(font18)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_19)

        self.sr_cmp_lbl = QLabel(self.frame_33)
        self.sr_cmp_lbl.setObjectName(u"sr_cmp_lbl")
        self.sr_cmp_lbl.setFont(font19)
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
        self.sr_shots_lbl.setFont(font17)
        self.sr_shots_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.sr_shots_lbl)

        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)
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
        self.label_37.setFont(font19)

        self.horizontalLayout_39.addWidget(self.label_37)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_3)

        self.sr_download_btn = QPushButton(self.frame_36)
        self.sr_download_btn.setObjectName(u"sr_download_btn")
        font20 = QFont()
        font20.setFamily(u"MS Shell Dlg 2")
        font20.setPointSize(10)
        font20.setBold(True)
        font20.setWeight(75)
        self.sr_download_btn.setFont(font20)
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
        icon29 = QIcon()
        icon29.addFile(u":/20x20/icons/20x20/cil-arrow-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sr_download_btn.setIcon(icon29)

        self.horizontalLayout_39.addWidget(self.sr_download_btn)


        self.browser_layout.addWidget(self.frame_36, 0, 0, 1, 6)


        self.gridLayout_28.addLayout(self.browser_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.reports_page)
        self.change_password_page = QWidget()
        self.change_password_page.setObjectName(u"change_password_page")
        self.gridLayout_36 = QGridLayout(self.change_password_page)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.old_pwd_le = QLineEdit(self.change_password_page)
        self.old_pwd_le.setObjectName(u"old_pwd_le")
        self.old_pwd_le.setMinimumSize(QSize(0, 40))
        self.old_pwd_le.setMaximumSize(QSize(300, 16777215))
        self.old_pwd_le.setFont(font3)
        self.old_pwd_le.setStyleSheet(u"")
        self.old_pwd_le.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.old_pwd_le)

        self.new_pwd1_le = QLineEdit(self.change_password_page)
        self.new_pwd1_le.setObjectName(u"new_pwd1_le")
        self.new_pwd1_le.setMinimumSize(QSize(0, 40))
        self.new_pwd1_le.setMaximumSize(QSize(300, 16777215))
        self.new_pwd1_le.setFont(font3)
        self.new_pwd1_le.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.new_pwd1_le)

        self.new_pwd2_le = QLineEdit(self.change_password_page)
        self.new_pwd2_le.setObjectName(u"new_pwd2_le")
        self.new_pwd2_le.setMinimumSize(QSize(0, 40))
        self.new_pwd2_le.setMaximumSize(QSize(300, 16777215))
        self.new_pwd2_le.setFont(font3)
        self.new_pwd2_le.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.new_pwd2_le)

        self.change_butt = QPushButton(self.change_password_page)
        self.change_butt.setObjectName(u"change_butt")
        self.change_butt.setMaximumSize(QSize(300, 28))
        font21 = QFont()
        font21.setFamily(u"MS Shell Dlg 2")
        font21.setPointSize(12)
        self.change_butt.setFont(font21)
        self.change_butt.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_butt.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.verticalLayout_10.addWidget(self.change_butt)


        self.gridLayout_36.addLayout(self.verticalLayout_10, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_36.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_36.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.change_password_page)

        self.gridLayout_13.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.content_frame, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.center_right_frame, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.center_frame, 1, 0, 1, 1)


        self.centralLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.shot_details_tabWidget.setCurrentIndex(3)
        self.dep_tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(3)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TENDRILL", None))
        self.label_title_bar_top.setText("")
#if QT_CONFIG(tooltip)
        self.projects_pb.setToolTip(QCoreApplication.translate("MainWindow", u"Projects", None))
#endif // QT_CONFIG(tooltip)
        self.projects_pb.setText("")
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
        self.toggle_pb.setText("")
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
        self.pro_add_btn.setText(QCoreApplication.translate("MainWindow", u"Add Project", None))
        ___qtablewidgetitem15 = self.pro_table.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem16 = self.pro_table.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"PROJECT", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Shot:", None))
        self.shotName_lbl.setText(QCoreApplication.translate("MainWindow", u"Shot name", None))
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
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.status_btn.setText(QCoreApplication.translate("MainWindow", u"WIP", None))
        self.input_label_2.setText(QCoreApplication.translate("MainWindow", u"Task Annotations", None))
        self.input_label_3.setText(QCoreApplication.translate("MainWindow", u"Feedback Annotations", None))
        self.shot_details_tabWidget.setTabText(self.shot_details_tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"ANNOTATIONS", None))
        ___qtreewidgetitem = self.Pscripts_treeWid.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1 = self.Poutput_treeWid.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.dep_tabWidget.setTabText(self.dep_tabWidget.indexOf(self.paint_tab), QCoreApplication.translate("MainWindow", u"PAINT", None))
        ___qtreewidgetitem2 = self.Rscripts_treeWid.headerItem()
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3 = self.Routput_treeWid.headerItem()
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.dep_tabWidget.setTabText(self.dep_tabWidget.indexOf(self.roto_tab), QCoreApplication.translate("MainWindow", u"ROTO", None))
        ___qtreewidgetitem4 = self.Mscripts_treeWid.headerItem()
        ___qtreewidgetitem4.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5 = self.Moutput_treeWid.headerItem()
        ___qtreewidgetitem5.setText(4, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.dep_tabWidget.setTabText(self.dep_tabWidget.indexOf(self.mm_tab), QCoreApplication.translate("MainWindow", u"MM", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"INPUTS", None))
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

        self.apply_filter_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        ___qtablewidgetitem51 = self.all_shots_tbWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"PROJECT", None));
        ___qtablewidgetitem52 = self.all_shots_tbWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"SEQUENCE", None));
        ___qtablewidgetitem53 = self.all_shots_tbWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"SHOT", None));
        ___qtablewidgetitem54 = self.all_shots_tbWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"DEPT", None));
        ___qtablewidgetitem55 = self.all_shots_tbWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem56 = self.all_shots_tbWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"ARTIST", None));
        ___qtablewidgetitem57 = self.all_shots_tbWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"TEAM LEAD", None));
        ___qtablewidgetitem58 = self.all_shots_tbWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"CUT IN", None));
        ___qtablewidgetitem59 = self.all_shots_tbWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"CUT OUT", None));
        ___qtablewidgetitem60 = self.all_shots_tbWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"DURATION", None));
        ___qtablewidgetitem61 = self.all_shots_tbWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"BIDS", None));
        ___qtablewidgetitem62 = self.all_shots_tbWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
        self.task_search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Shot Name...", None))
        self.task_search_btn.setText("")
#if QT_CONFIG(shortcut)
        self.task_search_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.t_pro_sel_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Project", None))

#if QT_CONFIG(tooltip)
        self.t_pro_sel_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Select Project", None))
#endif // QT_CONFIG(tooltip)
        self.t_status_sel_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Status", None))

#if QT_CONFIG(tooltip)
        self.t_status_sel_cb.setToolTip(QCoreApplication.translate("MainWindow", u"Select Status", None))
#endif // QT_CONFIG(tooltip)
        self.toolBox.setItemText(self.toolBox.indexOf(self.filters), QCoreApplication.translate("MainWindow", u"FILTERS", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.name_lbl.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Emp Id", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.emp_id_lbl.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Dept", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.dep_lbl.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Desg", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.desg_lbl.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TL", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tl_lbl.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Sup", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.sup_lbl.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.user_profile), QCoreApplication.translate("MainWindow", u"USER PROFILE", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"320", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Alll Shots", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pending", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.overviewdashboard), QCoreApplication.translate("MainWindow", u"OVERVIEW DASHBOARD", None))
        self.nukeX_btn.setText("")
        self.pushButton_5.setText("")
        self.photoshop_btn.setText("")
        self.shilloute_btn.setText("")
        self.pushButton_6.setText("")
        self.RV_btn.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.dcc_tools), QCoreApplication.translate("MainWindow", u"DCC $ DEV TOOLS", None))
        ___qtablewidgetitem63 = self.mytask_tableWid.horizontalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"PROJECT", None));
        ___qtablewidgetitem64 = self.mytask_tableWid.horizontalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"SEQUENCE", None));
        ___qtablewidgetitem65 = self.mytask_tableWid.horizontalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"SHOT", None));
        ___qtablewidgetitem66 = self.mytask_tableWid.horizontalHeaderItem(3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        ___qtablewidgetitem67 = self.mytask_tableWid.horizontalHeaderItem(4)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"FRAME IN", None));
        ___qtablewidgetitem68 = self.mytask_tableWid.horizontalHeaderItem(5)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"FRAME OUT", None));
        ___qtablewidgetitem69 = self.mytask_tableWid.horizontalHeaderItem(6)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"TOTAL FRAMES", None));
        ___qtablewidgetitem70 = self.mytask_tableWid.horizontalHeaderItem(7)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem71 = self.mytask_tableWid.horizontalHeaderItem(8)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"BIDS", None));
        ___qtablewidgetitem72 = self.mytask_tableWid.horizontalHeaderItem(9)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"START DATE", None));
        ___qtablewidgetitem73 = self.mytask_tableWid.horizontalHeaderItem(10)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
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
        self.old_pwd_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Current Password", None))
        self.new_pwd1_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Password", None))
        self.new_pwd2_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Re Enter New Password", None))
        self.change_butt.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
    # retranslateUi

