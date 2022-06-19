import os
from pathlib import Path
import win32security
from PySide2 import QtWidgets, QtGui
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QTreeWidgetItem
import datetime

class Scripts_Folder(object):
    def __init__(self):
        super(Scripts_Folder, self).__init__()


    def addPScriptsTree_widget(self):
        self.main_window.ui.Pscripts_treeWid.clear()
        try:
            self.main_window.ui.Pscripts_treeWid.itemClicked.disconnect()
        except:
            pass
        type = "paint"
        self.main_window.ui.Pscripts_treeWid.setColumnCount(7)
        self.main_window.ui.Pscripts_treeWid.itemDoubleClicked.connect(lambda : Scripts_Folder.scriptsItemClicked(self, type))
        pheader = self.main_window.ui.Pscripts_treeWid.header()

        pheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        paint_scripts_folders = os.path.join(self.base_Path + '\\paint\\scripts\\')
        print (paint_scripts_folders)
        folder_icon = QtGui.QIcon()
        folder_icon.addPixmap(QtGui.QPixmap(":/custom/icons/custom/folder-icon.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        file_icon = QtGui.QIcon()
        file_icon.addPixmap(QtGui.QPixmap(":/24x24/icons/24x24/cil-file.png"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)

        try:
            if not os.listdir(paint_scripts_folders) == []:
                for folder_name in os.listdir(paint_scripts_folders):  # [denoise, plates]
                    item_0 = QTreeWidgetItem([folder_name.upper()])
                    self.main_window.ui.Pscripts_treeWid.addTopLevelItem(item_0)
                    item_0.setData(0, Qt.UserRole, os.path.join(paint_scripts_folders, folder_name))
                    item_0.setTextColor(0, Qt.darkYellow)
                    item_0.setFont(0, QFont('Arial', 10, QFont.Bold))
                    item_0.setIcon(2, folder_icon)
                    app_files = os.listdir(os.path.join(paint_scripts_folders, folder_name))
                    for each_file in app_files:
                        print (each_file)
                        file_path = os.path.join(paint_scripts_folders, folder_name, each_file)
                        print ("sub_folder>>", file_path)
                        if os.path.isfile(file_path):
                            sub = QTreeWidgetItem(item_0, [os.path.basename(file_path)])
                            sub.setTextColor(0, Qt.darkGreen)
                            sub.setData(0, Qt.UserRole, file_path)
                            pixmap = QtGui.QPixmap(":/custom/icons/custom/" + file_path.split('.')[-1] + ".png")
                            soft_icon = QtGui.QIcon()
                            soft_icon.addPixmap(pixmap)
                            sub.setIcon(0, soft_icon)
                            sub.setIcon(2, file_icon)
                            sub.setFont(1, QFont('Arial', 10, QFont.Bold))
                            sub.setText(3, str(os.path.getsize(file_path)))
                            # owner=  Scripts_Folder.get_owner(self,file_path)

                            date_created = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

                            # sub.setText(4, owner)
                            sub.setText(5, str(date_created.date()))
                            sub.setText(6, str(date_created.time()).split('.')[0])
                            # sub.setData(4, Qt.UserRole, file_path)
                # for scriptFolder in os.listdir(paint_scripts_folders):
                #     print (scriptFolder)
                #     joint_script_folder = os.path.join(paint_scripts_folders, scriptFolder)
                #
                #     ignore = {".autosave"}
                #     for folder in os.listdir(joint_script_folder):
                #         f = os.path.join(joint_script_folder, str(folder))
                #         print(f)
                #         if not os.listdir(f) == []:
                #             shot_folder = max(os.listdir(f))
                #             paint_item = QTreeWidgetItem([1, shot_folder])
                #             self.main_window.ui.Pscripts_treeWid.addTopLevelItem(paint_item)
                #             pixmap = QtGui.QPixmap(":/custom/icons/custom/" + shot_folder.split('.')[-1] + ".png")
                #             soft_icon = QtGui.QIcon()
                #             soft_icon.addPixmap(pixmap)
                #             paint_item.setIcon(0, soft_icon)
                #             paint_item.setIcon(4, folder_icon)
                #             paint_item.setFont(1, QFont('Cambria', 10, QFont.Bold))
                #             paint_item.setData(0, Qt.UserRole, os.path.join(f, shot_folder))
                #             paint_item.setData(1, Qt.UserRole, os.path.join(f, shot_folder))
                #             paint_item.setData(4, Qt.UserRole, f)
                # i = 0
                # for in_scriptFolder in os.listdir(paint_scripts_folders):
                #     joint_folder = os.path.join(paint_scripts_folders, in_scriptFolder)
                #     for folder in os.listdir(joint_folder):
                #         f = os.path.join(joint_folder, folder)
                #         if not os.listdir(f) == []:
                #             for file in (sorted(os.listdir(f), reverse=True)):
                #                 p_child_item = QTreeWidgetItem([1, file])
                #                 self.main_window.ui.Pscripts_treeWid.topLevelItem(i).addChild(p_child_item)
                #                 p_child_item.setData(1, Qt.UserRole, os.path.join(f, file))
                #             i += 1
        except Exception as e:
            print ("exce >>>", e)
            pass

    def get_owner(self,FILENAME):
        open(FILENAME, "r").close()
        sd = win32security.GetFileSecurity(FILENAME, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, type = win32security.LookupAccountSid(None, owner_sid)
        return name
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
        type = "mm"
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
        if type == 'paint':
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
