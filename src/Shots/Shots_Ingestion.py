import csv
import os
import time
from datetime import datetime
from subprocess import call

import progressbar
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import Signal, QTimer, QRunnable, QObject, Slot, QThreadPool
from PySide2.QtWidgets import QFileDialog, QTableWidgetItem, QApplication, QMessageBox

import api
import win32security
import ntsecuritycon as con

from src.Shots.Worker_Class import Worker
from uipy.shots_ingest_modal import Ui_ShotsIngestProgressDialog


class ProgressThread(QtCore.QThread):
    updateProgressBar = Signal(float)

    def __init__(self, src_dir, dest_dir, val, parent=None):
        super(ProgressThread, self).__init__(parent)
        self.val = val
        self.src_dir = src_dir
        self.dest_dir = dest_dir

    def run(self):
        while True:
            self.updateProgressBar.emit(self.val)
            call(["robocopy", self.src_dir,
                  self.dest_dir, "/S"])
            # shutil.copytree(src_dir, dest_dir)
            QApplication.processEvents()
            self.exec_()

class Shots_Ingestion(object):
    def __init__(self, obj):
        super(Shots_Ingestion, self).__init__()
        self.main_window = obj
        self.main_window.ui.shot_import_table.setRowCount(0)
        # self.main_window.ui.sh_import_btn.setEnabled(False)
        self.main_window.ui.sh_selected_file_name.setText("")
        try:
            self.main_window.ui.sh_file_btn.clicked.disconnect()
            self.main_window.ui.sel_all_shots_chkBox.toggled.disconnect()
            self.main_window.ui.sh_upload_btn.clicked.disconnect()
            self.main_window.ui.sh_up_Client.activated.disconnect()
            self.main_window.ui.sh_up_Project.activated.disconnect()
            if self.file:
                del self.file
        except:
            pass
        self.main_window.ui.sh_file_btn.clicked.connect(lambda: self.select_file())
        self.main_window.ui.sel_all_shots_chkBox.toggled.connect(lambda: self.select_all_shots())
        self.main_window.ui.sh_upload_btn.clicked.connect(lambda: self.upload_shots())
        header = self.main_window.ui.shot_import_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.main_window.ui.sh_import_progressBar.hide()
        # self.clients_data = api.get_all_clients()
        # self.main_window.ui.sh_up_Client.clear()
        # self.main_window.ui.sh_up_Client.addItem("", None)
        # self.main_window.ui.sh_up_Client.setItemText(0,
        #                                              QtWidgets.QApplication.translate("MainWindow", "Select Client",
        #                                                                               None, -1))
        # for c, clients in enumerate(self.clients_data):
        #     self.main_window.ui.sh_up_Client.addItem("", clients['id'])
        #     self.main_window.ui.sh_up_Client.setItemText(c + 1,
        #                                                  QtWidgets.QApplication.translate("MainWindow", clients['name'],
        #                                                                                   None, -1))
        self.main_window.ui.sh_up_Project.clear()
        self.main_window.ui.sh_up_Project.addItem("", None)
        self.main_window.ui.sh_up_Project.setItemText(0,
                                                     QtWidgets.QApplication.translate("MainWindow", "Select Project",
                                                                                      None, -1))
        self.getProject()
        self.config = api.config

    def getProject(self):
        try:
            self.main_window.ui.sh_up_Project.activated.disconnect()
        except:
            pass

        self.main_window.ui.sh_up_Project.clear()
        self.main_window.ui.sh_up_Project.addItem("", None)
        self.main_window.ui.sh_up_Project.setItemText(0,
                                                      QtWidgets.QApplication.translate("MainWindow", "Select Project",
                                                                                       None, -1))
        self.main_window.ui.sh_file_btn.setEnabled(False)

        self.projects_data = api.get_client_projects()
        for p, projects in enumerate(self.projects_data):
            self.main_window.ui.sh_up_Project.addItem("", projects['id'])
            self.main_window.ui.sh_up_Project.setItemText(p + 1,
                                                          QtWidgets.QApplication.translate("MainWindow",
                                                                                           projects['name'],
                                                                                           None, -1))
        self.main_window.ui.sh_up_Project.activated.connect(self.projectData)

    def projectData(self, index):
        self.sel_project_id = self.main_window.ui.sh_up_Project.itemData(index)
        if self.sel_project_id is not None:
            self.main_window.ui.sh_file_btn.setEnabled(True)
        else:
            self.main_window.ui.sh_file_btn.setEnabled(False)

    def select_file(self):
        self.dlg = QFileDialog().getOpenFileName(None, 'Open File', '', 'Csv files(*.csv)')
        ## To get total count of rows for avg
        self.file = open(self.dlg[0])
        self.file_name = os.path.basename(self.dlg[0])
        self.main_window.ui.sh_selected_file_name.setText(self.file_name)
        if self.file:
        #     # self.numline = len(self.file.readlines())
        #     self.main_window.ui.sh_import_btn.setEnabled(True)
        # del self.file
        # try:
        #     self.main_window.ui.sh_import_btn.clicked.disconnect()
        # except:
        #     pass
        # self.main_window.ui.sh_import_btn.clicked.connect(lambda: self.import_csv_file())
            self.import_csv_file()

    def import_csv_file(self):
        self.seq_name = []
        self.get_seq_data = api.get_seq_projects(self.sel_project_id)
        if self.get_seq_data:
            for d in self.get_seq_data:
                self.seq_name.append(d['name'])
        try:
            with open(self.dlg[0],'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                print(reader)
                for i, row in enumerate(reader):
                    QApplication.processEvents()
                    if not row['Sequence'] in self.seq_name:
                        data = {
                            'name': row['Sequence'],
                            'project': self.sel_project_id,
                        }
                        api.create_seq(data)
                        self.seq_name.append(row['Sequence'])
                    self.main_window.ui.shot_import_table.insertRow(i)
                    checkbox = QtWidgets.QCheckBox()
                    self.main_window.ui.shot_import_table.setCellWidget(i, 0, checkbox)
                    row_Item = QTableWidgetItem()
                    row_Item.setData(1, row)
                    row_Item.setText(row['Sequence'])
                    self.main_window.ui.shot_import_table.setItem(i, 1, row_Item)
                    self.main_window.ui.shot_import_table.setItem(i, 2, QTableWidgetItem(row['Shot Name']))
                    self.main_window.ui.shot_import_table.setItem(i, 3, QTableWidgetItem(row['Type']))
                    self.main_window.ui.shot_import_table.setItem(i, 4, QTableWidgetItem(str(row['Frame IN'])))
                    self.main_window.ui.shot_import_table.setItem(i, 5, QTableWidgetItem(str(row['Frame OUT'])))
                    self.main_window.ui.shot_import_table.setItem(i, 6, QTableWidgetItem(str(int(row['Frame OUT'])-int(row['Frame IN'])+1)))
                    self.main_window.ui.shot_import_table.setItem(i, 7, QTableWidgetItem(str(row['ETA'])))
                    self.main_window.ui.shot_import_table.setItem(i, 8, QTableWidgetItem(str(row['Bid Days'])))
                    self.main_window.ui.shot_import_table.setItem(i, 9, QTableWidgetItem(str(row['Package ID'])))
                    self.main_window.ui.shot_import_table.setItem(i, 10, QTableWidgetItem(str(row['Estimate ID'])))
                    self.main_window.ui.shot_import_table.setItem(i, 11, QTableWidgetItem(str(row['Estimate Date'])))
                    self.main_window.ui.shot_import_table.setItem(i, 12, QTableWidgetItem("Ok"))
        except Exception as w:
            print(w)

    def on_finished(self):
        print("Finished")

    def updateProgressBar(self, val):
        print("Update Val", val)
        self.main_window.ui.sh_import_progressBar.setValue(val)

    def get_zize(self, path):
        return os.path.getsize(path)

    def select_all_shots(self):
        if self.main_window.ui.sel_all_shots_chkBox.isChecked():
            for i in range(self.main_window.ui.shot_import_table.rowCount()):
                self.main_window.ui.shot_import_table.cellWidget(i, 0).setChecked(True)
        else:
            for i in range(self.main_window.ui.shot_import_table.rowCount()):
                self.main_window.ui.shot_import_table.cellWidget(i, 0).setChecked(False)

    def upload_shots(self):
        self.seq_id = ''
        self.get_seqe_data = api.get_seq_projects(self.sel_project_id)
        total_count = self.main_window.ui.shot_import_table.rowCount()
        c = 0
        bar = progressbar.ProgressBar(maxval=total_count, \
                                      widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        for i in range(total_count):
            if self.main_window.ui.shot_import_table.cellWidget(i, 0).isChecked():
                row_data = self.main_window.ui.shot_import_table.item(i, 1).data(1)
                for d in self.get_seqe_data:
                    if row_data['Sequence'] == d['name']:
                        self.current_seq_name = d['name']
                        self.pro_name = d['project']['name']
                        self.cli_name = d['project']['client']
                        self.seq_id = d['id']
                eta_date = datetime.strptime(row_data['ETA'], '%d-%m-%Y')
                estimate_date = ""
                try:
                    estimate_date = datetime.strptime(row_data['Estimate Date'], '%d-%m-%Y')
                except Exception as e:
                    pass
                shot_data = {
                    'name': row_data['Shot Name'],
                    'sequence': self.seq_id,
                    'bid_days': row_data['Bid Days'],
                    'task_type': row_data['Type'],
                    'eta': eta_date.strftime('%Y-%m-%d'),
                    'actual_start_frame': row_data['Frame IN'],
                    'actual_end_frame': row_data['Frame OUT'],
                    'package_id': row_data['Package ID'],
                    'estimate_id': row_data['Estimate ID'],
                    'estimate_date': estimate_date,
                    'input_path': row_data['Input Path'],
                    'comments': row_data['Comments'],
                    'status': "YTA"
                }
                try:
                    response = api.create_shots(shot_data)
                    print(response.json())
                    shot_res_data = response.json()
                    if response.status_code == 201:
                        api.createShot_group({'name': shot_res_data['name'] + '_' + str(shot_res_data['id'])})
                        self.create_directories(cli_name=self.cli_name, pro_name=self.pro_name,
                                            current_seq_name=self.current_seq_name, shotName=row_data['Shot Name'],row_data = row_data)
                except Exception as e:
                    print(e)
            bar.update(i+1)
            time.sleep(0.1)

        bar.finish()
        msg = QMessageBox()
        msg.setText("Selected Data Ingested sucessfully")
        msg.setWindowTitle("Error")

        msg.setIcon(QMessageBox.Information)
        # msg.setStyleSheet("background-color: rgb(202,0,3);color:'white'")
        msg.exec_()
        # self.main_window.ui.shot_import_table.()

    def create_directories(self, cli_name=None, pro_name=None, current_seq_name=None, shotName=None, row_data=None):
        print ("HELLO")
        self.base_dir = ""
        self.row_data = ""
        self.base_dir = os.path.join(self.config['STORAGE']['storage_url'], pro_name, current_seq_name, shotName)
        self.row_data = row_data
        print (self.base_dir)
        os.makedirs(self.base_dir, exist_ok=True)
        default_folder_structure = r'P:\Tendrill\folder_structure'
        cmd = f'Xcopy {default_folder_structure} {self.base_dir} /E /I'
        try:
            os.system(cmd)
            print ("Folder structure Created")
        except:
            print("Failed to create folder structure")
        # job_folders = [ 'comp', 'mm', 'paint', 'roto','scans']
        # for jb_folder in job_folders:
        #     os.makedirs(os.path.join(self.base_dir,jb_folder), exist_ok=True)
        # scan_folders = ['elements', 'mov', 'plates', 'proxy']
        # for scn_folder in scan_folders:
        #     os.makedirs(os.path.join(self.base_dir, '_scans',scn_folder), exist_ok=True)
        # general_folders = ['cp', 'internal_denoise', 'mattes', 'output', 'pre_renders', 'qc', 'qt', 'scripts', 'sv',
        #                    'qc\\internal_retake']
        # for gnrl_folder in general_folders:
        #     os.makedirs(os.path.join(self.base_dir, '_comp', gnrl_folder), exist_ok=True)
        #     os.makedirs(os.path.join(self.base_dir, '_paint', gnrl_folder), exist_ok=True)
        #     os.makedirs(os.path.join(self.base_dir, '_roto', gnrl_folder), exist_ok=True)
        #     os.makedirs(os.path.join(self.base_dir, '_mm', gnrl_folder), exist_ok=True)
        #
        # scripts_folders = ['3de', 'maya', 'mocha', 'nk', 'psd', 'rv', 'sfx']
        # for scrpt_folder in scripts_folders:
        #     os.makedirs(os.path.join(self.base_dir,'_comp', 'scripts', scrpt_folder), exist_ok=True)
        #     os.makedirs(os.path.join(self.base_dir, '_paint', 'scripts', scrpt_folder), exist_ok=True)
        #     os.makedirs(os.path.join(self.base_dir, '_roto', 'scripts', scrpt_folder), exist_ok=True)
        #     os.makedirs(os.path.join(self.base_dir, '_mm', 'scripts', scrpt_folder), exist_ok=True)
        #
        # dep_folders = ['_paint', '_roto', '_comp', '_mm']
        # for dep_folder in dep_folders:
        #     os.makedirs(os.path.join(self.base_dir, '_feedback', dep_folder), exist_ok=True)
        #     os.makedirs(os.path.join(self.base_dir, '_forsubmission', dep_folder), exist_ok=True)

        # try:
        #     worker = Worker(self.create_permission_groups)  # Any other args, kwargs are passed to the run function
        #     self.threadpool.start(worker)
        # except Exception as e:
        #     pass
        # try:
        #     worker = Worker(self.copy_plates)  # Any other args, kwargs are passed to the run function
        #     self.threadpool.start(worker)
        # except Exception as e:
        #     pass
        try:
            call(['robocopy', row_data['Input Path'], os.path.join(self.base_dir, 'scans', 'plates'), "/S", "/MIR"])
        except Exception as e:
            print (e)
            pass
        # try:
        #     call(['robocopy', row_data['Elements Path'], os.path.join(self.base_dir, '_scans', 'elements'), "/S", "/MIR"])
        # except Exception as e:
        #     pass

    def copy_plates(self):
        log_date = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
        log_dir = os.path.join(self.config['STORAGE']['storage_url'], self.config['STORAGE']['ingestion_logs'])
        log_file = log_dir+log_date+'.log'
        call(["robocopy", os.path.join(self.row_data['Input Path'], self.row_data['Shot Name']),
              os.path.join(self.base_dir, '_scans', 'plates'), "/S", "/MIR", "/LOG+:"+log_file])

    def create_permission_groups(self):
        permitted_users = api.get_permission_groups()
        for permitted_user in permitted_users:
            perm_dir = ""
            user = ""
            folder = ""
            if permitted_user['department'] == "PRODUCTION":
                user = permitted_user['permitted_users']
                perm_dir = self.base_dir
                if not os.path.exists(perm_dir):
                    os.makedirs(perm_dir)
                try:
                    FILENAME = perm_dir

                    artist, domain, type = win32security.LookupAccountName("", str(user))

                    sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

                    dacl = sd.GetSecurityDescriptorDacl()

                    dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                               win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT, con.GENERIC_ALL,
                                               artist)

                    sd.SetSecurityDescriptorDacl(1, dacl, 0)
                    win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
                except Exception as e:
                    print(perm_dir, e)
                    pass

            elif permitted_user['department'] == self.row_data['Type']:
                user = permitted_user['permitted_users']
                folder = '_' + permitted_user['department'].lower()
                perm_dir = os.path.join(self.base_dir, folder)
                if not os.path.exists(perm_dir):
                    os.makedirs(perm_dir)
                dep_dir = '_'+self.row_data['Type'].lower()
                submission_folder = os.path.join('_forsubmission',dep_dir)
                for_sub_perm = os.path.join(self.base_dir,submission_folder)
                try:
                    FILENAME = perm_dir

                    artist, domain, type = win32security.LookupAccountName("", str(user))

                    sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

                    dacl = sd.GetSecurityDescriptorDacl()

                    dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                               win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT, con.GENERIC_ALL,
                                               artist)

                    sd.SetSecurityDescriptorDacl(1, dacl, 0)
                    win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
                except Exception as e:
                    print(perm_dir, e)
                    pass

                if not os.path.exists(for_sub_perm):
                    os.makedirs(for_sub_perm)
                try:
                    FILENAME = for_sub_perm

                    artist, domain, type = win32security.LookupAccountName("", str(user))

                    sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

                    dacl = sd.GetSecurityDescriptorDacl()

                    dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                               win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT, con.GENERIC_ALL,
                                               artist)

                    sd.SetSecurityDescriptorDacl(1, dacl, 0)
                    win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
                except Exception as e:
                    print(for_sub_perm, e)
                    pass


