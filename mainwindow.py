#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 by SRE

import os
import sys

from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as Core
from PySide6 import QtWidgets
from PySide6.QtCharts import QChartView, QChart, QScatterSeries, QSplineSeries
from PySide6.QtGui import QPainter
from PySide6.QtCore import QPointF
from PySide6.QtWidgets import QFileDialog

from diagram import calculate
from auslesen import readFromFile

UIFilename = "form.ui"
ProjectDir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(ProjectDir, UIFilename))


def openFile():
    path, i = QFileDialog.getOpenFileName()
    try:
        readFromFile(path)
    except Exception as e:
        print(e)
        print("wrong file")


class MainWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.c = None
        self.setupUi(self)
        try:
            self.setDiagrams()
        except FileNotFoundError:
            pass
        self.actionOpen.triggered.connect(openFile)

    def setDiagrams(self):
        calculation = calculate()
        if calculation is not None:
            t, s, v, a, ma = calculation
            # ta = [(t, a) for t, a in zip(t, a) if a is not None]
            self.diagramm1.setRenderHint(QPainter.Antialiasing)
            self.diagramm1.setChart(Chart(
                [("t-s", zip(t, s), QScatterSeries)],
                "t-s"
            ))
            self.diagramm2.setRenderHint(QPainter.Antialiasing)
            self.diagramm2.setChart(Chart(
                [("t-v", zip(t, v), QScatterSeries)],
                "t-v"
            ))
            self.diagramm3.setRenderHint(QPainter.Antialiasing)
            self.diagramm3.setChart(Chart(
                [("t-a", zip(t, a), QScatterSeries), ("meanaccerlation", [(0, ma), (8.1, ma)], QSplineSeries)],
                "t-a"
            ))


class Chart(QChart):
    def __init__(self, datas, title: str):
        super(Chart, self).__init__()
        self.setTitle(title)
        for data in datas:
            self.set(data)
        self.createDefaultAxes()
        self.legend().setVisible(True)

    def set(self, data: []):
        name, data, form = data
        series = form(self)
        series.setMarkerSize(5)
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
