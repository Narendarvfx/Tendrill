import datetime

from PySide2 import QtCore
from PySide2.QtCore import QPoint, QCoreApplication
from PySide2.QtGui import QColor, Qt, QFont
from PySide2.QtWidgets import QGraphicsDropShadowEffect, QFrame, QGridLayout, QLabel, QSpacerItem, QSizePolicy, \
    QPushButton

import api
from uipy.notifications.notifications import Ui_Form, QWidget


class popup(QWidget):
    def __init__(self, parent=None, widget=None):
        QWidget.__init__(self, parent)
        self.notify_ui = Ui_Form()
        self.notify_ui.setupUi(self)
        self.employee_details = parent.employee_details
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
        # calculate the bottom right point from the parents rectangle
        point = widget.rect().bottomRight()

        # map that point as a global position
        global_point = widget.mapToGlobal(point)

        # by default, a widget will be placed from its top-left corner, so
        # we need to move it to the left based on the widgets width
        self.move(global_point - QPoint(self.width(), 0))

        self.addNotification()

    def addNotification(self):
        notification_data = api.getunreadNotifications(str(self.employee_details['id']))
        for i, data in enumerate(notification_data):
            self.frame = QFrame(self.notify_ui.scrollAreaWidgetContents)
            frame = "frame_"+str(i)
            self.frame.setObjectName(frame)
            self.frame.setStyleSheet(u"QFrame{\n"
                                       "background-color: rgb(27, 31, 38);\n"
                                       "border:1px solid rgb(44, 49, 60);\n"
                                       "border-radius:5px\n"
                                       "}")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.gridLayout = QGridLayout(self.frame)
            self.gridLayout.setObjectName(u"gridLayout")
            self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

            self.label_1 = QLabel(self.frame)
            self.label_1.setObjectName(u"label1")
            self.label_1.setStyleSheet(u"border:none;")

            self.gridLayout.addWidget(self.label_1, 3, 0, 1, 1)

            self.pushButton = QPushButton(self.frame)
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.setStyleSheet(u"background-color: none;\n"
                                          "padding:5px;\n"
                                          "color:white\n"
                                          "")
            self.pushButton.setFlat(True)

            self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

            self.label = QLabel(self.frame)
            self.label.setObjectName(u"label")
            font = QFont()
            font.setFamily(u"Segoe UI")
            font.setPointSize(11)
            self.label.setFont(font)
            self.label.setStyleSheet(u"border:none;\n"
                                     "color: rgb(240, 240, 240);")
            self.label.setWordWrap(True)

            self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

            self.notify_ui.verticalLayout_3.addWidget(self.frame)
            sent_date = datetime.datetime.strptime(data['sent_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d-%m-%Y %H:%M")
            self.label_1.setText(QCoreApplication.translate("Form", str(sent_date), None))
            self.pushButton.setText(QCoreApplication.translate("Form", data['status'], None))
            self.label.setText(QCoreApplication.translate("Form", data['message'], None))
            # self.pushButton.clicked.connect(lambda: self.clearFrame(self.frame))

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.notify_ui.verticalLayout_3.addItem(self.verticalSpacer)

    def clearFrame(self, frame):
        # self.notify_ui.verticalLayout_3.removeWidget(self.frame)
        frame.setStyleSheet('background-color:green')
