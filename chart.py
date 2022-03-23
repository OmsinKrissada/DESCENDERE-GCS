from pyqtgraph import PlotWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QFont
from typing import Union

from logger import logger


class Chart:
    def __init__(self, chart: PlotWidget, display: QLabel, unit: str = ''):
        self.chart = chart
        self.display = display
        self.unit = unit
        self.formatGraph()

    def formatGraph(self):
        # graph.setTitle(title)
        self.chart.setLabel('left', f'Value ({self.unit})')
        self.chart.setLabel('bottom', 'Packet Count')
        self.chart.getAxis(
            'bottom').setTickFont(QFont("Consolas"))
        self.chart.getAxis(
            'left').setTickFont(QFont("Consolas"))

    def plot(self, x: list, y: Union[list, tuple], **options):
        plottingThread = PlottingThread(
            self.chart, self.display, x, y, self.unit, **options)
        plottingThread.start()


class PlottingThread(QThread):
    def __init__(self, chart: PlotWidget, display: QLabel, x: list, y: list, unit: str, **options):
        self.chart = chart
        self.x = x
        self.y = y
        self.display = display
        self.unit = unit
        self.options = options
        self._isRunning = True
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        logger.info('Plotting thread started')
        self.chart.clear()
        if type(self.y) is tuple:
            self.display.setText(
                f'{self.y[0][-1]}, {self.y[1][-1]}, {self.y[2][-1]} {self.unit}')
            self.chart.plot(**{'x': self.x[-30:-1], 'y': self.y[0][-30:-1],
                               'symbol': 'o', 'symbolSize': 6, 'symbolPen': 'r', 'pen': 'r'})
            self.chart.plot(**{'x': self.x[-30:-1], 'y': self.y[1][-30:-1],
                               'symbol': 'o', 'symbolSize': 6, 'symbolPen': 'g', 'pen': 'g'})
            self.chart.plot(**{'x': self.x[-30:-1], 'y': self.y[2][-30:-1],
                               'symbol': 'o', 'symbolSize': 6, 'symbolPen': 'c', 'pen': 'c'})
        else:
            self.display.setText(f'{self.y[-1]} {self.unit}')
            self.chart.plot(**{'x': self.x[-30:-1], 'y': self.y[-30:-1],
                               'symbol': 'o', 'symbolSize': 6})

    def stop(self):
        self._isRunning = False
        self.terminate()
