import os

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTreeWidgetItem

class PreRenders_Folder(object):
    def __init__(self):
        super(PreRenders_Folder, self).__init__()

    def Ppre_renders_folder(self):
        self.main_window.ui.Ppre_ren_treeWid.clear()
        try:
            self.main_window.ui.Ppre_ren_treeWid.itemClicked.disconnect()
        except:
            pass
        type='_paint'
        self.main_window.ui.Ppre_ren_treeWid.itemClicked.connect(lambda: PreRenders_Folder.onPrerenderItemClicked(self,type))
        pheader = self.main_window.ui.Ppre_ren_treeWid.header()
        pheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        PpreRenders_Folder = os.path.join(self.base_Path + '_paint\\pre_renders\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        try:
            for artist_folder in os.listdir(PpreRenders_Folder):
                final_folder = os.path.join(PpreRenders_Folder, str(artist_folder))
                if not os.listdir(final_folder) == []:
                    pre_folder = max(os.listdir(final_folder))
                    item_0 = QTreeWidgetItem([pre_folder])
                    self.main_window.ui.Ppre_ren_treeWid.addTopLevelItem(item_0)
                    item_0.setIcon(4, folder_icon)
                    item_0.setFont(0, QFont('Cambria', 10, QFont.Bold))
                    item_0.setData(4, Qt.UserRole, os.path.join(PpreRenders_Folder, artist_folder))
            p = 0
            for artist_folder in os.listdir(PpreRenders_Folder):
                joint_folder = os.path.join(PpreRenders_Folder, artist_folder)
                if not os.listdir(joint_folder) == []:
                    for folder in sorted(os.listdir(joint_folder), reverse=True):
                        item = QTreeWidgetItem([folder])
                        self.main_window.ui.Ppre_ren_treeWid.topLevelItem(p).addChild(item)
                        item.setIcon(3, folder_icon)
                        item.setData(3, Qt.UserRole, os.path.join(joint_folder, folder))
                    p += 1
        except Exception as e:
            pass

    def Rpre_renders_folder(self):
        self.main_window.ui.Rpre_ren_treeWid.clear()
        try:
            self.main_window.ui.Rpre_ren_treeWid.itemClicked.disconnect()
        except:
            pass
        type ='_roto'
        self.main_window.ui.Rpre_ren_treeWid.itemClicked.connect(lambda: PreRenders_Folder.onPrerenderItemClicked(self, type))
        rheader = self.main_window.ui.Rpre_ren_treeWid.header()
        rheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        ### Roto PreRenders
        RpreRenders_Folder = os.path.join(self.base_Path + '_roto\\pre_renders\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        try:
            for artist_folder in os.listdir(RpreRenders_Folder):
                final_folder = os.path.join(RpreRenders_Folder, str(artist_folder))
                if not os.listdir(final_folder) == []:
                    pre_folder = max(os.listdir(final_folder))
                    item_0 = QTreeWidgetItem([pre_folder])
                    item_0.setFont(0, QFont('Cambria', 10, QFont.Bold))
                    self.main_window.ui.Rpre_ren_treeWid.addTopLevelItem(item_0)
                    item_0.setIcon(4, folder_icon)
                    item_0.setData(4, Qt.UserRole, os.path.join(RpreRenders_Folder, artist_folder))
            r = 0
            for artist_folder in os.listdir(RpreRenders_Folder):
                joint_folder = os.path.join(RpreRenders_Folder, artist_folder)
                if not os.listdir(joint_folder) == []:
                    for folder in sorted(os.listdir(joint_folder), reverse=True):
                        item = QTreeWidgetItem([folder])
                        self.main_window.ui.Rpre_ren_treeWid.topLevelItem(r).addChild(item)
                        item.setIcon(3, folder_icon)
                        item.setData(3, Qt.UserRole, os.path.join(joint_folder, folder))
                    r += 1
        except Exception as e:
            pass

    def Mpre_renders_folder(self):
        self.main_window.ui.Mpre_ren_treeWid.clear()
        try:
            self.main_window.ui.Mpre_ren_treeWid.itemClicked.disconnect()
        except:
            pass
        type = '_mm'
        self.main_window.ui.Mpre_ren_treeWid.itemClicked.connect(lambda :PreRenders_Folder.onPrerenderItemClicked(self, type))
        mheader = self.main_window.ui.Mpre_ren_treeWid.header()
        mheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        ### MM PreRenders
        MpreRenders_Folder = os.path.join(self.base_Path + '_mm\\pre_renders\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        try:
            for artist_folder in os.listdir(MpreRenders_Folder):
                final_folder = os.path.join(MpreRenders_Folder, str(artist_folder))
                if not os.listdir(final_folder) == []:
                    pre_folder = max(os.listdir(final_folder))
                    item_0 = QTreeWidgetItem([pre_folder])
                    item_0.setFont(0, QFont('Cambria', 10, QFont.Bold))
                    self.main_window.ui.Mpre_ren_treeWid.addTopLevelItem(item_0)
                    item_0.setIcon(4, folder_icon)
                    item_0.setData(4, Qt.UserRole, os.path.join(MpreRenders_Folder, artist_folder))
            m = 0
            for artist_folder in os.listdir(MpreRenders_Folder):
                joint_folder = os.path.join(MpreRenders_Folder, artist_folder)
                if not os.listdir(joint_folder) == []:
                    for folder in sorted(os.listdir(joint_folder), reverse=True):
                        item = QTreeWidgetItem([folder])
                        self.main_window.ui.Mpre_ren_treeWid.topLevelItem(m).addChild(item)
                        item.setIcon(3, folder_icon)
                        item.setData(3, Qt.UserRole, os.path.join(joint_folder, folder))
                    m += 1
        except Exception as e:
            pass

    def onPrerenderItemClicked(self, type):
        if type == '_paint':
            currentIndex = self.main_window.ui.Ppre_ren_treeWid.currentIndex()
            col = currentIndex.column()
            p = self.main_window.ui.Ppre_ren_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(p)
        elif type=='_roto':
            currentIndex = self.main_window.ui.Rpre_ren_treeWid.currentIndex()
            col = currentIndex.column()
            r = self.main_window.ui.Rpre_ren_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(r)
        elif type=='_mm':
            currentIndex = self.main_window.ui.Mpre_ren_treeWid.currentIndex()
            col = currentIndex.column()
            m = self.main_window.ui.Mpre_ren_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(m)