import sys
# from pimsviewer import GUI
# from PySide2.QtWidgets import QApplication
# from pimsviewer.example_plugins import AnnotatePlugin
#
# filepath = 'D:/2dview/showoverview.png'
#
# # Class names of extra plugins to add
# plugins = [AnnotatePlugin]
#
# app = QApplication(sys.argv)
# gui = GUI(extra_plugins=plugins)
# gui.open(fileName=filepath)
# gui.show()
#
# sys.exit(app.exec_())

from pimsviewer import run
from pimsviewer.example_plugins import AnnotatePlugin

run('D:/2dview/showoverview.png', [AnnotatePlugin])