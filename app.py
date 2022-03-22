from PyQt5 import QtCore
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtGui import QFont
from pyqtgraph import PlotWidget
from port import DisconnectException
from datetime import datetime

from ui.mainwindow_ui import Ui_MainWindow
from communication import TelemetryHandler, Port
from logger import logger
# from chart import GraphicGraph
from rtc import RTC
import settings

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from folium.folium import Map
from folium import Marker, Icon
import sys
import io
import time
import pyqtgraph as pg
import csv
import simplekml
import paho.mqtt.client as mqtt


class App(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Initialize main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        # self.showMaximized()

        # Initialize map
        # self.ui.gps_map.setHtml(
        #     '<h1 style="height: 100%; text-align: center; font-family: Inter; background-color: #1c1c28; color: white;">No Data Available</h1>')
        self.map_initialized = False

        # Initilize MQTT
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = lambda client, userdata, flags, rc: print(
            "Connected to MQTT broker with result code "+str(rc))
        self.mqtt_client.on_message = lambda client, userdata, msg: print(
            msg.topic+" "+str(msg.payload))
        self.mqtt_client.username_pw_set('1022', 'Teasgote783')
        try:
            self.mqtt_client.connect("cansat.info", 1883)
        except Exception:
            logger.warn('Cannot connect to MQTT broker')
            self.ui.telemetry_log.append('❌ Cannot connect to MQTT broker')

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
        self.c_lat_data = []
        self.c_lng_data = []
        self.p_temp_data = []
        self.p_altitude_data = []
        self.p_gyro_r_data = []
        self.p_gyro_p_data = []
        self.p_gyro_y_data = []
        self.p_accel_r_data = []
        self.p_accel_p_data = []
        self.p_accel_y_data = []
        self.p_mag_r_data = []
        self.p_mag_p_data = []
        self.p_mag_y_data = []
        self.p_ptr_err_data = []
        self.p_voltage_data = []
        self.coords = []

        for g in graphs:
            self.formatGraph(g[0], g[1], g[2])

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
        self.telemetry_thread.requestHalt.connect(self.stop_lifecycle)

        self.updateCmdPreview()

        # Connect UI components
        self.connect()

    def init_lifecycle(self):
        logger.info('Starting lifecycle ...')

        # Start timing
        self.rtc = RTC()

        logger.debug(self.current_port)
        self.telemetry = TelemetryHandler(self.current_port)

        self.lifecycle_thread.start()
        self.telemetry_thread.start()

        self.ui.telemetry_box.setEnabled(True)
        self.ui.start_button.pressed.disconnect()
        self.ui.start_button.pressed.connect(self.stop_lifecycle)
        self.ui.start_button.setText('PAUSE')

    def stop_lifecycle(self):
        logger.info('Stopping lifecycle ...')
        self.lifecycle_thread.stop()
        self.telemetry_thread.stop()

        self.telemetry.destroy()

        self.ui.telemetry_box.setEnabled(False)
        self.ui.start_button.pressed.disconnect()
        self.ui.start_button.pressed.connect(self.init_lifecycle)
        self.ui.start_button.setText('RESUME')
        self.refreshPort()

    def lifecycle(self):
        '''
        Continuous tasks go here
        '''
        self.ui.mission_time.setText(self.rtc.time_UTC())
        self.ui.elapsed_time.setText('T + '+self.rtc.time_elapsed())

        self.ui.total_pkg_value.setText(str(
            self.container_healthy_pkg+self.container_corrupted_pkg+self.payload_healthy_pkg+self.payload_corrupted_pkg))
        self.ui.total_corrupted_pkg_value.setText(
            str(self.container_corrupted_pkg+self.payload_corrupted_pkg))

    def connect(self):
        '''
        Connect UI components with their respective functions.
        '''
        self.ui.actionParachute.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'PARADEPLOY'))
        self.ui.actionPoll.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'POLL'))
        self.ui.actionReset_Camera_Rotation.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'RESETCAM'))
        self.ui.actionCalibrate_Gimbal_IMU.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'CALCAM'))
        self.ui.actionRelease_Sequence.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'SEQUENCE'))
        self.ui.actionHalt_Sequence.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'HALT'))
        self.ui.actionRelease.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'RELEASE'))
        self.ui.actionBreak.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'BREAK'))
        self.ui.action1_PRELAUNCH.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'STATE1'))
        self.ui.action2_LAUNCH.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'STATE2'))
        self.ui.action3_PARADEPLOY.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'STATE3'))
        self.ui.action4_TPDEPLOY.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'STATE4'))
        self.ui.action5_RELEASED.triggered.connect(
            lambda: self.telemetry.sendCommand('FORCE', 'STATE5'))

        self.ui.actionFull_Screen.triggered.connect(self.toggleFullScreen)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.port_value.currentTextChanged.connect(
            lambda text: self.selectPort(text))
        self.ui.port_refresh_button.pressed.connect(self.refreshPort)
        self.ui.sim_file_button.pressed.connect(self.selectSimFile)

        self.ui.cmd_select_box.currentTextChanged.connect(
            self.updateCmdPreview)
        self.ui.cmdSendButton_2.pressed.connect(self.sendControlCommand)

        self.ui.start_button.pressed.connect(self.init_lifecycle)

    def handleTelemetry(self, data: str):
        # Display in log widget
        if(not data or data == '\r' or data == '\n'):
            return
        self.ui.telemetry_log.append(f'📩 {data}')
        if self.ui.autoscroll_check.isChecked():
            scrollbar = self.ui.telemetry_log.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
        if data is None:
            logger.error('Received data is None')
            return
        pkg = data.split(',')
        self.mqtt_client.publish('teams/1022', data)

        # Determine package origin
        if pkg[3] == 'C':
            # logger.info(f'[CANSAT] :{data}')
            with open('Flight_1022_C_with_corrupted.csv', 'a') as f:
                f.write(data+'\n')
            self.latest_container_telemetry = pkg[:]
            self.updateContainer()
        elif pkg[3] == 'T':
            # logger.info(f'[PAYLOAD]: {data}')
            with open('Flight_1022_T_with_corrupted.csv', 'a') as f:
                f.write(data+'\n')
            self.latest_payload_telemetry = pkg[:]
            self.updatePayload()

    def updateCmdPreview(self):
        command = self.ui.cmd_select_box.currentText()
        if hasattr(self, 'settime_preview_timer'):
            self.settime_preview_timer.stop()
        if command == 'Power ON':
            self.ui.cmd_preview.setText(
                TelemetryHandler.previewSendCommand('CX', 'ON'))
        if command == 'Power OFF':
            self.ui.cmd_preview.setText(
                TelemetryHandler.previewSendCommand('CX', 'OFF'))
        if command == 'Set Time':
            self.ui.cmd_preview.setText(
                TelemetryHandler.previewSendCommand('ST', datetime.utcnow().strftime('%H:%M:%S')))
            self.settime_preview_timer = QTimer()
            self.settime_preview_timer.timeout.connect(lambda: self.ui.cmd_preview.setText(
                TelemetryHandler.previewSendCommand('ST', datetime.utcnow().strftime('%H:%M:%S'))))
            self.settime_preview_timer.start(1000)

        if command == 'SIM Enable':
            self.ui.cmd_preview.setText(
                TelemetryHandler.previewSendCommand('SIM', 'ENABLE'))
        if command == 'SIM Activate':
            self.ui.cmd_preview.setText(
                TelemetryHandler.previewSendCommand('SIM', 'ACTIVATE'))
            self.startSim()
        if command == 'SIM Disable':
            self.ui.cmd_preview.setText(
                TelemetryHandler.previewSendCommand('SIM', 'DISABLE'))

    def sendControlCommand(self):
        if not hasattr(self, 'telemetry') or self.telemetry is None:
            logger.warning(
                'Unable to send command (no telemetry object found)')
            self.ui.telemetry_log.append(
                'Unable to send command (no telemetry object found)')
            return
        self.telemetry.sendRawCommand(self.ui.cmd_preview.text())
        self.ui.telemetry_log.append(f'📨 {self.ui.cmd_preview.text()}')

    def updateContainer(self):
        # Destructuring telemetry data
        try:
            TEAM_ID, MISSION_TIME, PACKET_COUNT, PACKET_TYPE, MODE, TP_RELEASED, ALTITUDE, TEMP, VOLTAGE, GPS_TIME, GPS_LATITUDE, GPS_LONGITUDE, GPS_ALTITUDE, GPS_SATS, SOFTWARE_STATE, CMD_ECHO = self.latest_container_telemetry
            self.container_healthy_pkg += 1
            self.ui.c_healthy_pkg_count.setText(
                str(self.container_healthy_pkg))
            with open('Flight_1022_C.csv', 'a') as file:
                file.write(','.join(self.latest_container_telemetry)+'\n')

        except Exception:
            self.container_corrupted_pkg += 1
            self.ui.c_corrupted_pkg_count.setText(
                str(self.container_corrupted_pkg))
            logger.warning(
                f'Corrupted packet: {self.latest_container_telemetry}')
            return

        # Update data
        self.c_pkg_data.append(
            self.container_healthy_pkg if settings.PACKET_COUNT_ORIGIN == 'local' else int(PACKET_COUNT))
        self.c_temp_data.append(float(TEMP))
        self.c_altitude_data.append(float(ALTITUDE))
        self.c_gps_altitude_data.append(float(GPS_ALTITUDE))
        self.c_voltage_data.append(float(VOLTAGE))
        self.c_lat_data = GPS_LATITUDE
        self.c_lng_data = GPS_LONGITUDE
        self.ui.c_state.setText(SOFTWARE_STATE)

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

        # Update battery
        bat_percent = self.batteryPercentage(float(VOLTAGE))
        self.ui.container_battery_percent.setText(
            f'{bat_percent.__round__(2)}%')
        self.ui.c_battery_visual.setValue(int(bat_percent))

        self.ui.last_cmd_value.setText(CMD_ECHO)

    def updatePayload(self):
        # Destructuring telemetry data
        try:
            TEAM_ID, MISSION_TIME, PACKET_COUNT, PACKET_TYPE, TP_ALTITUDE, TP_TEMP, TP_VOLTAGE, GYRO_R, GYRO_P, GYRO_Y, ACCEL_R, ACCEL_P, ACCEL_Y, MAG_R, MAG_P, MAG_Y, POINTING_ERROR, TP_SOFTWARE_STATE = self.latest_payload_telemetry
            self.payload_healthy_pkg += 1
            self.ui.p_healthy_pkg_count.setText(
                str(self.payload_healthy_pkg))
            with open('Flight_1022_T.csv', 'a') as file:
                file.write(','.join(self.latest_payload_telemetry)+'\n')
        except Exception:
            self.payload_corrupted_pkg += 1
            self.ui.p_corrupted_pkg_count.setText(
                str(self.payload_corrupted_pkg))
            logger.warning(
                f'Corrupted packet: {self.latest_payload_telemetry}')
            return

        # Update data
        self.p_pkg_data.append(
            self.payload_healthy_pkg if settings.PACKET_COUNT_ORIGIN == 'local' else int(PACKET_COUNT))
        self.p_temp_data.append(float(TP_TEMP))
        self.p_altitude_data.append(float(TP_ALTITUDE))
        self.p_gyro_r_data.append(float(GYRO_R))
        self.p_gyro_p_data.append(float(GYRO_P))
        self.p_gyro_y_data.append(float(GYRO_Y))
        self.p_accel_r_data.append(float(ACCEL_R))
        self.p_accel_p_data.append(float(ACCEL_P))
        self.p_accel_y_data.append(float(ACCEL_Y))
        self.p_mag_r_data.append(float(MAG_R))
        self.p_mag_p_data.append(float(MAG_P))
        self.p_mag_y_data.append(float(MAG_Y))
        self.p_ptr_err_data.append(float(POINTING_ERROR))
        self.p_voltage_data.append(float(TP_VOLTAGE))
        self.ui.p_state.setText(TP_SOFTWARE_STATE)

        # Update chart
        self.plot(self.ui.p_temp_chart, self.p_pkg_data, self.p_temp_data)
        self.plot(self.ui.p_gyro_chart,
                  self.p_pkg_data, (self.p_gyro_r_data, self.p_gyro_p_data, self.p_gyro_y_data))
        self.plot(self.ui.p_accel_chart,
                  self.p_pkg_data, (self.p_accel_r_data, self.p_accel_p_data, self.p_accel_y_data))
        self.plot(self.ui.p_mag_chart,
                  self.p_pkg_data, (self.p_mag_r_data, self.p_mag_p_data, self.p_mag_y_data))
        self.plot(self.ui.p_ptr_err_chart,
                  self.p_pkg_data, self.p_ptr_err_data)
        self.plot(self.ui.p_voltage_chart,
                  self.p_pkg_data, self.p_voltage_data)

        # Update battery
        bat_percent = self.batteryPercentage(float(TP_VOLTAGE))
        self.ui.payload_battery_percent.setText(
            f'{bat_percent.__round__(2)}%')
        self.ui.p_battery_visual.setValue(int(bat_percent))

    # def appendData(self, data: list, new_data):
    #     data.append(new_data)
    #     if data.__len__() > 30:
    #         data.pop(0)

    def formatGraph(self, graph: PlotWidget, title: str, unit: str = ''):
        graph.setTitle(title)
        graph.setLabel('left', f'{title} ({unit})')
        graph.setLabel('bottom', 'Packet Count')
        graph.getAxis(
            'bottom').setTickFont(QFont("Consolas"))
        graph.getAxis(
            'left').setTickFont(QFont("Consolas"))

    def plot(self, chart: PlotWidget, x: list, y: list, **options):
        plottingThread = PlottingThread(chart, x, y, **options)
        plottingThread.start()

    def batteryPercentage(self, voltage: float):
        return ((voltage-5.2)/3.2)*100

    def startSim(self):
        if hasattr(self, 'sim_thread'):
            logger.warning('Sim timer already exist, not starting')
            return
        self.sim_thread = SimThread()
        self.sim_thread.start()

    def stopSim(self):
        if not hasattr(self, 'sim_thread'):
            logger.warn('Sim timer does not exist, not stopping')

    def selectPort(self, port_name: str):
        logger.debug(f'Selecting port name: {port_name}')
        self.current_port = port_name
        if not self.lifecycle_thread.isRunning():
            return
        if hasattr(self, 'telemetry') and self.telemetry is not None:
            self.telemetry.setPort(port_name)
        else:
            self.telemetry = TelemetryHandler(port_name)

    def refreshPort(self):
        logger.debug('Refreshing ports')
        self.ui.port_value.clear()
        self.ui.port_value.addItems(Port.list())

    def selectSimFile(self):
        self.sim_filename, _ = QFileDialog.getOpenFileName(
            filter='CSV Files (*.csv);;All Files (*)', caption='Open simulation file')
        self.ui.sim_file_display.setText(self.sim_filename.split('/')[-1])

    def updateMap(self, coords: tuple):
        # self.coords.append(coords)
        # kml = simplekml.Kml()
        # kml.newpoint(coords=self.coords)
        # kml.save("Save.kml")
        self.coords += f'{coords[1]},{coords[0]},{self.c_gps_altitude_data[-1]}\n'
        with open('data.kml', 'w') as file:
            file.writelines('<kml xmlns="http://www.opengis.net/kml/2.2" '
                            'xmlns:gx="http://www.google.com/kml/ext/2.2">'
                            '<Folder><name>Log</name><Placemark><name>SPOROS</name>'
                            '<styleUrl>#yellowLineGreenPoly</styleUrl><Style>'
                            '<LineStyle><color>ff00ffff</color><colorMode>normal</colorMode><width>4</width></LineStyle>'
                            '</Style><LineString><extrude>1</extrude><altitudeMode>absolute</altitudeMode><coordinates>'+'\n')
            file.writelines(self.coords)
            file.writelines(
                '\n' + '</coordinates></LineString></Placemark></Folder></kml>')
        # pass
        # self.ui.lat_value.setText(str(coords[0]))
        # self.ui.lng_value.setText(str(coords[1]))
        # if self.map_initialized:
        #     self.map
        #     Marker(
        #         location=coords,
        #         popup=str(self.c_pkg_data[-1] + 1) + ' : ' +
        #         str(self.c_altitude_data) + 'm',
        #         icon=Icon(),
        #     ).add_to(self.map)
        # else:
        #     self.map = Map(location=coords, zoom_start=16,
        #                    min_zoom=10, prefer_canvas=True)
        # self.map_data = io.BytesIO()
        # self.map.save(self.map_data, close_file=False)
        # self.ui.gps_map.setHtml(self.map_data.getvalue().decode())
        # self.map_initialized = True

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
        logger.info('Lifecycle thread stopped')


