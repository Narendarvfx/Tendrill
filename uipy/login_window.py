# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(722, 413)
        LoginWindow.setStyleSheet(u"QFrame{\n"
"background-color: rgba(255, 255, 255,0);\n"
"border:2px;\n"
"border-bottom-color: rgb(85, 170, 255);\n"
"border-radius: 25px\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: transparent;\n"
"color: white;\n"
"border:none;\n"
"border-left:2px;\n"
"\n"
"}")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(False)
        self.frame_2.setGeometry(QRect(60, 50, 201, 81))
        self.frame_2.setStyleSheet(u"image: url(:/custom/icons/custom/tendril.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 110, 321, 211))
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(30, 80, 251, 2))
        self.line_5.setMaximumSize(QSize(16777215, 2))
        self.line_5.setStyleSheet(u"background-color: rgb(127, 127, 127);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(30, 40, 251, 42))
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.toolButton_6 = QToolButton(self.frame_7)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setEnabled(False)
        self.toolButton_6.setStyleSheet(u"border: 0px;\n"
"background-color:none;\n"
"")
        icon = QIcon()
        icon.addFile(u":/custom/icons/custom/baseline_account_circle_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.toolButton_6)

        self.username_le = QLineEdit(self.frame_7)
        self.username_le.setObjectName(u"username_le")
        self.username_le.setMinimumSize(QSize(0, 40))
        self.username_le.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.username_le.setFont(font)
        self.username_le.setStyleSheet(u"")
        self.username_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.username_le.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.username_le)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(30, 100, 251, 42))
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.toolButton_7 = QToolButton(self.frame_8)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setEnabled(False)
        self.toolButton_7.setStyleSheet(u"border: 0px;\n"
"background-color:none;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/custom/icons/custom/baseline_lock_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_7.setIcon(icon1)
        self.toolButton_7.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.toolButton_7)

        self.password_le = QLineEdit(self.frame_8)
        self.password_le.setObjectName(u"password_le")
        self.password_le.setMinimumSize(QSize(0, 40))
        self.password_le.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.password_le.setFont(font1)
        self.password_le.setFocusPolicy(Qt.StrongFocus)
        self.password_le.setStyleSheet(u"")
        self.password_le.setEchoMode(QLineEdit.Password)
        self.password_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.password_le.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.password_le)

        self.layoutWidget_9 = QWidget(self.frame)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(30, 160, 251, 36))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.login_btn = QPushButton(self.layoutWidget_9)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamily(u"Myanmar Text")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.login_btn.setFont(font2)
        self.login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn.setLayoutDirection(Qt.LeftToRight)
        self.login_btn.setStyleSheet(u"background-color: rgb(107, 202, 221);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 8pt \"Myanmar Text\";")
        icon2 = QIcon()
        icon2.addFile(u":/custom/icons/custom/login-rounded-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QSize(26, 26))

        self.horizontalLayout_11.addWidget(self.login_btn)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QRect(45, 0, 241, 31))
        self.lineEdit_4.setStyleSheet(u"font: 10pt \"Arial\";")
        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(60, 250, 251, 2))
        self.line_6.setMaximumSize(QSize(16777215, 2))
        self.line_6.setStyleSheet(u"background-color: rgb(127, 127, 127);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 721, 411))
        self.label.setPixmap(QPixmap(u":/custom/icons/custom/Dark Full Hd Wallpaper.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.layoutWidget_10 = QWidget(self.centralwidget)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(60, 310, 254, 20))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.layoutWidget_10)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")

        self.horizontalLayout_12.addWidget(self.checkBox_3)

        self.label_4 = QLabel(self.layoutWidget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_4)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(670, 20, 25, 19))
        self.toolButton.setStyleSheet(u"background-color: transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/24x24/icons/24x24/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon3)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.line_6.raise_()
        self.layoutWidget_10.raise_()
        self.toolButton.raise_()
        QWidget.setTabOrder(self.username_le, self.password_le)
        QWidget.setTabOrder(self.password_le, self.login_btn)
        QWidget.setTabOrder(self.login_btn, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.toolButton_7)
        QWidget.setTabOrder(self.toolButton_7, self.toolButton_6)

        self.retranslateUi(LoginWindow)
        self.toolButton.clicked.connect(LoginWindow.close)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.toolButton_6.setText(QCoreApplication.translate("LoginWindow", u"...", None))
        self.username_le.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"User Name", None))
        self.toolButton_7.setText(QCoreApplication.translate("LoginWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.password_le.setToolTip(QCoreApplication.translate("LoginWindow", u"Enter password to Login", None))
#endif // QT_CONFIG(tooltip)
        self.password_le.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password...", None))
#if QT_CONFIG(tooltip)
        self.login_btn.setToolTip(QCoreApplication.translate("LoginWindow", u"Submit", None))
#endif // QT_CONFIG(tooltip)
        self.login_btn.setText(QCoreApplication.translate("LoginWindow", u"LOGIN", None))
#if QT_CONFIG(shortcut)
        self.login_btn.setShortcut(QCoreApplication.translate("LoginWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_4.setText(QCoreApplication.translate("LoginWindow", u"login to your account", None))
        self.label.setText("")
        self.checkBox_3.setText(QCoreApplication.translate("LoginWindow", u"Remember me", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Forgot Password ?", None))
        self.toolButton.setText("")
    # retranslateUi

