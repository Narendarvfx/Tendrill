from PySide2 import QtCore
from PySide2.QtCore import QEasingCurve, QPoint, QAbstractAnimation, QCoreApplication, QUrl, QThreadPool, QTimer

from PySide2.QtWidgets import QDialog

from uipy.projects.output_path_modal import Ui_Output_Path_Dialog


class OutputPathModal(QDialog):
    def __init__(self, instance, *args, **kwargs):
        super(OutputPathModal, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Output_Path_Dialog()
        self.ui.setupUi(self)
        self.main_window = instance.main_window
        host = self.main_window.geometry()
        point = host.center() - self.rect().center()
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animMove = QtCore.QPropertyAnimation(self, b"pos");
        self.animMove.setDuration(250);
        self.animMove.setStartValue(point - QPoint(0, 30));
        self.animMove.setEndValue(point);
        self.animMove.setEasingCurve(QEasingCurve.OutQuad);
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)
        self.animMove.start(QAbstractAnimation.DeleteWhenStopped)
        self.ui.save_btn.clicked.connect(self.save_shot)

    def get_output_path(self):
        output_path = self.ui.output_path_textEdit.toPlainText()
        return output_path

    def save_shot(self):
        self.accept()
