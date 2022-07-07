#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 by SRE

import os
import shutil
import sys

from PySide6 import QtCore as Core
from PySide6.QtCore import QUrl
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QShortcut, QKeySequence, QDesktopServices
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QFileDialog

from auslesen import readFromFile
from chart import Chart, SplineSeries, ScatterSeries
from diagram import calculate
from windows import Settings, showInprint

UIFilename = "form.ui"
ProjectDir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(ProjectDir, UIFilename))


def visibility(vis: bool, *widgets: QWidget):
    for w in widgets:
        w.setVisible(vis)


class MainWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.distance: float = 0.2
        self.settings = Settings(self.setDistance)
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.openFile)  # option file open
        self.openSC = QShortcut(QKeySequence("Ctrl+o"), self)  # shortcut for fileopen
        self.openSC.activated.connect(self.openFile)
        self.actionSettings.triggered.connect(self.settings.show)
        self.actionDocu.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://bszet-ig21.github.io")))
        self.actionProjekt.triggered.connect(lambda: showInprint(self))
        # connect Visible of diagrams to the checkboxes
        self.checkBox_1.stateChanged\
            .connect(lambda: visibility(self.checkBox_1.isChecked(), self.diagramm1, self.lbl_1))
        self.checkBox_2.stateChanged\
            .connect(lambda: visibility(self.checkBox_2.isChecked(), self.diagramm2, self.lbl_2))
        self.checkBox_3.stateChanged\
            .connect(lambda: visibility(self.checkBox_3.isChecked(), self.diagramm3, self.lbl_3))
        self.checkbox_grid.stateChanged.connect(lambda: self.setGirdVis(self.checkbox_grid.isChecked()))
        self.checkBox_formeln.stateChanged.connect(lambda: self.setSerVis(self.checkBox_formeln.isChecked()))
        self.times = []

    def setDistance(self, distance: int):
        self.distance = distance
        self.setDiagrams()

    def setSerVis(self, vis: bool):
        self.diagramm1.chart().setSeriesVis(1, vis)
        self.diagramm2.chart().setSeriesVis(1, vis)
        self.diagramm3.chart().setSeriesVis(1, vis)

    def setGirdVis(self, vis: bool):
        self.diagramm1.chart().setGridVis(vis)
        self.diagramm2.chart().setGridVis(vis)
        self.diagramm3.chart().setGridVis(vis)

    def setDiagrams(self):
        calculation = calculate(self.distance, self.times)
        if calculation is not None:
            t, s, v, a, ps, pv, aa, paras_s, paras_v, paras_a = calculation
            self.lbl_1.setText(f"y = {paras_s[0]}x² + {paras_s[1]}x + {paras_s[2]}\na={paras_s[0]*2}")
            self.diagramm1.setRenderHint(QPainter.Antialiasing)
            self.diagramm1.setChart(
                Chart(
                    [
                        ScatterSeries("s-t", zip(t, s)),
                        SplineSeries("fit", zip(t, ps))
                    ],
                    "s-t", "t in s", "s in m"
                )
            )
            self.lbl_2.setText(f"y = {paras_v[0]}x + {paras_v[1]}\na={paras_v[0]}")
            self.diagramm2.setRenderHint(QPainter.Antialiasing)
            self.diagramm2.setChart(
                Chart(
                    [
                        ScatterSeries("v-t", zip(t, v)),
                        SplineSeries("fit", zip(t, pv))
                    ],
                    "v-t", "t in s", "v in m/s"
                )
            )
            self.lbl_3.setText(f"y = {paras_a[0]}\na={paras_a[0]}")
            self.diagramm3.setRenderHint(QPainter.Antialiasing)
            self.diagramm3.setChart(
                Chart(
                    [
                        ScatterSeries("a-t", zip(t, a)),
                        SplineSeries(f"average acceleration", zip(t, aa))
                    ],
                    "a-t", "t in s", 'a in m/s²'
                )
            )
        else:
            print("err: No times")

    def openFile(self):
        path = QFileDialog. \
            getOpenFileName(self, "Open Data File exel/csv",
                            filter="Standard(*.xlsx *.csv *.txt);; Tabel Files (*.xlsx *.csv);; All Files (*.*)")[0]
        try:
            self.times = readFromFile(path)
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
