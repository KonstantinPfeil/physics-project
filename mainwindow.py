#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 by SRE

import os
import sys

from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as Core
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtCharts import QChartView, QChart, QSplineSeries
from PySide6.QtGui import QPainter
from PySide6.QtCore import QPointF

from diagram import calculate
from auslesen import readFromFile

UIFilename = "form.ui"
ProjectDir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(ProjectDir, UIFilename))


class MainWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        calculation = calculate()
        if calculation is not None:
            t, s, v, a = calculation
            ta = [(t, a) for t, a in zip(t, a) if a is not None]
            self.c = Chart([zip(t, s), zip(t, v), ta], self)
            self.c.show()


def setData(chart, data: []):
    series = QSplineSeries(chart)
    for x, y in data:
        series << QPointF(x, y)
    chart.addSeries(series)


class Chart(QChartView):
    def __init__(self, datas: [list], parent=None):
        super(Chart, self).__init__(parent)

        self.resize(400, 300)
        self.setRenderHint(QPainter.Antialiasing)

        chart = QChart()
        self.setChart(chart)
        chart.setTitle('Simple splinechart example')
        for data in datas:
            setData(chart, data)
        chart.createDefaultAxes()
        chart.legend().setVisible(False)


if __name__ == "__main__":
    Core.QCoreApplication.setAttribute(Core.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
