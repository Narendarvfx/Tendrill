# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'team_list_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Team_List_Dialog(object):
    def setupUi(self, Team_List_Dialog):
        if not Team_List_Dialog.objectName():
            Team_List_Dialog.setObjectName(u"Team_List_Dialog")
        Team_List_Dialog.resize(533, 333)
        Team_List_Dialog.setMinimumSize(QSize(533, 333))
        Team_List_Dialog.setMaximumSize(QSize(533, 333))

        Team_List_Dialog.setSizeGripEnabled(False)
        Team_List_Dialog.setModal(True)
        self.gridLayout = QGridLayout(Team_List_Dialog)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(Team_List_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.shotName_lbl = QLabel(self.frame)
        self.shotName_lbl.setObjectName(u"shotName_lbl")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.shotName_lbl.setFont(font)
        self.shotName_lbl.setStyleSheet(u"color:white;\n"
"border:none;")
        self.shotName_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.shotName_lbl, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.close_btn = QPushButton(self.frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"background:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/24x24/icons/24x24/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setFlat(False)

        self.gridLayout_2.addWidget(self.close_btn, 0, 3, 1, 1)

        self.team_tabWid = QTableWidget(self.frame)
        if (self.team_tabWid.columnCount() < 4):
            self.team_tabWid.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.team_tabWid.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.team_tabWid.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.team_tabWid.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.team_tabWid.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.team_tabWid.setObjectName(u"team_tabWid")

        self.team_tabWid.setFrameShape(QFrame.NoFrame)
        self.team_tabWid.setFrameShadow(QFrame.Raised)
        self.team_tabWid.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.team_tabWid.setAlternatingRowColors(True)
        self.team_tabWid.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.team_tabWid.setShowGrid(False)
        self.team_tabWid.setSortingEnabled(True)
        self.team_tabWid.horizontalHeader().setCascadingSectionResizes(True)
        self.team_tabWid.horizontalHeader().setStretchLastSection(True)
        self.team_tabWid.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.team_tabWid, 1, 0, 1, 4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Team_List_Dialog)

        QMetaObject.connectSlotsByName(Team_List_Dialog)
    # setupUi

    def retranslateUi(self, Team_List_Dialog):
        Team_List_Dialog.setWindowTitle(QCoreApplication.translate("Team_List_Dialog", u"Dialog", None))
        self.shotName_lbl.setText(QCoreApplication.translate("Team_List_Dialog", u"Shot 001", None))
        self.close_btn.setText("")
        ___qtablewidgetitem = self.team_tabWid.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Team_List_Dialog", u"ARTIST", None));
        ___qtablewidgetitem1 = self.team_tabWid.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Team_List_Dialog", u"MAN DAYS", None));
        ___qtablewidgetitem2 = self.team_tabWid.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Team_List_Dialog", u"COMPILER", None));
        ___qtablewidgetitem3 = self.team_tabWid.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Team_List_Dialog", u"ACTIONS", None));
    # retranslateUi

