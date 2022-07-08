# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1176, 650)
        MainWindow.setMinimumSize(QSize(1176, 650))
        MainWindow.setMaximumSize(QSize(1176, 650))
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.84, y1:1, x2:1, y2:0, stop:0 rgba(38, 41, 46, 100), stop:1 rgba(86, 93, 103, 1));")
        self.actionDocu = QAction(MainWindow)
        self.actionDocu.setObjectName(u"actionDocu")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionProjektinformationen = QAction(MainWindow)
        self.actionProjektinformationen.setObjectName(u"actionProjektinformationen")
        font = QFont()
        font.setKerning(True)
        self.actionProjektinformationen.setFont(font)
        self.actionProjekt = QAction(MainWindow)
        self.actionProjekt.setObjectName(u"actionProjekt")
        self.actioninfo_Website = QAction(MainWindow)
        self.actioninfo_Website.setObjectName(u"actioninfo_Website")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.diagramm1 = QChartView(self.centralwidget)
        self.diagramm1.setObjectName(u"diagramm1")
        self.diagramm1.setGeometry(QRect(80, 180, 301, 351))
        self.diagramm1.setStyleSheet(u"background-color: rgb(38, 41, 46);\n"
"border-radius: 10px;")
        self.diagramm2 = QChartView(self.centralwidget)
        self.diagramm2.setObjectName(u"diagramm2")
        self.diagramm2.setGeometry(QRect(440, 180, 301, 351))
        self.diagramm2.setStyleSheet(u"background-color: rgb(38, 41, 46);\n"
"border-radius: 10px;")
        self.diagramm3 = QChartView(self.centralwidget)
        self.diagramm3.setObjectName(u"diagramm3")
        self.diagramm3.setGeometry(QRect(800, 180, 301, 351))
        self.diagramm3.setStyleSheet(u"background-color: rgb(38, 41, 46);\n"
"border-radius: 10px;")
        self.lbl_Title = QLabel(self.centralwidget)
        self.lbl_Title.setObjectName(u"lbl_Title")
        self.lbl_Title.setGeometry(QRect(0, -10, 1181, 101))
        font1 = QFont()
        font1.setPointSize(35)
        font1.setBold(True)
        self.lbl_Title.setFont(font1)
        self.lbl_Title.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(187, 178, 233);")
        self.lbl_Title.setAlignment(Qt.AlignCenter)
        self.checkBox_1 = QCheckBox(self.centralwidget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setGeometry(QRect(80, 150, 261, 20))
        self.checkBox_1.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.checkBox_1.setChecked(True)
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(440, 150, 291, 20))
        self.checkBox_2.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.checkBox_2.setChecked(True)
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(800, 150, 301, 20))
        self.checkBox_3.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.checkBox_3.setChecked(True)
        self.checkbox_grid = QCheckBox(self.centralwidget)
        self.checkbox_grid.setObjectName(u"checkbox_grid")
        self.checkbox_grid.setGeometry(QRect(80, 90, 85, 20))
        self.checkbox_grid.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.checkbox_grid.setChecked(True)
        self.checkBox_formeln = QCheckBox(self.centralwidget)
        self.checkBox_formeln.setObjectName(u"checkBox_formeln")
        self.checkBox_formeln.setGeometry(QRect(80, 120, 131, 20))
        self.checkBox_formeln.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.checkBox_formeln.setChecked(True)
        self.lbl_1 = QLabel(self.centralwidget)
        self.lbl_1.setObjectName(u"lbl_1")
        self.lbl_1.setGeometry(QRect(90, 540, 281, 40))
        self.lbl_1.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.lbl_1.setAlignment(Qt.AlignCenter)
        self.lbl_2 = QLabel(self.centralwidget)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setGeometry(QRect(440, 540, 301, 40))
        self.lbl_2.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.lbl_2.setAlignment(Qt.AlignCenter)
        self.lbl_3 = QLabel(self.centralwidget)
        self.lbl_3.setObjectName(u"lbl_3")
        self.lbl_3.setGeometry(QRect(810, 540, 291, 40))
        self.lbl_3.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.lbl_3.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1176, 24))
        self.menubar.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.menuinfo = QMenu(self.menubar)
        self.menuinfo.setObjectName(u"menuinfo")
        self.menuinfo.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuinfo.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuinfo.addAction(self.actionProjekt)
        self.menuinfo.addAction(self.actionDocu)
        self.menuinfo.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"physics project", None))
        self.actionDocu.setText(QCoreApplication.translate("MainWindow", u"Doku", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Abstand", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionProjektinformationen.setText(QCoreApplication.translate("MainWindow", u"Projektinformationen", None))
        self.actionProjekt.setText(QCoreApplication.translate("MainWindow", u"Impressum", None))
        self.actioninfo_Website.setText(QCoreApplication.translate("MainWindow", u"info-Website", None))
        self.lbl_Title.setText(QCoreApplication.translate("MainWindow", u"Auswertung gleichf\u00f6rmige Bewegung", None))
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"Diagramm s-t", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Diagramm v-t", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Diagramm a-t", None))
        self.checkbox_grid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.checkBox_formeln.setText(QCoreApplication.translate("MainWindow", u"Fits", None))
        self.lbl_1.setText("")
        self.lbl_2.setText("")
        self.lbl_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuinfo.setTitle(QCoreApplication.translate("MainWindow", u"Projekt", None))
    # retranslateUi

