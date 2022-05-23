# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shots_ingest_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_ShotsIngestProgressDialog(object):
    def setupUi(self, ShotsIngestProgressDialog):
        if not ShotsIngestProgressDialog.objectName():
            ShotsIngestProgressDialog.setObjectName(u"ShotsIngestProgressDialog")
        ShotsIngestProgressDialog.resize(484, 370)
        self.verticalLayout = QVBoxLayout(ShotsIngestProgressDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ShotsIngestProgressDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.shot_ingest_progress_bar = QProgressBar(self.frame)
        self.shot_ingest_progress_bar.setObjectName(u"shot_ingest_progress_bar")
        self.shot_ingest_progress_bar.setValue(99)

        self.verticalLayout_2.addWidget(self.shot_ingest_progress_bar)


        self.verticalLayout.addWidget(self.frame)

        self.shot_textBrowser = QTextBrowser(ShotsIngestProgressDialog)
        self.shot_textBrowser.setObjectName(u"shot_textBrowser")

        self.verticalLayout.addWidget(self.shot_textBrowser)

        self.buttonBox = QDialogButtonBox(ShotsIngestProgressDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ShotsIngestProgressDialog)
        self.buttonBox.accepted.connect(ShotsIngestProgressDialog.accept)
        self.buttonBox.rejected.connect(ShotsIngestProgressDialog.reject)

        QMetaObject.connectSlotsByName(ShotsIngestProgressDialog)
    # setupUi

    def retranslateUi(self, ShotsIngestProgressDialog):
        ShotsIngestProgressDialog.setWindowTitle(QCoreApplication.translate("ShotsIngestProgressDialog", u"Dialog", None))
    # retranslateUi

