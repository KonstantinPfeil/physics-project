from PySide6.QtCharts import QChart, QScatterSeries, QSplineSeries, QXYSeries, QValueAxis
from PySide6.QtCore import QPointF, Qt


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
