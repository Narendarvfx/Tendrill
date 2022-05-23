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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(717, 410)
        Form.setStyleSheet(u"QFrame{\n"
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
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 721, 411))
        self.label.setPixmap(QPixmap(u":/custom/icons/custom/Dark Full Hd Wallpaper.jpg"))
        self.label.setScaledContents(True)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 110, 321, 211))
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 80, 251, 2))
        self.line_3.setMaximumSize(QSize(16777215, 2))
        self.line_3.setStyleSheet(u"background-color: rgb(127, 127, 127);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 40, 251, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_2 = QToolButton(self.layoutWidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setStyleSheet(u"border: 0px;\n"
"")
        icon = QIcon()
        icon.addFile(u":/custom/icons/custom/baseline_account_circle_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.username_le = QLineEdit(self.layoutWidget)
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

        self.horizontalLayout.addWidget(self.username_le)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 100, 251, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButton_3 = QToolButton(self.layoutWidget1)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setStyleSheet(u"border: 0px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/custom/icons/custom/baseline_lock_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.toolButton_3)

        self.password_le = QLineEdit(self.layoutWidget1)
        self.password_le.setObjectName(u"password_le")
        self.password_le.setMinimumSize(QSize(0, 40))
        self.password_le.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.password_le.setFont(font1)
        self.password_le.setFocusPolicy(Qt.ClickFocus)
        self.password_le.setStyleSheet(u"")
        self.password_le.setEchoMode(QLineEdit.Password)
        self.password_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.password_le)

        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 160, 251, 36))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.login_btn = QPushButton(self.layoutWidget2)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMaximumSize(QSize(16777215, 30))
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

        self.horizontalLayout_3.addWidget(self.login_btn)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(45, 0, 251, 31))
        self.lineEdit_2.setStyleSheet(u"font: 10pt \"Arial\";")
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(60, 250, 251, 2))
        self.line_4.setMaximumSize(QSize(16777215, 2))
        self.line_4.setStyleSheet(u"background-color: rgb(127, 127, 127);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.layoutWidget3 = QWidget(Form)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(60, 310, 254, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")

        self.horizontalLayout_4.addWidget(self.checkBox)

        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, 50, 201, 81))
        self.frame_2.setStyleSheet(u"image: url(:/custom/icons/custom/tendril.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.toolButton_2.setText(QCoreApplication.translate("Form", u"...", None))
        self.username_le.setPlaceholderText(QCoreApplication.translate("Form", u"User Name", None))
        self.toolButton_3.setText(QCoreApplication.translate("Form", u"...", None))
#if QT_CONFIG(tooltip)
        self.password_le.setToolTip(QCoreApplication.translate("Form", u"Enter password to Login", None))
#endif // QT_CONFIG(tooltip)
        self.password_le.setPlaceholderText(QCoreApplication.translate("Form", u"Password...", None))
#if QT_CONFIG(tooltip)
        self.login_btn.setToolTip(QCoreApplication.translate("Form", u"Submit", None))
#endif // QT_CONFIG(tooltip)
        self.login_btn.setText(QCoreApplication.translate("Form", u"LOGIN", None))
#if QT_CONFIG(shortcut)
        self.login_btn.setShortcut(QCoreApplication.translate("Form", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"login to your account", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Remember me", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Forgot Password ?", None))
    # retranslateUi
