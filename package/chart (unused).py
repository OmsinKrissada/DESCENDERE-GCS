from PySide6.QtCharts import *
from PySide6.QtGui import QColor, QPen
import pyqtgraph
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

pyqtgraph.setConfigOption('background', 'w')
pyqtgraph.setConfigOption('foreground', 'k')


class toPlot:
    def __init__(self, color: tuple, curve=False) -> None:
        self.line = QSplineSeries() if curve else QLineSeries()
        self.point = QScatterSeries()
        self.x = []
        self.y = []
        self.color = QColor(color[0], color[1], color[2])
        self.pen = QPen(self.color)
        self.pen.setWidth(2)
        self.line.setPen(self.pen)
        self.point.setMarkerSize(8)
        self.point.setColor(self.color)

    def plot(self, x, y):
        self.line.append(x, y)
        self.point.append(x, y)
        self.x.append(x)
        self.y.append(y)

    def clear(self):
        self.point.clear()
        self.line.clear()


class GraphicGraph:
    def __init__(self, graph: QChartView, title: str, unit: str, line, theme=QChart.ChartThemeBlueIcy) -> None:
        self.Graph = graph
        self.Title = title
        self.Unit = unit
        self.Theme = theme

        self._mline = True if isinstance(line, tuple) else False

        self.lines = line
        self.X_AXIS = QValueAxis()
        self.Y_AXIS = QValueAxis()
        self._chart = QChart()

        self._chart.legend().hide()
        self._chart.setDropShadowEnabled(True)
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self._chart.setTheme(self.Theme)
        self._chart.setMargins(QMargins(10, 10, 10, 0))

        self.X_AXIS.setRange(0, 100)
        self.Y_AXIS.setRange(0, 100)
        self._chart.setAxisX(self.X_AXIS)
        self._chart.setAxisY(self.Y_AXIS)
        if self._mline:
            for line in self.lines:
                self._chart.addSeries(line.line)
                self._chart.addSeries(line.point)
        else:
            self._chart.addSeries(self.lines.line)
            self._chart.addSeries(self.lines.point)
        self._chart.setTitle(f"{self.Title} 0 {self.Unit}")
        self.Graph.setChart(self._chart)
        self.Graph.setRenderHint(QPainter.Antialiasing)

    def __eq__(self, other: object) -> bool:
        return self.Graph == other.Graph

    def update(self, x):
        Maxx = []
        Minx = []
        Maxy = []
        Miny = []
        for line in self.lines:
            self._chart.removeSeries(line.line)
            self._chart.removeSeries(line.point)
            self._chart.addSeries(line.line)
            self._chart.addSeries(line.point)
            Maxx.append(max(line.x))
            Minx.append(min(line.x))
            Maxy.append(max(line.y))
            Miny.append(min(line.y))
        self._chart.setTitle(f"{self.Title} {x} {self.Unit}")
        self.X_AXIS.setRange(min(Minx), max(Maxx))
        self.Y_AXIS.setRange(min(Miny), max(Maxy))


class Graph:
    def __init__(self, graph: pyqtgraph.PlotWidget):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    window.resize(440, 300)

    sys.exit(app.exec())
