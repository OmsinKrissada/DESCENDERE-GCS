from PyQt5 import QtCore
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtGui import QFont
from pyqtgraph.widgets.PlotWidget import PlotWidget
from ui.mainwindow_ui import Ui_MainWindow

from communication import TelemetryHandler, Port
from logger import logger
from chart import GraphicGraph
from rtc import RTC
import settings

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from folium.folium import Map
import sys
import io
import time
import threading
import pyqtgraph as pg


class App(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Initialize main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        # self.showMaximized()

        # Initialize map
        self.ui.gps_map.setHtml(
            '<h1 style="height: 100%; text-align: center; font-family: Inter; background-color: #1c1c28; color: white;">No Data Available</h1>')

        # Initialize charts
        graphs = [
            [self.ui.c_temp_chart, 'Temperature', '°C'],
            [self.ui.c_altitude_chart, 'Altitude', 'm'],
            [self.ui.c_gps_altitude_chart, 'GPS Altitude', 'm'],
            [self.ui.c_voltage_chart, 'Voltage', 'V'],
            [self.ui.p_temp_chart, 'Temperature', '°C'],
            [self.ui.p_gyro_chart, 'Gyroscope', 'degrees/s'],
            [self.ui.p_accel_chart, 'Acceleration', 'm/s^2'],
            [self.ui.p_mag_chart, 'Magnatic Field', 'gauss'],
            [self.ui.p_ptr_err_chart, 'Pointing Error', 'degrees'],
            [self.ui.p_voltage_chart, 'Voltage', 'V'],
        ]

        # Initialize chart data
        self.container_healthy_pkg = 0
        self.container_corrupted_pkg = 0
        self.payload_healthy_pkg = 0
        self.payload_corrupted_pkg = 0

        self.c_pkg_data = []
        self.p_pkg_data = []

        self.c_temp_data = []
        self.c_altitude_data = []
        self.c_gps_altitude_data = []
        self.c_voltage_data = []
        self.p_temp_data = []
        self.p_gyro_data = []
        self.p_accel_data = []
        self.p_mag_data = []
        self.p_ptr_err_data = []
        self.p_voltage_data = []

        for i in graphs:
            self.formatGraph(i[0], i[1], i[2])

        # Start timing
        self.rtc = RTC()

        # Connect UI components
        self.connect()

        # Display available ports, if at least one available, initiate TelemetryHandler first in the list
        available_ports = Port.list()
        self.ui.port_value.addItems(available_ports)
        if available_ports:
            self.current_port = available_ports[0]
        else:
            self.current_port = None
            self.ui.port_value.setCurrentText('No Ports Available')

        self.lifecycle_thread = LifecycleThread()
        self.lifecycle_thread.lifecycleRequested.connect(self.lifecycle)
        self.telemetry_thread = TelemetryThread()
        self.telemetry_thread.received.connect(self.handleTelemetry)

    def init_lifecycle(self):
        self.started = True
        self.telemetry = TelemetryHandler(self.current_port)
        self.lifecycle_thread.start()
        self.telemetry_thread.start()

    def lifecycle(self):
        '''
        Continuous tasks go here
        '''
        self.ui.mission_time.setText(self.rtc.time_UTC())
        self.ui.elapsed_time.setText('T + '+self.rtc.time_elapsed())

        self.ui.total_pkg_value.setText(str(
            self.container_healthy_pkg+self.container_corrupted_pkg+self.payload_healthy_pkg+self.payload_corrupted_pkg))

    def handleTelemetry(self, data: str):
        # Display in log widget
        self.ui.telemetry_log.append(f'{data}')
        scrollbar = self.ui.telemetry_log.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

        pkg = data.split(',')

        # Determine package origin
        if pkg[3] == 'C':
            # logger.info(f'[CANSAT] :{data}')
            self.latest_container_telemetry = pkg[:]
            self.updateContainer()
        elif pkg[3] == 'P':
            # logger.info(f'[PAYLOAD]: {data}')
            self.latest_payload_telemetry = pkg[:]
            self.updatePayload()

    def updateContainer(self):
        try:
            TEAM_ID, MISSION_TIME, PACKET_COUNT, PACKET_TYPE, MODE, TP_RELEASED, ALTITUDE, TEMP, VOLTAGE, GPS_TIME, GPS_LATITUDE, GPS_LONGITUDE, GPS_ALTITUDE, GPS_SATS, SOFTWARE_STATE, CMD_ECHO = self.latest_container_telemetry
            self.container_healthy_pkg += 1
            self.ui.c_healthy_pkg_count.setText(
                str(self.container_healthy_pkg))
        except Exception:
            self.container_corrupted_pkg += 1
            self.ui.c_corrupted_pkg_count.setText(
                str(self.container_corrupted_pkg))
            logger.warning(
                f'Corrupted packet: {self.latest_container_telemetry}')
        # Update data
        self.c_pkg_data.append(
            self.container_healthy_pkg if settings.PACKET_COUNT_ORIGIN == 'local' else int(PACKET_COUNT))
        self.c_temp_data.append(float(TEMP))
        self.c_altitude_data.append(float(ALTITUDE))
        self.c_gps_altitude_data.append(float(GPS_ALTITUDE))
        self.c_voltage_data.append(float(VOLTAGE))
        # Update chart
        self.plot(self.ui.c_temp_chart, self.c_pkg_data, self.c_temp_data)
        self.plot(self.ui.c_altitude_chart,
                  self.c_pkg_data, self.c_altitude_data)
        self.plot(self.ui.c_gps_altitude_chart,
                  self.c_pkg_data, self.c_gps_altitude_data)
        self.plot(self.ui.c_voltage_chart,
                  self.c_pkg_data, self.c_voltage_data)
        # Update map
        self.updateMap((GPS_LATITUDE, GPS_LONGITUDE))
        self.ui.lat_value.setText(GPS_LATITUDE)
        self.ui.lng_value.setText(GPS_LONGITUDE)
        self.ui.sats_value.setText(GPS_SATS)

    def updatePayload(self):
        pass

    def formatGraph(self, graph: PlotWidget, title: str, unit: str = ''):
        graph.setTitle(title)
        graph.setLabel('left', f'{title} ({unit})')
        graph.setLabel('bottom', 'Packet Count')
        graph.getAxis(
            'bottom').setTickFont(QFont("Consolas"))
        graph.getAxis(
            'left').setTickFont(QFont("Consolas"))
        # graph.plot(symbol='o')
        # graph.setLimits(xMax=b)

    def plot(self, chart: PlotWidget, x: list, y: list, **options):
        plot_options = {
            **{'x': x, 'y': y, 'symbol': 'o', 'symbolSize': 6}, **options}
        # print(plot_options)
        # chart.plot()
        print(y[-30:-1])
        chart.setRange(xRange=[self.c_pkg_data[-1]-30, self.c_pkg_data[-1]])
        chart.plot(**{'x': x[-30:-1], 'y': y[-30:-1],
                   'symbol': 'o', 'symbolSize': 6})

    # def stop(self):
    #     self._isRunning = False

    def connect(self):
        '''
        Connect UI components with their respective functions.
        '''
        self.ui.actionForce_parachute_deployment.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'PARADEPLOY'))
        self.ui.actionForce_parachute_deployment.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'TIMEDPL'))
        self.ui.actionForce_parachute_deployment.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'BEGINPL'))
        self.ui.actionForce_parachute_deployment.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'STOPPL'))
        self.ui.actionForce_parachute_deployment.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'RESETCAMPOS'))

        self.ui.actionFull_Screen.triggered.connect(self.toggleFullScreen)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.cmdSendButton_2.pressed.connect(
            lambda: self.sendCommand(self.ui.cmd_input.text))
        self.ui.port_refresh_button.pressed.connect(self.refreshPort)
        self.ui.port_value.currentTextChanged.connect(
            lambda text: self.selectPort(text))
        self.ui.start_button.pressed.connect(self.init_lifecycle)

    def selectPort(self, port_name: str):
        if not self.started:
            return
        if self.telemetry:
            self.telemetry.setPort(port_name)
        else:
            print('selecting port')
            self.telemetry = TelemetryHandler(port_name)

    def refreshPort(self):
        self.ui.port_value.clear()
        self.ui.port_value.addItems(Port.list())

    def updateMap(self, coords: tuple):
        self.ui.lat_value.setText(str(coords[0]))
        self.ui.lng_value.setText(str(coords[1]))
        self.map = Map(location=coords)
        self.map_data = io.BytesIO()
        self.map.save(self.map_data, close_file=False)
        self.ui.gps_map.setHtml(self.map_data.getvalue().decode())

    def sendCommand(self, command: str):
        self.telemetry.sendCommand(command)
        logger.debug(command)
        print(command)
        # self.ui.cmdPreview.setText(command)

    def toggleFullScreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


