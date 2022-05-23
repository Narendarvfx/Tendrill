# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'succes_dialog.ui'
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


class Ui_msg_dialog(object):
    def setupUi(self, msg_dialog):
        if not msg_dialog.objectName():
            msg_dialog.setObjectName(u"msg_dialog")
        msg_dialog.resize(349, 68)
        msg_dialog.setMinimumSize(QSize(0, 68))
        msg_dialog.setMaximumSize(QSize(16777215, 68))
        self.gridLayout = QGridLayout(msg_dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.display_frame = QFrame(msg_dialog)
        self.display_frame.setObjectName(u"display_frame")
        self.display_frame.setStyleSheet(u"background-color: rgb(14, 198, 4);")
        self.display_frame.setFrameShape(QFrame.StyledPanel)
        self.display_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.display_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.display_msg = QLabel(self.display_frame)
        self.display_msg.setObjectName(u"display_msg")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        self.display_msg.setFont(font)
        self.display_msg.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_2.addWidget(self.display_msg, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.display_frame, 0, 0, 1, 1)


        self.retranslateUi(msg_dialog)

        QMetaObject.connectSlotsByName(msg_dialog)
    # setupUi

    def retranslateUi(self, msg_dialog):
        msg_dialog.setWindowTitle(QCoreApplication.translate("msg_dialog", u"Dialog", None))
        self.display_msg.setText(QCoreApplication.translate("msg_dialog", u"     Project Created Succesfully!!", None))
    # retranslateUi

