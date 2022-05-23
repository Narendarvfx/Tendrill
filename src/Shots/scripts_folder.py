import os
from pathlib import Path

from PySide2 import QtWidgets, QtGui
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QTreeWidgetItem

class Scripts_Folder(object):
    def __init__(self):
        super(Scripts_Folder, self).__init__()


    def addPScriptsTree_widget(self):
        self.main_window.ui.Pscripts_treeWid.clear()
        try:
            self.main_window.ui.Pscripts_treeWid.itemClicked.disconnect()
        except:
            pass
        type = "_paint"
        self.main_window.ui.Pscripts_treeWid.itemClicked.connect(lambda : Scripts_Folder.scriptsItemClicked(self, type))
        pheader = self.main_window.ui.Pscripts_treeWid.header()
        pheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        paint_scripts_folders = os.path.join(self.base_Path + '_paint\\scripts\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        try:
            if not os.listdir(paint_scripts_folders) == []:
                j = 0
                for scriptFolder in os.listdir(paint_scripts_folders):
                    joint_script_folder = os.path.join(paint_scripts_folders, scriptFolder)
                    ignore = {".autosave"}
                    for folder in os.listdir(joint_script_folder):
                        f = os.path.join(joint_script_folder, str(folder))
                        if not os.listdir(f) == []:
                            shot_folder = max(os.listdir(f))
                            paint_item = QTreeWidgetItem([1, shot_folder])
                            self.main_window.ui.Pscripts_treeWid.addTopLevelItem(paint_item)
                            pixmap = QtGui.QPixmap(":/custom/icons/custom/" + shot_folder.split('.')[-1] + ".png")
                            soft_icon = QtGui.QIcon()
                            soft_icon.addPixmap(pixmap)
                            paint_item.setIcon(0, soft_icon)
                            paint_item.setIcon(4, folder_icon)
                            paint_item.setFont(1, QFont('Cambria', 10, QFont.Bold))
                            paint_item.setData(0, Qt.UserRole, os.path.join(f, shot_folder))
                            paint_item.setData(1, Qt.UserRole, os.path.join(f, shot_folder))
                            paint_item.setData(4, Qt.UserRole, f)
                i = 0
                for in_scriptFolder in os.listdir(paint_scripts_folders):
                    joint_folder = os.path.join(paint_scripts_folders, in_scriptFolder)
                    for folder in os.listdir(joint_folder):
                        f = os.path.join(joint_folder, folder)
                        if not os.listdir(f) == []:
                            for file in (sorted(os.listdir(f), reverse=True)):
                                p_child_item = QTreeWidgetItem([1, file])
                                self.main_window.ui.Pscripts_treeWid.topLevelItem(i).addChild(p_child_item)
                                p_child_item.setData(1, Qt.UserRole, os.path.join(f, file))
                            i += 1
        except Exception as e:
            pass

    def addRScriptsTree_widget(self):
        self.main_window.ui.Rscripts_treeWid.clear()
        try:
            self.main_window.ui.Rscripts_treeWid.itemClicked.disconnect()
        except:
            pass
        type = "_roto"
        self.main_window.ui.Rscripts_treeWid.itemClicked.connect(lambda : Scripts_Folder.scriptsItemClicked(self, type))
        rheader = self.main_window.ui.Rscripts_treeWid.header()
        rheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        ### Roto Script folders
        roto_scripts_folders = os.path.join(self.base_Path + '_roto\\scripts\\')
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        try:
            if not os.listdir(roto_scripts_folders) == []:
                for scriptFolder in os.listdir(roto_scripts_folders):
                    joint_script_folder = os.path.join(roto_scripts_folders, scriptFolder)
                    for folder in os.listdir(joint_script_folder):
                        f = os.path.join(joint_script_folder, str(folder))
                        if not os.listdir(f) == []:
                            shot_folder = max(os.listdir(f))
                            roto_item = QTreeWidgetItem([1, shot_folder])
                            self.main_window.ui.Rscripts_treeWid.addTopLevelItem(roto_item)
                            pixmap = QtGui.QPixmap(":/custom/icons/custom/" + shot_folder.split('.')[-1] + ".png")
                            soft_icon = QtGui.QIcon()
                            soft_icon.addPixmap(pixmap)
                            roto_item.setIcon(0, soft_icon)
                            # item_0.setIcon(3, soft_icon)
                            roto_item.setIcon(4, folder_icon)
                            roto_item.setFont(1, QFont('Cambria', 10, QFont.Bold))
                            roto_item.setData(0, Qt.UserRole, os.path.join(f, shot_folder))
                            roto_item.setData(1, Qt.UserRole, os.path.join(f, shot_folder))
                            roto_item.setData(4, Qt.UserRole, f)
                i = 0
                for in_scriptFolder in os.listdir(roto_scripts_folders):
                    joint_folder = os.path.join(roto_scripts_folders, in_scriptFolder)
                    for folder in os.listdir(joint_folder):
                        f = os.path.join(joint_folder, folder)
                        if not os.listdir(f) == []:
                            for file in (sorted(os.listdir(f), reverse=True)):
                                r_child_item = QTreeWidgetItem([1, file])
                                self.main_window.ui.Rscripts_treeWid.topLevelItem(i).addChild(r_child_item)
                                r_child_item.setData(1, Qt.UserRole, os.path.join(f, file))
                            i += 1
        except Exception as e:
            pass

    def addMScriptsTree_widget(self):
        self.main_window.ui.Mscripts_treeWid.clear()
        try:
            self.main_window.ui.Mscripts_treeWid.itemClicked.disconnect()
        except:
            pass
        type = "_mm"
        self.main_window.ui.Mscripts_treeWid.itemClicked.connect(lambda : Scripts_Folder.scriptsItemClicked(self, type))
        ### MM Script folders
        mm_scripts_folders = os.path.join(self.base_Path + '_mm\\scripts\\')
        soft_icon = QtGui.QIcon()
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        try:
            if not os.listdir(mm_scripts_folders) == []:
                for scriptFolder in os.listdir(mm_scripts_folders):
                    joint_script_folder = os.path.join(mm_scripts_folders, scriptFolder)
                    for folder in os.listdir(joint_script_folder):
                        f = os.path.join(joint_script_folder, str(folder))
                        if not os.listdir(f) == []:
                            shot_folder = max(os.listdir(f))
                            pixmap = QtGui.QPixmap(":/custom/icons/custom/" + shot_folder.split('.')[-1] + ".png")
                            soft_icon.addPixmap(pixmap)
                            mm_item = QTreeWidgetItem([1, shot_folder])
                            self.main_window.ui.Mscripts_treeWid.addTopLevelItem(mm_item)
                            mm_item.setIcon(0, soft_icon)
                            # item_0.setIcon(3, soft_icon)
                            mm_item.setIcon(4, folder_icon)
                            mm_item.setFont(1, QFont('Cambria', 10, QFont.Bold))
                            mm_item.setData(0, Qt.UserRole, os.path.join(f, shot_folder))
                            mm_item.setData(1, Qt.UserRole, os.path.join(f, shot_folder))
                            mm_item.setData(4, Qt.UserRole, f)
                i = 0
                for in_scriptFolder in os.listdir(mm_scripts_folders):
                    joint_folder = os.path.join(mm_scripts_folders, in_scriptFolder)
                    for folder in os.listdir(joint_folder):
                        f = os.path.join(joint_folder, folder)
                        if not os.listdir(f) == []:
                            for file in (sorted(os.listdir(f), reverse=True)):
                                m_child_item = QTreeWidgetItem([1, file])
                                self.main_window.ui.Mscripts_treeWid.topLevelItem(i).addChild(m_child_item)
                                m_child_item.setData(1, Qt.UserRole, os.path.join(f, file))
                            i += 1
        except Exception as e:
            pass


    def scriptsItemClicked(self, type):
        if type == '_paint':
            currentIndex = self.main_window.ui.Pscripts_treeWid.currentIndex()
            col = currentIndex.column()
            p = self.main_window.ui.Pscripts_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(p)
        elif type=='_roto':
            currentIndex = self.main_window.ui.Rscripts_treeWid.currentIndex()
            col = currentIndex.column()
            r = self.main_window.ui.Rscripts_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(r)
        elif type=='_mm':
            currentIndex = self.main_window.ui.Mscripts_treeWid.currentIndex()
            col = currentIndex.column()
            m = self.main_window.ui.Mscripts_treeWid.currentItem().data(col, Qt.UserRole)
            os.startfile(m)
