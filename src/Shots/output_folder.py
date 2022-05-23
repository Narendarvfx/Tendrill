import os

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTreeWidgetItem


class Output_Folder(object):
    def __init__(self):
        super(Output_Folder, self).__init__()

    def Poutput_folder(self):
        self.main_window.ui.Poutput_treeWid.clear()
        try:
            self.main_window.ui.Poutput_treeWid.itemClicked.disconnect()
        except:
            pass
        type='_paint'
        self.main_window.ui.Poutput_treeWid.itemClicked.connect(lambda : Output_Folder.outputItemClicked(self, type))
        pheader = self.main_window.ui.Poutput_treeWid.header()
        pheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        ## Paint Output Folder
        Poutput_Folder = os.path.join(self.base_Path + '_paint\\output\\')
        folder_icon = QtGui.QIcon()
        stc_icon = QtGui.QIcon()  ## Send to Compiler
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        try:
            for artist_folder in os.listdir(Poutput_Folder):
                final_out = os.path.join(Poutput_Folder, str(artist_folder))
                if not os.listdir(final_out) == []:
                    out_folder = max(os.listdir(final_out))
                    item_0 = QTreeWidgetItem([out_folder])
                    item_0.setFont(0, QFont('Cambria', 10, QFont.Bold))
                    self.main_window.ui.Poutput_treeWid.addTopLevelItem(item_0)
                    item_0.setIcon(4, folder_icon)
                    item_0.setData(4, Qt.UserRole, os.path.join(Poutput_Folder, artist_folder))

            p = 0
            for artist_folder in os.listdir(Poutput_Folder):
                joint_folder = os.path.join(Poutput_Folder, artist_folder)
                if not os.listdir(joint_folder) == []:
                    for folder in sorted(os.listdir(joint_folder), reverse=True):
                        item = QTreeWidgetItem([folder])
                        self.main_window.ui.Poutput_treeWid.topLevelItem(p).addChild(item)
                        item.setIcon(3, folder_icon)
                        item.setData(3, Qt.UserRole, os.path.join(joint_folder, folder))
                    p += 1
        except Exception as e:
            pass

    def Routput_folder(self):
        self.main_window.ui.Routput_treeWid.clear()
        try:
            self.main_window.ui.Routput_treeWid.itemClicked.disconnect()
        except:
            pass
        type='_roto'
        self.main_window.ui.Routput_treeWid.itemClicked.connect(lambda : Output_Folder.outputItemClicked(self, type))
        rheader = self.main_window.ui.Routput_treeWid.header()
        rheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        ## Roto Output Folder
        Routput_Folder = os.path.join(self.base_Path + '_roto\\output\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        try:
            for artist_folder in os.listdir(Routput_Folder):
                final_out = os.path.join(Routput_Folder, str(artist_folder))
                if not os.listdir(final_out) == []:
                    out_folder = max(os.listdir(final_out))
                    item_0 = QTreeWidgetItem([out_folder])
                    item_0.setFont(0, QFont('Cambria', 10, QFont.Bold))
                    self.main_window.ui.Routput_treeWid.addTopLevelItem(item_0)
                    item_0.setIcon(4, folder_icon)
                    item_0.setData(4, Qt.UserRole, os.path.join(Routput_Folder, artist_folder))

            r = 0
            for artist_folder in os.listdir(Routput_Folder):
                joint_folder = os.path.join(Routput_Folder, artist_folder)
                if not os.listdir(joint_folder) == []:
                    for folder in sorted(os.listdir(joint_folder), reverse=True):
                        item = QTreeWidgetItem([folder])
                        self.main_window.ui.Routput_treeWid.topLevelItem(r).addChild(item)
                        item.setIcon(3, folder_icon)
                        item.setData(3, Qt.UserRole, os.path.join(joint_folder, folder))
                    r += 1
        except Exception as e:
            pass

    def Moutput_folder(self):
        self.main_window.ui.Moutput_treeWid.clear()
        try:
            self.main_window.ui.Moutput_treeWid.itemClicked.disconnect()
        except:
            pass
        type='_mm'
        self.main_window.ui.Moutput_treeWid.itemClicked.connect(lambda : Output_Folder.outputItemClicked(self, type))
        mheader = self.main_window.ui.Moutput_treeWid.header()
        mheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        ## MM Output Folder
        Moutput_Folder = os.path.join(self.base_Path + '_mm\\output\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        try:
            for artist_folder in os.listdir(Moutput_Folder):
                final_out = os.path.join(Moutput_Folder, str(artist_folder))
                if not os.listdir(final_out) == []:
                    out_folder = max(os.listdir(final_out))
                    item_0 = QTreeWidgetItem([out_folder])
                    item_0.setFont(0, QFont('Cambria', 10, QFont.Bold))
                    self.main_window.ui.Moutput_treeWid.addTopLevelItem(item_0)
                    item_0.setIcon(4, folder_icon)
                    item_0.setData(4, Qt.UserRole, os.path.join(Moutput_Folder, artist_folder))

            m = 0
            for artist_folder in os.listdir(Moutput_Folder):
                joint_folder = os.path.join(Moutput_Folder, artist_folder)
                if not os.listdir(joint_folder) == []:
                    for folder in sorted(os.listdir(joint_folder), reverse=True):
                        item = QTreeWidgetItem([folder])
                        self.main_window.ui.Moutput_treeWid.topLevelItem(m).addChild(item)
                        item.setIcon(3, folder_icon)
                        item.setData(3, Qt.UserRole, os.path.join(joint_folder, folder))
                    m += 1
        except Exception as e:
            pass

    def outputItemClicked(self, type):
        if type == '_paint':
            currentIndex = self.main_window.ui.Poutput_treeWid.currentIndex()
            col = currentIndex.column()
            p = self.main_window.ui.Poutput_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(p)
        elif type=='_roto':
            currentIndex = self.main_window.ui.Routput_treeWid.currentIndex()
            col = currentIndex.column()
            r = self.main_window.ui.Routput_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(r)
        elif type=='_mm':
            currentIndex = self.main_window.ui.Moutput_treeWid.currentIndex()
            col = currentIndex.column()
            m = self.main_window.ui.Moutput_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(m)