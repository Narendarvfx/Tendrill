import glob
import os
from subprocess import call

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QPoint, QThreadPool
from PySide2.QtWidgets import QWidget, QDialog, QWidgetItem, QListWidgetItem

import api
from uipy.downloads_modal import Ui_Downloads_Dialog
from src.Shots.Worker_Class import Worker


class DownloadModal(QDialog):
    def __init__(self, instance, *args, **kwargs):
        super(DownloadModal, self).__init__()
        self.ui = Ui_Downloads_Dialog()
        self.ui.setupUi(self)
        try:
            self.ui.start_btn.clicked.disconnect()
            self.ui.cancel_btn.clicked.disconnect()
            self.ui.sel_path_btn.clicked.disconnect()
        except:
            pass
        self.config = api.config
        self.selected_shots = instance.selected_shots
        self.main_window = instance.main_window
        self.ui.sel_path_btn.clicked.connect(lambda: self.select_path())
        self.path = ""
        self.ui.start_btn.clicked.connect(lambda: self.startKaro())
        self.ui.cancel_btn.clicked.connect(lambda: self.close_dialog())
        self.threadpool = QThreadPool()
        self.ui.start_btn.setEnabled(False)
        self.ui.sel_path_btn.setEnabled(False)
        if len(self.selected_shots)>0:
            self.ui.sel_path_btn.setEnabled(True)

    def select_path(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.sel_path_text_label.setText(str(self.path))
        if os.path.isdir(self.path):
            self.ui.start_btn.setEnabled(True)

    def startKaro(self):
        self.shot_final_dir = ""
        for shots in self.selected_shots:
            task_type = '_'+shots['task_type']
            item = QListWidgetItem()
            item.setText(str(shots['name']))
            self.shot_base_dir = os.path.join(self.config['STORAGE']['storage_url'],
                                                     self.config['STORAGE']['parent_directory'],
                                                     shots['sequence']['project']['client'],
                                                     shots['sequence']['project']['name'],
                                                     shots['sequence']['name'],
                                                     shots['name'],'_forsubmission',task_type)
            if os.path.isdir(self.shot_base_dir):
                try:
                    self.shot_final_dir = max(glob.glob(os.path.join(self.shot_base_dir, '*/')),
                                              key=os.path.getmtime)
                    self.ui.shots_list_widget.addItem(item)
                    if shots['status']['code'] == "IAP":
                        worker = Worker(self.download_final_shots)  # Any other args, kwargs are passed to the run function
                        self.threadpool.start(worker)
                except Exception as e:
                    pass
                    print(e)
    def download_final_shots(self):
        call(["robocopy",self.shot_final_dir, self.path, "/S"])

    def close_dialog(self):
        self.close()