class PlottingThread(QThread):

    # Carriers
    # lifecycleRequested = QtCore.pyqtSignal(object)

    def __init__(self, chart: PlotWidget, x: list, y: list, **options):
        self.chart = chart
        self.x = x
        self.y = y
        self.options = options
        self._isRunning = True
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        logger.info('Plotting thread started')
        plot_options = {
            **{'x': self.x, 'y': self.y, 'symbol': 'o', 'symbolSize': 6}, **self.options}
        # print(plot_options)
        # chart.plot()
        # print(self.y[-30:-1])
        self.chart.clear()
        # self.chart.setRange(
        #     xRange=[window.c_pkg_data[-1]-30, window.c_pkg_data[-1]])
        if type(self.y) is tuple:
            self.chart.plot(**{'x': self.x[-30:-1], 'y': self.y[0][-30:-1],
                               'symbol': 'o', 'symbolSize': 6, 'symbolPen': 'r', 'pen': 'r'})
            self.chart.plot(**{'x': self.x[-30:-1], 'y': self.y[1][-30:-1],
                               'symbol': 'o', 'symbolSize': 6, 'symbolPen': 'g', 'pen': 'g'})
            self.chart.plot(**{'x': self.x[-30:-1], 'y': self.y[2][-30:-1],
                               'symbol': 'o', 'symbolSize': 6, 'symbolPen': 'c', 'pen': 'c'})
        else:
            self.chart.plot(**{'x': self.x[-30:-1], 'y': self.y[-30:-1],
                               'symbol': 'o', 'symbolSize': 6})
        # self.plot()

    # def plot(self):

    def stop(self):
        self._isRunning = False
        self.terminate()


