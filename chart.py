from PySide6.QtCharts import QChart, QScatterSeries, QSplineSeries, QXYSeries, QValueAxis
from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QBrush, QFont


class Chart(QChart):
    def __init__(self, series, title: str, xname, yname):
        super(Chart, self).__init__()
        self.setTitle(title)
        for s in series:
            self.add(s)
        self.legend().setVisible(True)
        self.createDefaultAxes()
        """xaxis, yaxis = self.axes()
        yaxis.setTitleFont(QFont("sans-serif", 9))
        xaxis.setTitleFont(QFont("sans-serif", 9))
        yaxis.setTitleText(yname)
        xaxis.setTitleText(xname)"""

    def add(self, s: QXYSeries):
        s.setParent(self)
        self.addSeries(s)

    def setSeriesVis(self, index: int, vis: bool):
        self.series()[index].setVisible(vis)

    def setGridVis(self, vis: bool):
        for a in self.axes():
            a.setGridLineVisible(vis)


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
