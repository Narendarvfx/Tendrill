import os
import shutil
import time

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QApplication, QDialog, QGraphicsDropShadowEffect

from py.copy_window import Ui_Copy_Dialog


class FileCopyProgress(QDialog):

    def __init__(self, parent=None, src=None, dest=None, shot_Name=None):
        super(FileCopyProgress, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setModal(False)
        self.ui = Ui_Copy_Dialog()
        self.ui.setupUi(self)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(252, 165, 3, 50))
        self.ui.frame.setGraphicsEffect(self.shadow)
        self.src = src
        self.dest = dest
        self.rate = "0"
        self.total_time = "0 s"
        self.time_elapsed = "0 s"
        self.time_remaining = "0 s"
        self.build_ui()
        self.ui.shot_lbl.setText(shot_Name)
        self.ui.copy_abort_btn.clicked.connect(lambda: self.abort_btn())
        self.stopp = 0

    def build_ui(self):
        self.ui.lbl_src.setText('Source: '+ self.src)
        self.ui.lbl_dest.setText('Destination: ' + self.dest)

        self.auto_start_timer = QTimer()
        self.auto_start_timer.singleShot(100, lambda: self.copy_files_with_progress(self.src, self.dest, self.progress, self.copy_done))

        self.copy_timer = QTimer()
        self.copy_timer.timeout.connect(lambda: self.process_informations())
        self.copy_timer.start(1000)
        self.show()

    def abort_btn(self):
        self.copy_timer.stop()
        self.stopp = 1

    def process_informations(self):

        time_elapsed_raw = time.clock() - self.start_time
        self.time_elapsed = '{:.2f} s'.format(time_elapsed_raw)
        self.ui.lbl_time_elapsed.setText('Time Elapsed: ' + self.time_elapsed)

        # example - Total: 100 Bytes, bisher kopiert 12 Bytes/s
        time_remaining_raw = self._totalSize/self._copied
        self.time_remaining = '{:.2f} s'.format(time_remaining_raw) if time_remaining_raw < 60. else '{:.2f} min'.format(time_remaining_raw)
        self.ui.lbl_time_remaining.setText('Time Remaining: ' + self.time_remaining)

        rate_raw = (self._copied - self._copied_tmp)/1024/1024
        self.rate = '{:.2f} MB/s'.format(rate_raw)
        self.ui.lbl_rate.setText('Transfer rate: ' + self.rate)

        self._copied_tmp = self._copied

    def progress(self):
        self._progress = (self._copied/self._totalSize)*100

        try:
            self.ui.pb.setValue(self._progress)
        except:
            pass

        QApplication.processEvents()

    def get_total_size(self, src):
        return sum( os.path.getsize(os.path.join(dirpath,filename)) for dirpath, dirnames, filenames in os.walk(src) for filename in filenames ) # total size of files in bytes

    def copy_done(self):
        self.ui.pb.setValue(100)
        self.close()

    def make_dirs(self, dest):
        if not os.path.exists(dest):
            os.makedirs(dest)

    def copy_files_with_progress(self, src, dst, callback_progress, callback_copydone, length=16*1024*1024):
        self._copied = 0
        self._copied_tmp = 0
        self._totalSize = self.get_total_size(src)
        self.make_dirs(dst)
        self.start_time = time.clock()
        for path, dirs, filenames in os.walk(src):
            if dirs != []:
                for directories in dirs:
                    destDir = path.replace(src, dst)
                    # print(destDir)
                    self.make_dirs(os.path.join(destDir, directories))
                    for pat, di, filenam in os.walk(os.path.join(src, directories)):
                        shutil.copy(os.path.join(pat,filenam), destDir)
                        print(pat,filenam)
            for sfile in filenames:
                if self.stopp == 0:
                    srcFile = os.path.join(path, sfile)
                    destFile = os.path.join(dst, sfile)

                    with open(srcFile, 'rb') as fsrc:
                        with open(destFile, 'wb') as fdst:
                            _path, _file = os.path.split(destFile)
                            self.ui.shot_details_textEdit.append(_file)
                            while 1:
                                buf = fsrc.read(length)
                                if not buf:
                                    break
                                fdst.write(buf)
                                self._copied += len(buf)
                                callback_progress()
        try:
            self.copy_timer.stop()
        except:
            print('Error: could not stop QTimer')

        callback_copydone()