class LifecycleThread(QThread):

    # Carriers
    lifecycleRequested = QtCore.pyqtSignal(object)

    def __init__(self):
        self._isRunning = True
        super(LifecycleThread, self).__init__(None)

    def __del__(self):
        self.wait()

    def run(self):
        logger.info('Lifecycle thread started')
        while True:
            self.lifecycleRequested.emit(None)
            time.sleep(0.001)  # Not to consume too much processing power

    def stop(self):
        self._isRunning = False
        self.terminate()


class TelemetryThread(QThread):

    # Carriers
    received = QtCore.pyqtSignal(object)

    def __init__(self):
        self._isRunning = True
        super(TelemetryThread, self).__init__(None)

    def __del__(self):
        self.wait()

    def run(self):
        logger.info('Telemetry thread started')
        while True:
            incoming_data = window.telemetry.read()
            self.received.emit(incoming_data)

    def stop(self):
        self._isRunning = False
        self.terminate()


if __name__ == '__main__':
    pg.setConfigOption('foreground', 'w')
    pg.setConfigOption('background', '28293d')
    pg.setConfigOption('antialias', True)
    # pg.setConfigOption('font', 'Consolas')

    app = QtWidgets.QApplication(sys.argv)
    window = App()
    # window.showFullScreen()

    # window.updateMap((13.67876, 100.52819))

    try:

        logger.info('Starting window ...')
        sys.exit(app.exec_())
    except SystemExit:
        logger.info('Closing window ...')
