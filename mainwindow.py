#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 by SRE

import os
import sys, shutil

from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as Core
from PySide6 import QtWidgets
from PySide6.QtGui import QPainter, QShortcut, QKeySequence, QBrush, QColor
from PySide6.QtWidgets import QFileDialog

from diagram import calculate
from auslesen import readFromFile
from chart import Chart, SplineSeries, ScatterSeries

UIFilename = "form.ui"
ProjectDir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(ProjectDir, UIFilename))


class MainWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.setDiagrams()
        self.actionOpen.triggered.connect(self.openFile)  # option file open
        self.openSC = QShortcut(QKeySequence("Ctrl+o"), self)  # shortcut for fileopen
        self.openSC.activated.connect(self.openFile)
        # connect Visible of diagrams to the checkboxes
        self.checkBox_1.stateChanged.connect(lambda: self.diagramm1.setVisible(self.checkBox_1.isChecked()))
        self.checkBox_2.stateChanged.connect(lambda: self.diagramm2.setVisible(self.checkBox_2.isChecked()))
        self.checkBox_3.stateChanged.connect(lambda: self.diagramm3.setVisible(self.checkBox_3.isChecked()))
        self.checkbox_grid.stateChanged.connect(lambda: self.setGirdVis(self.checkbox_grid.isChecked()))
        self.checkBox_formeln.stateChanged.connect(lambda: self.setSerVis(self.checkBox_formeln.isChecked()))

    def setSerVis(self, vis: bool):
        self.diagramm1.chart().setSeriesVis(1, vis)
        self.diagramm2.chart().setSeriesVis(1, vis)
        self.diagramm3.chart().setSeriesVis(1, vis)

    def setGirdVis(self, vis: bool):
        self.diagramm1.chart().setGridVis(vis)
        self.diagramm2.chart().setGridVis(vis)
        self.diagramm3.chart().setGridVis(vis)

    def setDiagrams(self):
        calculation = calculate()
        if calculation is not None:
            t, s, v, a, ps, pv, aa, paras_s, paras_v, paras_a = calculation
            self.diagramm1.setRenderHint(QPainter.Antialiasing)
            self.diagramm1.setChart(
                Chart(
                    [
                        ScatterSeries("t-s", zip(t, s)),
                        SplineSeries("fit", zip(t, ps))
                    ],
                    "t-s", "t in s", "s in m"
                )
            )
            self.diagramm2.setRenderHint(QPainter.Antialiasing)
            self.diagramm2.setChart(
                Chart(
                    [
                        ScatterSeries("t-v", zip(t, v)),
                        SplineSeries("fit", zip(t, pv))
                    ],
                    "t-v", "t in s", "v in m/s"
                )
            )
            self.diagramm3.setRenderHint(QPainter.Antialiasing)
            self.diagramm3.setChart(
                Chart(
                    [
                        ScatterSeries("t-a", zip(t, a)),
                        SplineSeries(f"average acceleration", zip(t, aa))
                    ],
                    "t-a", "t in s", 'a in m/s²'
                )
            )
        else:
            print("err: No times")

    def openFile(self):
        path = QFileDialog. \
            getOpenFileName(self, "Open Data File exel/csv",
                            filter="Standard(*.xlsx *.csv *.txt);; Tabel Files (*.xlsx *.csv);; All Files (*.*)")[0]
        if path.endswith(".txt"):
            shutil.copy(path, os.path.dirname(os.path.abspath(__file__)))
            return
        try:
            readFromFile(path)
        except Exception as e:
            print(e)
            print("wrong file")
            return
        self.setDiagrams()


if __name__ == "__main__":
    Core.QCoreApplication.setAttribute(Core.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
