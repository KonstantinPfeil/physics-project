#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 by SRE

import os
import sys

from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as Core
from PySide6 import QtWidgets
from PySide6.QtCharts import QChart, QScatterSeries, QSplineSeries, QXYSeries, QValueAxis
from PySide6.QtGui import QPainter, QShortcut, QKeySequence, QBrush, QColor
from PySide6.QtCore import QPointF, Qt
from PySide6.QtWidgets import QFileDialog

from diagram import calculate
from auslesen import readFromFile

UIFilename = "form.ui"
ProjectDir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(ProjectDir, UIFilename))


class MainWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.c = None
        self.setupUi(self)
        self.setDiagrams()
        self.actionOpen.triggered.connect(self.openFile)  # option file open
        self.openSC = QShortcut(QKeySequence("Ctrl+o"), self)  # shortcut for fileopen
        self.openSC.activated.connect(self.openFile)
        # connect Visible of diagrams with the checkboxes
        self.checkBox_1.stateChanged.connect(lambda: self.diagramm1.setVisible(self.checkBox_1.isChecked()))
        self.checkBox_2.stateChanged.connect(lambda: self.diagramm2.setVisible(self.checkBox_2.isChecked()))
        self.checkBox_3.stateChanged.connect(lambda: self.diagramm3.setVisible(self.checkBox_3.isChecked()))

    def setDiagrams(self):
        calculation = calculate()
        if calculation is not None:
            t, s, v, a, ma = calculation
            # ta = [(t, a) for t, a in zip(t, a) if a is not None]
            self.diagramm1.setRenderHint(QPainter.Antialiasing)
            self.diagramm1.setChart(Chart(
                [ScatterSeries("t-s", zip(t, s))],
                "t-s"
            ))
            self.diagramm2.setRenderHint(QPainter.Antialiasing)
            self.diagramm2.setChart(
                Chart([ScatterSeries("t-v", zip(t, v))], "t-v")
            )
            self.diagramm3.setRenderHint(QPainter.Antialiasing)
            self.diagramm3.setChart(
                Chart(
                    [
                        ScatterSeries("t-a", zip(t, a)),
                        SplineSeries("mean acceleration", [(0, ma), (8.1, ma)])
                    ],
                    "t-a"
                )
            )
        else:
            print("err: No times")

    def openFile(self):
        path = QFileDialog. \
            getOpenFileName(self, "Open Data File exel/csv",
                            filter="Tabel Files (*.xlsx *.csv);; All Files (*.*)")[0]
        try:
            readFromFile(path)
        except Exception as e:
            print(e)
            print("wrong file")
            return
        self.setDiagrams()


class Chart(QChart):
    def __init__(self, series, title: str, maxX: int = 10,  maxY: int = 10):
        super(Chart, self).__init__()
        self.setTitle(title)
        for s in series:
            self.add(s)
        self.legend().setVisible(True)
        self.createDefaultAxes()
        """ax = QValueAxis(self)
        ax.setGridLineVisible(False)
        ax.setRange(0, maxX)
        self.addAxis(ax, Qt.AlignmentFlag.AlignBottom)
        ay = QValueAxis(self)
        ay.setGridLineVisible(False)
        ay.setRange(0, maxY)
        self.addAxis(ay, Qt.AlignmentFlag.AlignLeft)"""

    def add(self, s: QXYSeries):
        s.setParent(self)
        self.addSeries(s)


class SplineSeries(QSplineSeries):
    def __init__(self, name, data):
        super(SplineSeries, self).__init__()
        self.setMarkerSize(5)
        for x, y in data:
            self << QPointF(x, y)
        self.setName(name)


class ScatterSeries(QScatterSeries):
    def __init__(self, name, data):
        super(ScatterSeries, self).__init__()
        self.setMarkerSize(5)
        for x, y in data:
            self << QPointF(x, y)
        self.setName(name)


if __name__ == "__main__":
    Core.QCoreApplication.setAttribute(Core.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