class TelemetryThread(QThread):

    # Carriers
    received = QtCore.pyqtSignal(object)
    requestHalt = QtCore.pyqtSignal(object)

    def __init__(self):
        self._isRunning = True
        super(TelemetryThread, self).__init__(None)

    def __del__(self):
        self.wait()

    def run(self):
        logger.info('Telemetry thread started')
        while True:
            try:
                incoming_data = window.telemetry.read()
            except DisconnectException:
                self.requestHalt.emit(None)
                return
            self.received.emit(incoming_data)

    def stop(self):
        self._isRunning = False
        self.terminate()
        logger.info('Telemetry thread stopped')


class SimThread(QThread):
    def __init__(self):
        self._isRunning = True
        super(SimThread, self).__init__(None)

    def __del__(self):
        self.wait()

    def run(self):
        logger.info('Sim thread started')
        while True:
            with open(window.sim_filename) as file:
                data = file.readlines()
                for line in data:
                    window.telemetry.sendRawCommand(line)
                    window.ui.telemetry_log.append(f'📨 {line}')
                    time.sleep(1)

    def stop(self):
        self._isRunning = False
        self.terminate()
        logger.info('Sim thread stopped')


if __name__ == '__main__':
    pg.setConfigOption('foreground', 'w')
    pg.setConfigOption('background', '28293d')
    pg.setConfigOption('antialias', True)
    # pg.setConfigOption('readonly', True)

    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.showMaximized()
    # window.showFullScreen()

    # window.updateMap((13.67876, 100.52819))

    try:

        logger.info('Starting window ...')
        sys.exit(app.exec_())
    except SystemExit:
        logger.info('Closing window ...')
