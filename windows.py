import os
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import QRect


class Settings(QWidget):
    def __init__(self, returnFunc):
        super(Settings, self).__init__()
        self.returnFunc = returnFunc
        self.setFixedSize(200, 175)
        self.setWindowTitle("Settings")

        self.distanceTextEdit = QLineEdit(self)
        self.distanceTextEdit.setPlaceholderText("Distance between the magnets in m")
        self.distanceTextEdit.setGeometry(QRect(5, 25, 190, 30))
        self.distanceTextEdit.textEdited.connect(self.changeInDistanceSetting)
        self.distanceTextEdit.show()

        self.saveBtn = QPushButton(self, text="save distance")
        self.saveBtn.setGeometry(QRect(5, 125, 190, 40))
        self.saveBtn.clicked.connect(self.sendReturn)
        self.saveBtn.show()

    def changeInDistanceSetting(self, text: str):
        try:
            float(text)
            self.distanceTextEdit.setStyleSheet("")
        except ValueError:
            self.distanceTextEdit.setStyleSheet("color: red;")

    def sendReturn(self):
        try:
            self.returnFunc(float(self.distanceTextEdit.text()))
            self.close()
            self.distanceTextEdit.setText("")
        except ValueError:
            pass


content = r"""//==================================\\
||           ||   ||\\ //||    ||..\\    ||..\\     ||    ||\\ ||    NNN           ||
||           ||   ||  \/  ||    ||        || \\      ||    || \\||       ||              ||
\\==================================//

  BSZ-ET Dresden
  Strehlener Platz 2, 01219 Dresden Germany 
  E-Mail:      bgy@bszet.de
  Phone:      0351-4735-201
  Principal:  Herr Bernd Petschke

  Class: IG21 
  Team members:
      - Christoph Trischler 
          E-Mail:  t21trischlerch@bszetdd.lernsax.de
      - Konstantin Pfeil
          E-Mail:  t21pfeilko@bszetdd.lernsax.de
      - Karl Felix Wendt
          E-Mail:  t21wendtka@bszetdd.lernsax.de
      - Juius Weissleder
          E-Mail:  t21weisslederju@bszetdd.lernsax.de
  working period:
      June 28, 2022 - July 15, 2022
  school subjects:
      - IT systems 
      - physics """


def showInprint(parent):
    window = QWidget()
    parent.inprint = window
    window.setFixedSize(300, 435)
    window.setWindowTitle("Impressum")
    window.content = QLabel(window)
    window.content.resize(300, 435)
    window.content.setText(content)
    window.content.show()
    window.show()
