import os
from pathlib import Path
from functools import  partial
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QTreeWidgetItem

class Annotations_Folder(object):
    def __init__(self):
        super(Annotations_Folder, self).__init__()


    def addTask_Annotation_widget(self):
        self.ann_path = os.path.join(self.base_Path,self.shot_details['task_type'].lower(),'annotations')
        try:
            for i in range(self.main_window.ui.taskann.count()):
                self.main_window.ui.taskann.takeItem(i-1)
                self.main_window.ui.taskann.clear()
        except Exception as e:
            print ("EXCEPTION in MODEL>>>>>>>", e)

        try:
            self.ui_image_viewer = self.main_window.ui.taskann
            self.ui_image_viewer.setViewMode(QtWidgets.QListWidget.IconMode)
            self.ui_image_viewer.setResizeMode(QtWidgets.QListWidget.Adjust)
            self.ui_image_viewer.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.ui_image_viewer.setIconSize(QtCore.QSize(410, 400))
            self.ui_image_viewer.setMovement(QtWidgets.QListWidget.Static)
            print(self.ui_image_viewer.count())
            self.imgs = iter(os.listdir(self.ann_path))
            for img in self.imgs:
                img_path = os.path.join(self.ann_path, img)
                pixmap = QtGui.QPixmap(img_path)
                name = os.path.splitext(os.path.basename(img_path))[0]
                item = QtWidgets.QListWidgetItem(QtGui.QIcon(pixmap), name)
                item.setData(QtCore.Qt.UserRole,img_path)
                self.ui_image_viewer.addItem(item)
            # self.ui_image_viewer.doubleClicked.connect(partial(Annotations_Folder.select_item, self.ui_image_viewer.currentIndex(), self.ui_image_viewer))

        except Exception as e:
            print ("ANNOTATIONs EXE::", e)
            pass

    def addFeedback_Annotation_widget(self):
        self.ann_path = os.path.join(self.base_Path,self.shot_details['task_type'].lower(),'feedback')
        try:
            self.ui_feedback_viewer = self.main_window.ui.feedbackann
            self.ui_feedback_viewer.setViewMode(QtWidgets.QListView.IconMode)
            self.ui_feedback_viewer.setResizeMode(QtWidgets.QListView.Adjust)
            self.ui_feedback_viewer.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.ui_feedback_viewer.setIconSize(QtCore.QSize(400, 400))
            self.ui_feedback_viewer.setMovement(QtWidgets.QListView.Static)
            self.ui_feedback_viewer.setModel(QtGui.QStandardItemModel())
            self.imgs = iter(os.listdir(self.ann_path))
            timer = QtCore.QTimer(self)
            timer.timeout.connect(lambda : Annotations_Folder.load(self,self.ui_feedback_viewer))
            timer.start(100)
            # self.ui_feedback_viewer.doubleClicked.connect(lambda : Annotations_Folder.select_item(self, self.ui_feedback_viewer.currentIndex(), self.ui_feedback_viewer))

        except Exception as e:
            print ("ANNOTATION EXE::", e)
            pass

    def load(self, obj):

        for img in self.imgs:
            img_path = os.path.join(self.ann_path, img)
            pixmap = QtGui.QPixmap(img_path)
            name = os.path.splitext(os.path.basename(img_path))[0]
            item = QtGui.QStandardItem(QtGui.QIcon(pixmap),name)
            item.setData(img_path)
            obj.model().appendRow(item)


    def select_item(self, index, obj):
        try:
            os.startfile(obj.model().itemData(index)[257])

        except Exception as e:
            print (e)
            print ('unable to load the file')
