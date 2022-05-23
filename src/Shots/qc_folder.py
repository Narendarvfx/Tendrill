import os

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTreeWidgetItem


class Qc_Folder(object):
    def __init__(self):
        super(Qc_Folder, self).__init__()

    def Pqc_Folder(self):
        self.main_window.ui.Pqc_treeWid.clear()
        try:
            self.main_window.ui.Pqc_treeWid.itemClicked.disconnect()
        except Exception as e:
            pass
        header = self.main_window.ui.Pqc_treeWid.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.main_window.ui.Pqc_treeWid.setAlternatingRowColors(True)
        qc_Folder = os.path.join(self.base_Path + '_paint\\qc\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        i = 0
        try:
            for artist_folder in os.listdir(qc_Folder):
                if artist_folder != 'internal_retake':
                    joint_folder = os.path.join(qc_Folder, artist_folder)
                    if not os.listdir(joint_folder) == []:
                        for folder in sorted(os.listdir(joint_folder), reverse=True):
                            item = QTreeWidgetItem([folder])
                            self.main_window.ui.Pqc_treeWid.addTopLevelItem(item)
                            item.setIcon(2, folder_icon)
                            item.setData(2, Qt.UserRole, os.path.join(joint_folder, folder))
                            item.setIcon(4, folder_icon)
                            item.setToolTip(4, 'Retake Folder')
                            item.setData(4, Qt.UserRole, os.path.join(qc_Folder, 'internal_retake', folder))

                        i += 1
        except Exception as e:
            pass
        type = '_paint'
        self.main_window.ui.Pqc_treeWid.itemClicked.connect(lambda: Qc_Folder.onQcItemClicked(self, type))

    def Rqc_Folder(self):
        self.main_window.ui.Rqc_treeWid.clear()
        try:
            self.main_window.ui.Rqc_treeWid.itemClicked.disconnect()
        except Exception as e:
            pass
        header = self.main_window.ui.Rqc_treeWid.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.main_window.ui.Rqc_treeWid.setAlternatingRowColors(True)
        qc_Folder = os.path.join(self.base_Path + '_roto\\qc\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        i = 0
        try:
            for artist_folder in os.listdir(qc_Folder):
                if artist_folder != 'internal_retake':
                    joint_folder = os.path.join(qc_Folder, artist_folder)
                    if not os.listdir(joint_folder) == []:
                        for folder in sorted(os.listdir(joint_folder), reverse=True):
                            item = QTreeWidgetItem([folder])
                            self.main_window.ui.Rqc_treeWid.addTopLevelItem(item)
                            item.setIcon(2, folder_icon)
                            item.setData(2, Qt.UserRole, os.path.join(joint_folder, folder))
                            item.setIcon(4, folder_icon)
                            item.setToolTip(4, 'Retake Folder')
                            item.setData(4, Qt.UserRole, os.path.join(qc_Folder, 'internal_retake', folder))

                        i += 1
        except Exception as e:
            pass

        type = '_roto'
        self.main_window.ui.Rqc_treeWid.itemClicked.connect(lambda: Qc_Folder.onQcItemClicked(self, type))

    def Mqc_Folder(self):
        self.main_window.ui.Mqc_treeWid.clear()
        try:
            self.main_window.ui.Mqc_treeWid.itemClicked.disconnect()
        except Exception as e:
            pass
        header = self.main_window.ui.Mqc_treeWid.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.main_window.ui.Mqc_treeWid.setAlternatingRowColors(True)
        qc_Folder = os.path.join(self.base_Path + '_mm\\qc\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        i = 0
        try:
            for artist_folder in os.listdir(qc_Folder):
                if artist_folder != 'internal_retake':
                    joint_folder = os.path.join(qc_Folder, artist_folder)
                    if not os.listdir(joint_folder) == []:
                        for folder in sorted(os.listdir(joint_folder), reverse=True):
                            item = QTreeWidgetItem([folder])
                            self.main_window.ui.Mqc_treeWid.addTopLevelItem(item)
                            item.setIcon(2, folder_icon)
                            item.setData(2, Qt.UserRole, os.path.join(joint_folder, folder))
                            item.setIcon(4, folder_icon)
                            item.setToolTip(4, 'Retake Folder')
                            item.setData(4, Qt.UserRole, os.path.join(qc_Folder, 'internal_retake', folder))

                        i += 1
        except Exception as e:
            pass
        type = '_mm'
        self.main_window.ui.Mqc_treeWid.itemClicked.connect(lambda: Qc_Folder.onQcItemClicked(self, type))

    def onQcItemClicked(self, type):
        if type == '_paint':
            currentIndex = self.main_window.ui.Pqc_treeWid.currentIndex()
            col = currentIndex.column()
            p = self.main_window.ui.Pqc_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(p)
        elif type=='_roto':
            currentIndex = self.main_window.ui.Rqc_treeWid.currentIndex()
            col = currentIndex.column()
            r = self.main_window.ui.Rqc_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(r)
        elif type=='_mm':
            currentIndex = self.main_window.ui.Mqc_treeWid.currentIndex()
            col = currentIndex.column()
            m = self.main_window.ui.Mqc_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(m)