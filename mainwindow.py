#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 by SRE

import os
import sys

from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as Core
from PySide6 import QtWidgets
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
            # ta = [(t, a) for t, a in zip(t, a) if a is not None]
            self.c = QChartView(self)   # todo in QTEditor QChartView statt den blauen Boxen
            self.c.resize(400, 300)
            self.c.setRenderHint(QPainter.Antialiasing)
            self.c.setChart(Chart(
                [("t-s", zip(t, s)), ("t-v", zip(t, v)), ("t-a", zip(t, a))],
                "Test"
            ))
            self.c.show()


class Chart(QChart):
    def __init__(self, datas, title: str):
        super(Chart, self).__init__()
        self.setTitle(title)
        for data in datas:
            self.set(data)
        self.createDefaultAxes()
        self.legend().setVisible(True)

    def set(self, data: []):
        series = QSplineSeries(self)
        name, data = data
        for x, y in data:
            series << QPointF(x, y)
        series.setName(name)
        self.addSeries(series)


if __name__ == "__main__":
    Core.QCoreApplication.setAttribute(Core.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
