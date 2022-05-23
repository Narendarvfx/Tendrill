from PySide2 import QtGui
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QObject
from PySide2.QtGui import QColor, QBrush, QPainter
from PySide2.QtWidgets import QMainWindow

from uipy.main_window import Ui_MainWindow

class Employee_Stats(QMainWindow):
    def __init__(self, ui_object):
        super(Employee_Stats, self).__init__(ui_object)
        self.main_window = ui_object
        self.create_piechart()
        self.slice_value = ""

    def create_piechart(self):
        self.series = QtCharts.QPieSeries()
        data = {
            "Paint": (80, QColor("#e67d75")),
            "Roto": (50, QColor("#f0945b")),
            "MM": (30, QColor("#74b6f7")),
            "Management": (10, QColor("#aeed8a"))
        }

        for name, (value, color) in data.items():
            _slice = self.series.append("<span style=\"color: white;\">{} {}</span>".format(name, value), value)
            _slice.setBrush(color)
            _slice.setLabelVisible(True)
            _slice.setLabelColor(QColor('black'))
        # self.series.append("<span style=\"color: white;\">Paint {}</span>".format(80), 80)
        # self.series.append("<span style=\"color: white;\">Roto {}</span>".format(80), 80)
        # self.series.append("<span style=\"color: white;\">MM {}</span>".format(30), 30)
        # self.series.append("<span style=\"color: white;\">Management {}</span>".format(10), 10)
        self.series.hovered.connect(self.pie_clicked)

        chart = QtCharts.QChart()
        chart.legend().hide()
        chart.setBackgroundBrush(QBrush(QColor(Qt.transparent)))
        chart.addSeries(self.series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.setTitle("<span style=\"color: white;\">Department Wise Employee Stats</span>")
        chart.setFont(QtGui.QFont("Arial", 12))

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setFont(QtGui.QFont("Arial", 10))

        chartview = QtCharts.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        # chartview.setGeometry(0, 0, 500, 380)
        chartview.setParent(self.main_window.ui.frame_18)

        # self.main_window.ui.frame_18.resize(400,280)

    def pie_clicked(self, slice):
        slice.setExploded(True)
        slice.setExplodeDistanceFactor(0.09)
        # slice.setLabelVisible(True)
        for sli in self.series.slices():
            if sli == self.slice_value:
                sli.setExploded(False)
                # sli.setLabelVisible(False)
        self.slice_value = slice