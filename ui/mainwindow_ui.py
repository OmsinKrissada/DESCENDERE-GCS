# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTextBrowser, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Inter"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #1c1c28;")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.actionCSVLocation = QAction(MainWindow)
        self.actionCSVLocation.setObjectName(u"actionCSVLocation")
        self.actionReset_Camera_Rotation = QAction(MainWindow)
        self.actionReset_Camera_Rotation.setObjectName(u"actionReset_Camera_Rotation")
        self.actionParachute = QAction(MainWindow)
        self.actionParachute.setObjectName(u"actionParachute")
        self.actionForce_2nd_parachute_deployment = QAction(MainWindow)
        self.actionForce_2nd_parachute_deployment.setObjectName(u"actionForce_2nd_parachute_deployment")
        self.actionForce_stop_payload_deployment = QAction(MainWindow)
        self.actionForce_stop_payload_deployment.setObjectName(u"actionForce_stop_payload_deployment")
        self.actionFull_Screen = QAction(MainWindow)
        self.actionFull_Screen.setObjectName(u"actionFull_Screen")
        self.actionFull_Screen.setShortcutVisibleInContextMenu(False)
        self.actionForce_timed_payload_deployment = QAction(MainWindow)
        self.actionForce_timed_payload_deployment.setObjectName(u"actionForce_timed_payload_deployment")
        self.actionOpen_simulation_file = QAction(MainWindow)
        self.actionOpen_simulation_file.setObjectName(u"actionOpen_simulation_file")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionEnable = QAction(MainWindow)
        self.actionEnable.setObjectName(u"actionEnable")
        self.actionEnable.setCheckable(True)
        self.actionDisable = QAction(MainWindow)
        self.actionDisable.setObjectName(u"actionDisable")
        self.actionPoll = QAction(MainWindow)
        self.actionPoll.setObjectName(u"actionPoll")
        self.actionStart_break_sequence = QAction(MainWindow)
        self.actionStart_break_sequence.setObjectName(u"actionStart_break_sequence")
        self.actionRelease_Sequence = QAction(MainWindow)
        self.actionRelease_Sequence.setObjectName(u"actionRelease_Sequence")
        self.actionRelease = QAction(MainWindow)
        self.actionRelease.setObjectName(u"actionRelease")
        self.actionBreak = QAction(MainWindow)
        self.actionBreak.setObjectName(u"actionBreak")
        self.actionCalibrate_Gimbal_IMU = QAction(MainWindow)
        self.actionCalibrate_Gimbal_IMU.setObjectName(u"actionCalibrate_Gimbal_IMU")
        self.actionHalt_Sequence = QAction(MainWindow)
        self.actionHalt_Sequence.setObjectName(u"actionHalt_Sequence")
        self.action0_PRELAUNCH = QAction(MainWindow)
        self.action0_PRELAUNCH.setObjectName(u"action0_PRELAUNCH")
        self.action1_LAUNCH = QAction(MainWindow)
        self.action1_LAUNCH.setObjectName(u"action1_LAUNCH")
        self.action2_PARADEPLOY = QAction(MainWindow)
        self.action2_PARADEPLOY.setObjectName(u"action2_PARADEPLOY")
        self.action3_TPDEPLOY = QAction(MainWindow)
        self.action3_TPDEPLOY.setObjectName(u"action3_TPDEPLOY")
        self.action4_RELEASED = QAction(MainWindow)
        self.action4_RELEASED.setObjectName(u"action4_RELEASED")
        self.action5_LAND = QAction(MainWindow)
        self.action5_LAND.setObjectName(u"action5_LAND")
        self.actionForce_Polling_Payload = QAction(MainWindow)
        self.actionForce_Polling_Payload.setObjectName(u"actionForce_Polling_Payload")
        self.actionUnforce_Polling_Payload = QAction(MainWindow)
        self.actionUnforce_Polling_Payload.setObjectName(u"actionUnforce_Polling_Payload")
        self.actionMode0 = QAction(MainWindow)
        self.actionMode0.setObjectName(u"actionMode0")
        self.actionMode1 = QAction(MainWindow)
        self.actionMode1.setObjectName(u"actionMode1")
        self.actionPayload_On = QAction(MainWindow)
        self.actionPayload_On.setObjectName(u"actionPayload_On")
        self.actionPayload_Off = QAction(MainWindow)
        self.actionPayload_Off.setObjectName(u"actionPayload_Off")
        self.actionToggle_Container_Camera = QAction(MainWindow)
        self.actionToggle_Container_Camera.setObjectName(u"actionToggle_Container_Camera")
        self.actionToggle_Custom_Packet = QAction(MainWindow)
        self.actionToggle_Custom_Packet.setObjectName(u"actionToggle_Custom_Packet")
        self.actionMode_2 = QAction(MainWindow)
        self.actionMode_2.setObjectName(u"actionMode_2")
        self.actionMode_3 = QAction(MainWindow)
        self.actionMode_3.setObjectName(u"actionMode_3")
        self.actionMode_4 = QAction(MainWindow)
        self.actionMode_4.setObjectName(u"actionMode_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"color: white;\n"
"background-color: #1c1c28;\n"
"border-radius: 20px;")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(18, -1, 18, -1)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Demi"])
        font1.setPointSize(25)
        self.label_8.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_8)


        self.gridLayout_6.addWidget(self.widget_2, 0, 0, 1, 1)

        self.config_box = QWidget(self.centralwidget)
        self.config_box.setObjectName(u"config_box")
        self.config_box.setMinimumSize(QSize(311, 151))
        font2 = QFont()
        font2.setPointSize(10)
        self.config_box.setFont(font2)
        self.config_box.setStyleSheet(u"color: white;\n"
"background-color: rgb(40, 41, 61);\n"
"border-radius: 20px;")
        self.gridLayout_4 = QGridLayout(self.config_box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.mission_time = QLabel(self.config_box)
        self.mission_time.setObjectName(u"mission_time")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mission_time.sizePolicy().hasHeightForWidth())
        self.mission_time.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Cascadia Code"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.mission_time.setFont(font3)
        self.mission_time.setStyleSheet(u"")
        self.mission_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.mission_time)

        self.reset_button = QPushButton(self.config_box)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setMaximumSize(QSize(80, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Inter"])
        font4.setPointSize(9)
        self.reset_button.setFont(font4)
        self.reset_button.setLayoutDirection(Qt.LeftToRight)
        self.reset_button.setStyleSheet(u"padding: 6px;\n"
"background-color: #434350;\n"
"border-radius: 5px;")

        self.horizontalLayout_28.addWidget(self.reset_button)


        self.gridLayout_4.addLayout(self.horizontalLayout_28, 0, 0, 1, 3)

        self.label_10 = QLabel(self.config_box)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setFamilies([u"Inter"])
        font5.setPointSize(12)
        self.label_10.setFont(font5)

        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)

        self.port_value = QComboBox(self.config_box)
        self.port_value.setObjectName(u"port_value")
        font6 = QFont()
        font6.setFamilies([u"Consolas"])
        font6.setPointSize(12)
        self.port_value.setFont(font6)
        self.port_value.setStyleSheet(u"padding: 5px;\n"
"background-color: rgba(231, 231, 231, 20);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.port_value, 1, 1, 1, 1)

        self.port_refresh_button = QPushButton(self.config_box)
        self.port_refresh_button.setObjectName(u"port_refresh_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.port_refresh_button.sizePolicy().hasHeightForWidth())
        self.port_refresh_button.setSizePolicy(sizePolicy1)
        self.port_refresh_button.setMaximumSize(QSize(110, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Inter"])
        font7.setPointSize(9)
        font7.setBold(False)
        self.port_refresh_button.setFont(font7)
        self.port_refresh_button.setStyleSheet(u"padding: 6px;\n"
"background-color: #434350;\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.port_refresh_button, 1, 2, 1, 1)

        self.label_11 = QLabel(self.config_box)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)

        self.sim_file_display = QLabel(self.config_box)
        self.sim_file_display.setObjectName(u"sim_file_display")
        self.sim_file_display.setEnabled(False)
        self.sim_file_display.setFont(font5)
        self.sim_file_display.setStyleSheet(u"padding: 5px;\n"
"background-color: rgba(231, 231, 231, 20);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.sim_file_display, 2, 1, 1, 1)

        self.sim_file_button = QPushButton(self.config_box)
        self.sim_file_button.setObjectName(u"sim_file_button")
        sizePolicy1.setHeightForWidth(self.sim_file_button.sizePolicy().hasHeightForWidth())
        self.sim_file_button.setSizePolicy(sizePolicy1)
        self.sim_file_button.setMaximumSize(QSize(110, 16777215))
        self.sim_file_button.setFont(font4)
        self.sim_file_button.setStyleSheet(u"padding: 6px;\n"
"background-color: #434350;\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.sim_file_button, 2, 2, 1, 1)


        self.gridLayout_6.addWidget(self.config_box, 0, 1, 1, 1)

        self.gps_box = QWidget(self.centralwidget)
        self.gps_box.setObjectName(u"gps_box")
        self.gps_box.setStyleSheet(u"color: white;\n"
"background-color: rgb(40, 41, 61);\n"
"border-radius: 20px;")
        self.verticalLayout_4 = QVBoxLayout(self.gps_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 18)
        self.header_box_3 = QGroupBox(self.gps_box)
        self.header_box_3.setObjectName(u"header_box_3")
        self.header_box_3.setMaximumSize(QSize(1079, 61))
        self.horizontalLayout_11 = QHBoxLayout(self.header_box_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.title_box_4 = QGroupBox(self.header_box_3)
        self.title_box_4.setObjectName(u"title_box_4")
        self.horizontalLayout_18 = QHBoxLayout(self.title_box_4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.line_5 = QFrame(self.title_box_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(62, 123, 250);\n"
"border-radius: 100px;")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.line_5)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)

        self.title_4 = QLabel(self.title_box_4)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setMaximumSize(QSize(16777215, 25))
        font8 = QFont()
        font8.setPointSize(16)
        font8.setBold(True)
        self.title_4.setFont(font8)
        self.title_4.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.title_4)


        self.horizontalLayout_11.addWidget(self.title_box_4)


        self.verticalLayout_4.addWidget(self.header_box_3)

        self.position_box = QGroupBox(self.gps_box)
        self.position_box.setObjectName(u"position_box")
        self.position_box.setMinimumSize(QSize(214, 40))
        self.horizontalLayout = QHBoxLayout(self.position_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lng_title_2 = QLabel(self.position_box)
        self.lng_title_2.setObjectName(u"lng_title_2")
        self.lng_title_2.setFont(font5)
        self.lng_title_2.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout.addWidget(self.lng_title_2)

        self.sats_value = QLabel(self.position_box)
        self.sats_value.setObjectName(u"sats_value")
        self.sats_value.setFont(font6)

        self.horizontalLayout.addWidget(self.sats_value)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lat_title = QLabel(self.position_box)
        self.lat_title.setObjectName(u"lat_title")
        self.lat_title.setFont(font5)
        self.lat_title.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout.addWidget(self.lat_title)

        self.lat_value = QLabel(self.position_box)
        self.lat_value.setObjectName(u"lat_value")
        self.lat_value.setFont(font6)

        self.horizontalLayout.addWidget(self.lat_value)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.lng_title = QLabel(self.position_box)
        self.lng_title.setObjectName(u"lng_title")
        self.lng_title.setFont(font5)
        self.lng_title.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout.addWidget(self.lng_title)

        self.lng_value = QLabel(self.position_box)
        self.lng_value.setObjectName(u"lng_value")
        self.lng_value.setFont(font6)

        self.horizontalLayout.addWidget(self.lng_value)


        self.verticalLayout_4.addWidget(self.position_box)


        self.gridLayout_6.addWidget(self.gps_box, 0, 2, 1, 1)

        self.container_box = QWidget(self.centralwidget)
        self.container_box.setObjectName(u"container_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.container_box.sizePolicy().hasHeightForWidth())
        self.container_box.setSizePolicy(sizePolicy2)
        self.container_box.setMinimumSize(QSize(1097, 361))
        self.container_box.setMaximumSize(QSize(16777215, 16777215))
        self.container_box.setStyleSheet(u"color: white;\n"
"background-color: rgb(40, 41, 61);\n"
"border-radius: 20px;")
        self.verticalLayout_6 = QVBoxLayout(self.container_box)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.header_box_2 = QGroupBox(self.container_box)
        self.header_box_2.setObjectName(u"header_box_2")
        self.header_box = QHBoxLayout(self.header_box_2)
        self.header_box.setObjectName(u"header_box")
        self.title_box = QGroupBox(self.header_box_2)
        self.title_box.setObjectName(u"title_box")
        self.horizontalLayout_4 = QHBoxLayout(self.title_box)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_2 = QFrame(self.title_box)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 25))
        self.line_2.setStyleSheet(u"background-color: rgb(62, 123, 250);\n"
"border-radius: 100px;")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.title = QLabel(self.title_box)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 25))
        self.title.setFont(font8)
        self.title.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.title)


        self.header_box.addWidget(self.title_box)

        self.battery_box = QGroupBox(self.header_box_2)
        self.battery_box.setObjectName(u"battery_box")
        self.battery_box.setFlat(False)
        self.horizontalLayout_6 = QHBoxLayout(self.battery_box)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_14 = QLabel(self.battery_box)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(61, 16777215))
        self.label_14.setFont(font5)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.c_state = QLabel(self.battery_box)
        self.c_state.setObjectName(u"c_state")
        font9 = QFont()
        font9.setFamilies([u"Consolas"])
        font9.setPointSize(11)
        self.c_state.setFont(font9)

        self.horizontalLayout_6.addWidget(self.c_state)

        self.container_battery_percent = QLabel(self.battery_box)
        self.container_battery_percent.setObjectName(u"container_battery_percent")
        font10 = QFont()
        font10.setFamilies([u"Consolas"])
        font10.setPointSize(15)
        self.container_battery_percent.setFont(font10)
        self.container_battery_percent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.container_battery_percent)

        self.widget = QWidget(self.battery_box)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(81, 51))
        self.widget.setMaximumSize(QSize(81, 51))
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.c_battery_visual = QProgressBar(self.widget)
        self.c_battery_visual.setObjectName(u"c_battery_visual")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.c_battery_visual.sizePolicy().hasHeightForWidth())
        self.c_battery_visual.setSizePolicy(sizePolicy3)
        self.c_battery_visual.setStyleSheet(u"QProgressBar {\n"
"	border-radius: 5px;\n"
"	background-color: #555770;\n"
"	border: 2px solid white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 5px;\n"
"	background-color: #39d98a;\n"
"	border: 2px solid #555770;\n"
"}")
        self.c_battery_visual.setMaximum(100)
        self.c_battery_visual.setValue(0)
        self.c_battery_visual.setTextVisible(False)
        self.c_battery_visual.setInvertedAppearance(False)

        self.horizontalLayout_7.addWidget(self.c_battery_visual)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        sizePolicy1.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy1)
        self.widget1.setMinimumSize(QSize(5, 13))
        self.widget1.setMaximumSize(QSize(5, 13))
        self.widget1.setStyleSheet(u"border-radius: 2px;\n"
"background-color: white;")

        self.horizontalLayout_7.addWidget(self.widget1)


        self.horizontalLayout_6.addWidget(self.widget)


        self.header_box.addWidget(self.battery_box)


        self.verticalLayout_6.addWidget(self.header_box_2)

        self.pkg_count_box = QGroupBox(self.container_box)
        self.pkg_count_box.setObjectName(u"pkg_count_box")
        self.pkg_count_box.setMinimumSize(QSize(214, 40))
        self.pkg_count_box.setMaximumSize(QSize(400, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.pkg_count_box)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pkg_count_label_3 = QLabel(self.pkg_count_box)
        self.pkg_count_label_3.setObjectName(u"pkg_count_label_3")
        self.pkg_count_label_3.setFont(font5)
        self.pkg_count_label_3.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout_5.addWidget(self.pkg_count_label_3)

        self.c_healthy_pkg_count = QLabel(self.pkg_count_box)
        self.c_healthy_pkg_count.setObjectName(u"c_healthy_pkg_count")
        self.c_healthy_pkg_count.setFont(font6)
        self.c_healthy_pkg_count.setStyleSheet(u"color: #39d98a;")

        self.horizontalLayout_5.addWidget(self.c_healthy_pkg_count)

        self.pkg_count_label_2 = QLabel(self.pkg_count_box)
        self.pkg_count_label_2.setObjectName(u"pkg_count_label_2")
        self.pkg_count_label_2.setFont(font5)
        self.pkg_count_label_2.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout_5.addWidget(self.pkg_count_label_2)

        self.c_corrupted_pkg_count = QLabel(self.pkg_count_box)
        self.c_corrupted_pkg_count.setObjectName(u"c_corrupted_pkg_count")
        self.c_corrupted_pkg_count.setFont(font6)
        self.c_corrupted_pkg_count.setStyleSheet(u"color: #ff5c5c;")

        self.horizontalLayout_5.addWidget(self.c_corrupted_pkg_count)


        self.verticalLayout_6.addWidget(self.pkg_count_box)

        self.chart_box = QGroupBox(self.container_box)
        self.chart_box.setObjectName(u"chart_box")
        self.chart_box.setMinimumSize(QSize(781, 201))
        self.chart_box.setMaximumSize(QSize(16777215, 201))
        self.chart_box.setStyleSheet(u"border-radius: 3px;")
        self.gridLayout_2 = QGridLayout(self.chart_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.c_voltage_chart = PlotWidget(self.chart_box)
        self.c_voltage_chart.setObjectName(u"c_voltage_chart")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.c_voltage_chart.sizePolicy().hasHeightForWidth())
        self.c_voltage_chart.setSizePolicy(sizePolicy4)
        self.c_voltage_chart.setMinimumSize(QSize(261, 0))
        self.c_voltage_chart.setMaximumSize(QSize(343, 191))
        self.c_voltage_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_2.addWidget(self.c_voltage_chart, 2, 3, 1, 1)

        self.c_temp_chart = PlotWidget(self.chart_box)
        self.c_temp_chart.setObjectName(u"c_temp_chart")
        sizePolicy4.setHeightForWidth(self.c_temp_chart.sizePolicy().hasHeightForWidth())
        self.c_temp_chart.setSizePolicy(sizePolicy4)
        self.c_temp_chart.setMinimumSize(QSize(261, 0))
        self.c_temp_chart.setMaximumSize(QSize(343, 191))
        self.c_temp_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_2.addWidget(self.c_temp_chart, 2, 0, 1, 1)

        self.c_gps_altitude_chart = PlotWidget(self.chart_box)
        self.c_gps_altitude_chart.setObjectName(u"c_gps_altitude_chart")
        sizePolicy4.setHeightForWidth(self.c_gps_altitude_chart.sizePolicy().hasHeightForWidth())
        self.c_gps_altitude_chart.setSizePolicy(sizePolicy4)
        self.c_gps_altitude_chart.setMinimumSize(QSize(261, 0))
        self.c_gps_altitude_chart.setMaximumSize(QSize(343, 191))
        self.c_gps_altitude_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_2.addWidget(self.c_gps_altitude_chart, 2, 2, 1, 1)

        self.c_altitude_chart = PlotWidget(self.chart_box)
        self.c_altitude_chart.setObjectName(u"c_altitude_chart")
        sizePolicy4.setHeightForWidth(self.c_altitude_chart.sizePolicy().hasHeightForWidth())
        self.c_altitude_chart.setSizePolicy(sizePolicy4)
        self.c_altitude_chart.setMinimumSize(QSize(261, 0))
        self.c_altitude_chart.setMaximumSize(QSize(343, 191))
        self.c_altitude_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_2.addWidget(self.c_altitude_chart, 2, 1, 1, 1)

        self.widget_8 = QWidget(self.chart_box)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.c_temp_label = QLabel(self.widget_8)
        self.c_temp_label.setObjectName(u"c_temp_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.c_temp_label.sizePolicy().hasHeightForWidth())
        self.c_temp_label.setSizePolicy(sizePolicy5)
        self.c_temp_label.setMinimumSize(QSize(0, 0))
        self.c_temp_label.setFont(font5)
        self.c_temp_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.c_temp_label)

        self.c_temp_value = QLabel(self.widget_8)
        self.c_temp_value.setObjectName(u"c_temp_value")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.c_temp_value.sizePolicy().hasHeightForWidth())
        self.c_temp_value.setSizePolicy(sizePolicy6)
        self.c_temp_value.setMinimumSize(QSize(0, 0))
        self.c_temp_value.setFont(font6)
        self.c_temp_value.setStyleSheet(u"color: cyan;")
        self.c_temp_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.c_temp_value)


        self.gridLayout_2.addWidget(self.widget_8, 1, 0, 1, 1)

        self.widget_9 = QWidget(self.chart_box)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.c_altitude_label = QLabel(self.widget_9)
        self.c_altitude_label.setObjectName(u"c_altitude_label")
        sizePolicy5.setHeightForWidth(self.c_altitude_label.sizePolicy().hasHeightForWidth())
        self.c_altitude_label.setSizePolicy(sizePolicy5)
        self.c_altitude_label.setMinimumSize(QSize(0, 0))
        self.c_altitude_label.setFont(font5)
        self.c_altitude_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.c_altitude_label)

        self.c_altitude_value = QLabel(self.widget_9)
        self.c_altitude_value.setObjectName(u"c_altitude_value")
        sizePolicy6.setHeightForWidth(self.c_altitude_value.sizePolicy().hasHeightForWidth())
        self.c_altitude_value.setSizePolicy(sizePolicy6)
        self.c_altitude_value.setMinimumSize(QSize(0, 0))
        self.c_altitude_value.setFont(font6)
        self.c_altitude_value.setStyleSheet(u"color: cyan;")
        self.c_altitude_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.c_altitude_value)


        self.gridLayout_2.addWidget(self.widget_9, 1, 1, 1, 1)

        self.widget_10 = QWidget(self.chart_box)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.c_gps_altitude_label = QLabel(self.widget_10)
        self.c_gps_altitude_label.setObjectName(u"c_gps_altitude_label")
        sizePolicy5.setHeightForWidth(self.c_gps_altitude_label.sizePolicy().hasHeightForWidth())
        self.c_gps_altitude_label.setSizePolicy(sizePolicy5)
        self.c_gps_altitude_label.setMinimumSize(QSize(0, 0))
        self.c_gps_altitude_label.setFont(font5)
        self.c_gps_altitude_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.c_gps_altitude_label)

        self.c_gps_altitude_value = QLabel(self.widget_10)
        self.c_gps_altitude_value.setObjectName(u"c_gps_altitude_value")
        sizePolicy6.setHeightForWidth(self.c_gps_altitude_value.sizePolicy().hasHeightForWidth())
        self.c_gps_altitude_value.setSizePolicy(sizePolicy6)
        self.c_gps_altitude_value.setMinimumSize(QSize(0, 0))
        self.c_gps_altitude_value.setFont(font6)
        self.c_gps_altitude_value.setStyleSheet(u"color: cyan;")
        self.c_gps_altitude_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.c_gps_altitude_value)


        self.gridLayout_2.addWidget(self.widget_10, 1, 2, 1, 1)

        self.widget_11 = QWidget(self.chart_box)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.c_voltage_label = QLabel(self.widget_11)
        self.c_voltage_label.setObjectName(u"c_voltage_label")
        sizePolicy5.setHeightForWidth(self.c_voltage_label.sizePolicy().hasHeightForWidth())
        self.c_voltage_label.setSizePolicy(sizePolicy5)
        self.c_voltage_label.setMinimumSize(QSize(0, 0))
        self.c_voltage_label.setFont(font5)
        self.c_voltage_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.c_voltage_label)

        self.c_voltage_value = QLabel(self.widget_11)
        self.c_voltage_value.setObjectName(u"c_voltage_value")
        sizePolicy6.setHeightForWidth(self.c_voltage_value.sizePolicy().hasHeightForWidth())
        self.c_voltage_value.setSizePolicy(sizePolicy6)
        self.c_voltage_value.setMinimumSize(QSize(0, 0))
        self.c_voltage_value.setFont(font6)
        self.c_voltage_value.setStyleSheet(u"color: cyan;")
        self.c_voltage_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.c_voltage_value)


        self.gridLayout_2.addWidget(self.widget_11, 1, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.chart_box)


        self.gridLayout_6.addWidget(self.container_box, 1, 0, 1, 2)

        self.telemetry_box = QWidget(self.centralwidget)
        self.telemetry_box.setObjectName(u"telemetry_box")
        self.telemetry_box.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.telemetry_box.sizePolicy().hasHeightForWidth())
        self.telemetry_box.setSizePolicy(sizePolicy2)
        self.telemetry_box.setMinimumSize(QSize(799, 305))
        self.telemetry_box.setStyleSheet(u"color: white;\n"
"background-color: rgb(40, 41, 61);\n"
"border-radius: 20px;")
        self.verticalLayout = QVBoxLayout(self.telemetry_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_box_4 = QGroupBox(self.telemetry_box)
        self.header_box_4.setObjectName(u"header_box_4")
        self.header_box_11 = QHBoxLayout(self.header_box_4)
        self.header_box_11.setObjectName(u"header_box_11")
        self.title_box_6 = QGroupBox(self.header_box_4)
        self.title_box_6.setObjectName(u"title_box_6")
        self.horizontalLayout_19 = QHBoxLayout(self.title_box_6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.line_7 = QFrame(self.title_box_6)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: rgb(62, 123, 250);\n"
"border-radius: 100px;")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_7)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)

        self.title_6 = QLabel(self.title_box_6)
        self.title_6.setObjectName(u"title_6")
        self.title_6.setMaximumSize(QSize(16777215, 25))
        self.title_6.setFont(font8)
        self.title_6.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.title_6)


        self.header_box_11.addWidget(self.title_box_6)

        self.status_box = QGroupBox(self.header_box_4)
        self.status_box.setObjectName(u"status_box")
        self.status_box.setMinimumSize(QSize(214, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.status_box)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.total_pkg_title = QLabel(self.status_box)
        self.total_pkg_title.setObjectName(u"total_pkg_title")
        self.total_pkg_title.setFont(font5)
        self.total_pkg_title.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout_10.addWidget(self.total_pkg_title)

        self.total_pkg_value = QLabel(self.status_box)
        self.total_pkg_value.setObjectName(u"total_pkg_value")
        self.total_pkg_value.setMinimumSize(QSize(45, 0))
        self.total_pkg_value.setFont(font6)

        self.horizontalLayout_10.addWidget(self.total_pkg_value)

        self.total_corrupted_pkg_title = QLabel(self.status_box)
        self.total_corrupted_pkg_title.setObjectName(u"total_corrupted_pkg_title")
        self.total_corrupted_pkg_title.setFont(font5)
        self.total_corrupted_pkg_title.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout_10.addWidget(self.total_corrupted_pkg_title)

        self.total_corrupted_pkg_value = QLabel(self.status_box)
        self.total_corrupted_pkg_value.setObjectName(u"total_corrupted_pkg_value")
        self.total_corrupted_pkg_value.setMinimumSize(QSize(45, 0))
        self.total_corrupted_pkg_value.setFont(font6)
        self.total_corrupted_pkg_value.setStyleSheet(u"color: #ff5c5c;")

        self.horizontalLayout_10.addWidget(self.total_corrupted_pkg_value)

        self.last_cmd_title = QLabel(self.status_box)
        self.last_cmd_title.setObjectName(u"last_cmd_title")
        self.last_cmd_title.setFont(font5)
        self.last_cmd_title.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout_10.addWidget(self.last_cmd_title)

        self.last_cmd_value = QLabel(self.status_box)
        self.last_cmd_value.setObjectName(u"last_cmd_value")
        self.last_cmd_value.setFont(font6)

        self.horizontalLayout_10.addWidget(self.last_cmd_value)


        self.header_box_11.addWidget(self.status_box)


        self.verticalLayout.addWidget(self.header_box_4)

        self.telemetry_group_2 = QWidget(self.telemetry_box)
        self.telemetry_group_2.setObjectName(u"telemetry_group_2")
        self.telemetry_group_2.setEnabled(True)
        font11 = QFont()
        font11.setFamilies([u"Inter"])
        font11.setPointSize(10)
        font11.setBold(False)
        font11.setStrikeOut(False)
        font11.setKerning(True)
        self.telemetry_group_2.setFont(font11)
        self.telemetry_group_2.setStyleSheet(u"background-color: #28293d;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.telemetry_group_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget2 = QWidget(self.telemetry_group_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setMaximumSize(QSize(16777215, 33))
        self.telemetry_control_group = QHBoxLayout(self.widget2)
        self.telemetry_control_group.setObjectName(u"telemetry_control_group")
        self.telemetry_control_group.setContentsMargins(1, 1, 1, 1)
        self.cmd_select_box = QComboBox(self.widget2)
        self.cmd_select_box.addItem("")
        self.cmd_select_box.addItem("")
        self.cmd_select_box.addItem("")
        self.cmd_select_box.addItem("")
        self.cmd_select_box.addItem("")
        self.cmd_select_box.addItem("")
        self.cmd_select_box.addItem("")
        self.cmd_select_box.setObjectName(u"cmd_select_box")
        sizePolicy1.setHeightForWidth(self.cmd_select_box.sizePolicy().hasHeightForWidth())
        self.cmd_select_box.setSizePolicy(sizePolicy1)
        font12 = QFont()
        font12.setFamilies([u"Inter"])
        font12.setPointSize(12)
        font12.setBold(False)
        self.cmd_select_box.setFont(font12)
        self.cmd_select_box.setMouseTracking(False)
        self.cmd_select_box.setAutoFillBackground(False)
        self.cmd_select_box.setStyleSheet(u"padding: 5px;\n"
"background-color: rgba(231, 231, 231, 20);\n"
"border-radius: 5px;")
        self.cmd_select_box.setEditable(False)
        self.cmd_select_box.setDuplicatesEnabled(False)
        self.cmd_select_box.setFrame(True)

        self.telemetry_control_group.addWidget(self.cmd_select_box)

        self.splitter_2 = QSplitter(self.widget2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label_7 = QLabel(self.splitter_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16))
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: #8f90a6;")
        self.splitter_2.addWidget(self.label_7)

        self.telemetry_control_group.addWidget(self.splitter_2)

        self.cmd_preview = QLineEdit(self.widget2)
        self.cmd_preview.setObjectName(u"cmd_preview")
        self.cmd_preview.setEnabled(True)
        self.cmd_preview.setFont(font6)
        self.cmd_preview.setStyleSheet(u"padding: 5px;\n"
"background-color: rgba(231, 231, 231, 20);\n"
"border-radius: 5px;\n"
"color: rgb(200, 200, 200);")
        self.cmd_preview.setFrame(True)

        self.telemetry_control_group.addWidget(self.cmd_preview)

        self.cmdSendButton_2 = QPushButton(self.widget2)
        self.cmdSendButton_2.setObjectName(u"cmdSendButton_2")
        font13 = QFont()
        font13.setPointSize(12)
        font13.setBold(False)
        font13.setKerning(True)
        self.cmdSendButton_2.setFont(font13)
        self.cmdSendButton_2.setStyleSheet(u"QPushButton {\n"
"	padding: 5px 10px;\n"
"	background-color: #06c270;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"	background-color: #39d98a;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #05a660;\n"
"}")
        self.cmdSendButton_2.setCheckable(False)
        self.cmdSendButton_2.setAutoDefault(False)
        self.cmdSendButton_2.setFlat(False)

        self.telemetry_control_group.addWidget(self.cmdSendButton_2)


        self.verticalLayout_3.addWidget(self.widget2)

        self.autoscroll_check = QCheckBox(self.telemetry_group_2)
        self.autoscroll_check.setObjectName(u"autoscroll_check")
        self.autoscroll_check.setFont(font)
        self.autoscroll_check.setChecked(True)

        self.verticalLayout_3.addWidget(self.autoscroll_check)

        self.telemetry_log = QTextBrowser(self.telemetry_group_2)
        self.telemetry_log.setObjectName(u"telemetry_log")
        font14 = QFont()
        font14.setFamilies([u"Consolas"])
        font14.setPointSize(10)
        self.telemetry_log.setFont(font14)
        self.telemetry_log.setStyleSheet(u"background-color: rgba(0, 0, 0, 20%);\n"
"border: 2px solid #444657;\n"
"padding: 3px;\n"
"color: white;")

        self.verticalLayout_3.addWidget(self.telemetry_log)


        self.verticalLayout.addWidget(self.telemetry_group_2)


        self.gridLayout_6.addWidget(self.telemetry_box, 1, 2, 2, 1)

        self.payload_box = QWidget(self.centralwidget)
        self.payload_box.setObjectName(u"payload_box")
        sizePolicy2.setHeightForWidth(self.payload_box.sizePolicy().hasHeightForWidth())
        self.payload_box.setSizePolicy(sizePolicy2)
        self.payload_box.setMinimumSize(QSize(1097, 0))
        self.payload_box.setMaximumSize(QSize(16777215, 16777215))
        self.payload_box.setStyleSheet(u"color: white;\n"
"background-color: rgb(40, 41, 61);\n"
"border-radius: 20px;")
        self.verticalLayout_5 = QVBoxLayout(self.payload_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.header_box_5 = QGroupBox(self.payload_box)
        self.header_box_5.setObjectName(u"header_box_5")
        self.header_box_6 = QHBoxLayout(self.header_box_5)
        self.header_box_6.setObjectName(u"header_box_6")
        self.title_box_5 = QGroupBox(self.header_box_5)
        self.title_box_5.setObjectName(u"title_box_5")
        self.horizontalLayout_20 = QHBoxLayout(self.title_box_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.line_6 = QFrame(self.title_box_5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMaximumSize(QSize(16777215, 25))
        self.line_6.setStyleSheet(u"background-color: rgb(62, 123, 250);\n"
"border-radius: 100px;")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_6)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_8)

        self.title_5 = QLabel(self.title_box_5)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setMaximumSize(QSize(16777215, 25))
        self.title_5.setFont(font8)
        self.title_5.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.title_5)


        self.header_box_6.addWidget(self.title_box_5)

        self.battery_box_3 = QGroupBox(self.header_box_5)
        self.battery_box_3.setObjectName(u"battery_box_3")
        self.battery_box_3.setFlat(False)
        self.horizontalLayout_15 = QHBoxLayout(self.battery_box_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.battery_box_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(61, 16777215))
        self.label_17.setFont(font5)

        self.horizontalLayout_15.addWidget(self.label_17)

        self.p_state = QLabel(self.battery_box_3)
        self.p_state.setObjectName(u"p_state")
        self.p_state.setFont(font9)

        self.horizontalLayout_15.addWidget(self.p_state)

        self.widget_6 = QWidget(self.battery_box_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(17, 5))
        self.widget_6.setStyleSheet(u"background-color: red;")

        self.horizontalLayout_15.addWidget(self.widget_6)

        self.label_13 = QLabel(self.battery_box_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(50, 16777215))
        self.label_13.setFont(font4)

        self.horizontalLayout_15.addWidget(self.label_13)

        self.widget_7 = QWidget(self.battery_box_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(17, 5))
        self.widget_7.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_15.addWidget(self.widget_7)

        self.label_12 = QLabel(self.battery_box_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(50, 16777215))
        self.label_12.setFont(font4)

        self.horizontalLayout_15.addWidget(self.label_12)

        self.widget_3 = QWidget(self.battery_box_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(17, 5))
        self.widget_3.setStyleSheet(u"background-color: cyan;")

        self.horizontalLayout_15.addWidget(self.widget_3)

        self.label_9 = QLabel(self.battery_box_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))
        self.label_9.setFont(font4)

        self.horizontalLayout_15.addWidget(self.label_9)

        self.payload_battery_percent = QLabel(self.battery_box_3)
        self.payload_battery_percent.setObjectName(u"payload_battery_percent")
        self.payload_battery_percent.setFont(font10)
        self.payload_battery_percent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.payload_battery_percent)

        self.widget_4 = QWidget(self.battery_box_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(81, 51))
        self.widget_4.setMaximumSize(QSize(81, 51))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.p_battery_visual = QProgressBar(self.widget_4)
        self.p_battery_visual.setObjectName(u"p_battery_visual")
        sizePolicy3.setHeightForWidth(self.p_battery_visual.sizePolicy().hasHeightForWidth())
        self.p_battery_visual.setSizePolicy(sizePolicy3)
        self.p_battery_visual.setStyleSheet(u"QProgressBar {\n"
"	border-radius: 5px;\n"
"	background-color: #555770;\n"
"	border: 2px solid white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 5px;\n"
"	background-color: #39d98a;\n"
"	border: 2px solid #555770;\n"
"}")
        self.p_battery_visual.setMaximum(100)
        self.p_battery_visual.setValue(0)
        self.p_battery_visual.setTextVisible(False)
        self.p_battery_visual.setInvertedAppearance(False)

        self.horizontalLayout_16.addWidget(self.p_battery_visual)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMinimumSize(QSize(5, 13))
        self.widget_5.setMaximumSize(QSize(5, 13))
        self.widget_5.setStyleSheet(u"border-radius: 2px;\n"
"background-color: white;")

        self.horizontalLayout_16.addWidget(self.widget_5)


        self.horizontalLayout_15.addWidget(self.widget_4)


        self.header_box_6.addWidget(self.battery_box_3)


        self.verticalLayout_5.addWidget(self.header_box_5)

        self.pkg_count_box_2 = QGroupBox(self.payload_box)
        self.pkg_count_box_2.setObjectName(u"pkg_count_box_2")
        self.pkg_count_box_2.setMinimumSize(QSize(214, 40))
        self.pkg_count_box_2.setMaximumSize(QSize(400, 31))
        self.horizontalLayout_17 = QHBoxLayout(self.pkg_count_box_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pkg_count_label_7 = QLabel(self.pkg_count_box_2)
        self.pkg_count_label_7.setObjectName(u"pkg_count_label_7")
        self.pkg_count_label_7.setFont(font5)
        self.pkg_count_label_7.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout_17.addWidget(self.pkg_count_label_7)

        self.p_healthy_pkg_count = QLabel(self.pkg_count_box_2)
        self.p_healthy_pkg_count.setObjectName(u"p_healthy_pkg_count")
        self.p_healthy_pkg_count.setFont(font6)
        self.p_healthy_pkg_count.setStyleSheet(u"color: #39d98a;")

        self.horizontalLayout_17.addWidget(self.p_healthy_pkg_count)

        self.pkg_count_label_8 = QLabel(self.pkg_count_box_2)
        self.pkg_count_label_8.setObjectName(u"pkg_count_label_8")
        self.pkg_count_label_8.setFont(font5)
        self.pkg_count_label_8.setStyleSheet(u"color: #8f90a6;")

        self.horizontalLayout_17.addWidget(self.pkg_count_label_8)

        self.p_corrupted_pkg_count = QLabel(self.pkg_count_box_2)
        self.p_corrupted_pkg_count.setObjectName(u"p_corrupted_pkg_count")
        self.p_corrupted_pkg_count.setFont(font6)
        self.p_corrupted_pkg_count.setStyleSheet(u"color: #ff5c5c;")

        self.horizontalLayout_17.addWidget(self.p_corrupted_pkg_count)


        self.verticalLayout_5.addWidget(self.pkg_count_box_2)

        self.chart_box_3 = QGroupBox(self.payload_box)
        self.chart_box_3.setObjectName(u"chart_box_3")
        self.chart_box_3.setMinimumSize(QSize(781, 175))
        self.chart_box_3.setMaximumSize(QSize(16777215, 193))
        self.chart_box_3.setStyleSheet(u"border-radius: 3px;")
        self.gridLayout_3 = QGridLayout(self.chart_box_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.p_gyro_chart = PlotWidget(self.chart_box_3)
        self.p_gyro_chart.setObjectName(u"p_gyro_chart")
        sizePolicy4.setHeightForWidth(self.p_gyro_chart.sizePolicy().hasHeightForWidth())
        self.p_gyro_chart.setSizePolicy(sizePolicy4)
        self.p_gyro_chart.setMinimumSize(QSize(343, 0))
        self.p_gyro_chart.setMaximumSize(QSize(343, 191))
        self.p_gyro_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_3.addWidget(self.p_gyro_chart, 1, 1, 1, 1)

        self.p_accel_chart = PlotWidget(self.chart_box_3)
        self.p_accel_chart.setObjectName(u"p_accel_chart")
        sizePolicy4.setHeightForWidth(self.p_accel_chart.sizePolicy().hasHeightForWidth())
        self.p_accel_chart.setSizePolicy(sizePolicy4)
        self.p_accel_chart.setMinimumSize(QSize(343, 0))
        self.p_accel_chart.setMaximumSize(QSize(343, 191))
        self.p_accel_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_3.addWidget(self.p_accel_chart, 1, 2, 1, 1)

        self.p_temp_chart = PlotWidget(self.chart_box_3)
        self.p_temp_chart.setObjectName(u"p_temp_chart")
        sizePolicy4.setHeightForWidth(self.p_temp_chart.sizePolicy().hasHeightForWidth())
        self.p_temp_chart.setSizePolicy(sizePolicy4)
        self.p_temp_chart.setMinimumSize(QSize(343, 0))
        self.p_temp_chart.setMaximumSize(QSize(343, 191))
        self.p_temp_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_3.addWidget(self.p_temp_chart, 1, 0, 1, 1)

        self.widget_12 = QWidget(self.chart_box_3)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.p_temp_label = QLabel(self.widget_12)
        self.p_temp_label.setObjectName(u"p_temp_label")
        sizePolicy5.setHeightForWidth(self.p_temp_label.sizePolicy().hasHeightForWidth())
        self.p_temp_label.setSizePolicy(sizePolicy5)
        self.p_temp_label.setMinimumSize(QSize(0, 0))
        self.p_temp_label.setFont(font5)
        self.p_temp_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.p_temp_label)

        self.p_temp_value = QLabel(self.widget_12)
        self.p_temp_value.setObjectName(u"p_temp_value")
        sizePolicy6.setHeightForWidth(self.p_temp_value.sizePolicy().hasHeightForWidth())
        self.p_temp_value.setSizePolicy(sizePolicy6)
        self.p_temp_value.setMinimumSize(QSize(0, 0))
        self.p_temp_value.setFont(font6)
        self.p_temp_value.setStyleSheet(u"color: cyan;")
        self.p_temp_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.p_temp_value)


        self.gridLayout_3.addWidget(self.widget_12, 0, 0, 1, 1)

        self.widget_13 = QWidget(self.chart_box_3)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.p_gyro_label = QLabel(self.widget_13)
        self.p_gyro_label.setObjectName(u"p_gyro_label")
        sizePolicy5.setHeightForWidth(self.p_gyro_label.sizePolicy().hasHeightForWidth())
        self.p_gyro_label.setSizePolicy(sizePolicy5)
        self.p_gyro_label.setMinimumSize(QSize(0, 0))
        self.p_gyro_label.setFont(font5)
        self.p_gyro_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.p_gyro_label)

        self.p_gyro_value = QLabel(self.widget_13)
        self.p_gyro_value.setObjectName(u"p_gyro_value")
        sizePolicy6.setHeightForWidth(self.p_gyro_value.sizePolicy().hasHeightForWidth())
        self.p_gyro_value.setSizePolicy(sizePolicy6)
        self.p_gyro_value.setMinimumSize(QSize(0, 0))
        self.p_gyro_value.setFont(font6)
        self.p_gyro_value.setStyleSheet(u"color: cyan;")
        self.p_gyro_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.p_gyro_value)


        self.gridLayout_3.addWidget(self.widget_13, 0, 1, 1, 1)

        self.widget_14 = QWidget(self.chart_box_3)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.p_accel_label = QLabel(self.widget_14)
        self.p_accel_label.setObjectName(u"p_accel_label")
        sizePolicy5.setHeightForWidth(self.p_accel_label.sizePolicy().hasHeightForWidth())
        self.p_accel_label.setSizePolicy(sizePolicy5)
        self.p_accel_label.setMinimumSize(QSize(0, 0))
        self.p_accel_label.setFont(font5)
        self.p_accel_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.p_accel_label)

        self.p_accel_value = QLabel(self.widget_14)
        self.p_accel_value.setObjectName(u"p_accel_value")
        sizePolicy6.setHeightForWidth(self.p_accel_value.sizePolicy().hasHeightForWidth())
        self.p_accel_value.setSizePolicy(sizePolicy6)
        self.p_accel_value.setMinimumSize(QSize(0, 0))
        self.p_accel_value.setFont(font6)
        self.p_accel_value.setStyleSheet(u"color: cyan;")
        self.p_accel_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.p_accel_value)


        self.gridLayout_3.addWidget(self.widget_14, 0, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.chart_box_3)

        self.chart_box_4 = QGroupBox(self.payload_box)
        self.chart_box_4.setObjectName(u"chart_box_4")
        self.chart_box_4.setMinimumSize(QSize(781, 175))
        self.chart_box_4.setMaximumSize(QSize(16777215, 201))
        self.chart_box_4.setStyleSheet(u"border-radius: 3px;")
        self.gridLayout_5 = QGridLayout(self.chart_box_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.p_altitude_chart = PlotWidget(self.chart_box_4)
        self.p_altitude_chart.setObjectName(u"p_altitude_chart")
        sizePolicy4.setHeightForWidth(self.p_altitude_chart.sizePolicy().hasHeightForWidth())
        self.p_altitude_chart.setSizePolicy(sizePolicy4)
        self.p_altitude_chart.setMinimumSize(QSize(343, 0))
        self.p_altitude_chart.setMaximumSize(QSize(343, 191))
        self.p_altitude_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_5.addWidget(self.p_altitude_chart, 1, 5, 1, 1)

        self.p_voltage_chart = PlotWidget(self.chart_box_4)
        self.p_voltage_chart.setObjectName(u"p_voltage_chart")
        sizePolicy4.setHeightForWidth(self.p_voltage_chart.sizePolicy().hasHeightForWidth())
        self.p_voltage_chart.setSizePolicy(sizePolicy4)
        self.p_voltage_chart.setMinimumSize(QSize(343, 0))
        self.p_voltage_chart.setMaximumSize(QSize(343, 191))
        self.p_voltage_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_5.addWidget(self.p_voltage_chart, 1, 3, 1, 1)

        self.p_mag_chart = PlotWidget(self.chart_box_4)
        self.p_mag_chart.setObjectName(u"p_mag_chart")
        sizePolicy4.setHeightForWidth(self.p_mag_chart.sizePolicy().hasHeightForWidth())
        self.p_mag_chart.setSizePolicy(sizePolicy4)
        self.p_mag_chart.setMinimumSize(QSize(343, 0))
        self.p_mag_chart.setMaximumSize(QSize(343, 191))
        self.p_mag_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_5.addWidget(self.p_mag_chart, 1, 0, 1, 1)

        self.widget_16 = QWidget(self.chart_box_4)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.p_ptr_err_label = QLabel(self.widget_16)
        self.p_ptr_err_label.setObjectName(u"p_ptr_err_label")
        sizePolicy5.setHeightForWidth(self.p_ptr_err_label.sizePolicy().hasHeightForWidth())
        self.p_ptr_err_label.setSizePolicy(sizePolicy5)
        self.p_ptr_err_label.setMinimumSize(QSize(0, 0))
        self.p_ptr_err_label.setFont(font5)
        self.p_ptr_err_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.p_ptr_err_label)

        self.p_ptr_err_value = QLabel(self.widget_16)
        self.p_ptr_err_value.setObjectName(u"p_ptr_err_value")
        sizePolicy6.setHeightForWidth(self.p_ptr_err_value.sizePolicy().hasHeightForWidth())
        self.p_ptr_err_value.setSizePolicy(sizePolicy6)
        self.p_ptr_err_value.setMinimumSize(QSize(0, 0))
        self.p_ptr_err_value.setFont(font6)
        self.p_ptr_err_value.setStyleSheet(u"color: cyan;")
        self.p_ptr_err_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.p_ptr_err_value)


        self.gridLayout_5.addWidget(self.widget_16, 0, 1, 1, 1)

        self.widget_17 = QWidget(self.chart_box_4)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.p_voltage_label = QLabel(self.widget_17)
        self.p_voltage_label.setObjectName(u"p_voltage_label")
        sizePolicy5.setHeightForWidth(self.p_voltage_label.sizePolicy().hasHeightForWidth())
        self.p_voltage_label.setSizePolicy(sizePolicy5)
        self.p_voltage_label.setMinimumSize(QSize(0, 0))
        self.p_voltage_label.setFont(font5)
        self.p_voltage_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.p_voltage_label)

        self.p_voltage_value = QLabel(self.widget_17)
        self.p_voltage_value.setObjectName(u"p_voltage_value")
        sizePolicy6.setHeightForWidth(self.p_voltage_value.sizePolicy().hasHeightForWidth())
        self.p_voltage_value.setSizePolicy(sizePolicy6)
        self.p_voltage_value.setMinimumSize(QSize(0, 0))
        self.p_voltage_value.setFont(font6)
        self.p_voltage_value.setStyleSheet(u"color: cyan;")
        self.p_voltage_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.p_voltage_value)


        self.gridLayout_5.addWidget(self.widget_17, 0, 3, 1, 1)

        self.p_ptr_err_chart = PlotWidget(self.chart_box_4)
        self.p_ptr_err_chart.setObjectName(u"p_ptr_err_chart")
        sizePolicy4.setHeightForWidth(self.p_ptr_err_chart.sizePolicy().hasHeightForWidth())
        self.p_ptr_err_chart.setSizePolicy(sizePolicy4)
        self.p_ptr_err_chart.setMinimumSize(QSize(343, 0))
        self.p_ptr_err_chart.setMaximumSize(QSize(343, 191))
        self.p_ptr_err_chart.setStyleSheet(u"background-color: black;")

        self.gridLayout_5.addWidget(self.p_ptr_err_chart, 1, 1, 1, 1)

        self.widget_15 = QWidget(self.chart_box_4)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.p_mag_label = QLabel(self.widget_15)
        self.p_mag_label.setObjectName(u"p_mag_label")
        sizePolicy5.setHeightForWidth(self.p_mag_label.sizePolicy().hasHeightForWidth())
        self.p_mag_label.setSizePolicy(sizePolicy5)
        self.p_mag_label.setMinimumSize(QSize(0, 0))
        self.p_mag_label.setFont(font5)
        self.p_mag_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.p_mag_label)

        self.p_mag_value = QLabel(self.widget_15)
        self.p_mag_value.setObjectName(u"p_mag_value")
        sizePolicy6.setHeightForWidth(self.p_mag_value.sizePolicy().hasHeightForWidth())
        self.p_mag_value.setSizePolicy(sizePolicy6)
        self.p_mag_value.setMinimumSize(QSize(0, 0))
        self.p_mag_value.setFont(font6)
        self.p_mag_value.setStyleSheet(u"color: cyan;")
        self.p_mag_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.p_mag_value)


        self.gridLayout_5.addWidget(self.widget_15, 0, 0, 1, 1)

        self.widget_18 = QWidget(self.chart_box_4)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.p_altitude_label = QLabel(self.widget_18)
        self.p_altitude_label.setObjectName(u"p_altitude_label")
        sizePolicy5.setHeightForWidth(self.p_altitude_label.sizePolicy().hasHeightForWidth())
        self.p_altitude_label.setSizePolicy(sizePolicy5)
        self.p_altitude_label.setMinimumSize(QSize(0, 0))
        self.p_altitude_label.setFont(font5)
        self.p_altitude_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.p_altitude_label)

        self.p_altitude_value = QLabel(self.widget_18)
        self.p_altitude_value.setObjectName(u"p_altitude_value")
        sizePolicy6.setHeightForWidth(self.p_altitude_value.sizePolicy().hasHeightForWidth())
        self.p_altitude_value.setSizePolicy(sizePolicy6)
        self.p_altitude_value.setMinimumSize(QSize(0, 0))
        self.p_altitude_value.setFont(font6)
        self.p_altitude_value.setStyleSheet(u"color: cyan;")
        self.p_altitude_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.p_altitude_value)


        self.gridLayout_5.addWidget(self.widget_18, 0, 5, 1, 1)


        self.verticalLayout_5.addWidget(self.chart_box_4)


        self.gridLayout_6.addWidget(self.payload_box, 2, 0, 2, 2)

        self.mission_box = QWidget(self.centralwidget)
        self.mission_box.setObjectName(u"mission_box")
        self.mission_box.setMaximumSize(QSize(16777215, 159))
        self.mission_box.setStyleSheet(u"background-color: #28293d;\n"
"color: white;\n"
"border-radius: 20px;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.mission_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.elapsed_time = QLabel(self.mission_box)
        self.elapsed_time.setObjectName(u"elapsed_time")
        font15 = QFont()
        font15.setPointSize(16)
        self.elapsed_time.setFont(font15)
        self.elapsed_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.elapsed_time)

        self.groupBox_3 = QGroupBox(self.mission_box)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(192, 45))
        self.groupBox_3.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.start_button = QPushButton(self.groupBox_3)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMaximumSize(QSize(80, 16777215))
        self.start_button.setFont(font4)
        self.start_button.setLayoutDirection(Qt.LeftToRight)
        self.start_button.setStyleSheet(u"padding: 6px;\n"
"background-color: #434350;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.start_button, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.stage_title = QWidget(self.mission_box)
        self.stage_title.setObjectName(u"stage_title")
        font16 = QFont()
        font16.setBold(True)
        self.stage_title.setFont(font16)
        self.horizontalLayout_2 = QHBoxLayout(self.stage_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(47, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.stage_title)
        self.label_3.setObjectName(u"label_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy7)
        font17 = QFont()
        font17.setFamilies([u"Inter"])
        font17.setBold(True)
        self.label_3.setFont(font17)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.stage_title)
        self.label_2.setObjectName(u"label_2")
        sizePolicy7.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy7)
        self.label_2.setFont(font17)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_4 = QLabel(self.stage_title)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
        self.label_4.setFont(font17)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(7, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_5 = QLabel(self.stage_title)
        self.label_5.setObjectName(u"label_5")
        sizePolicy7.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy7)
        self.label_5.setFont(font17)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.stage_title)
        self.label_6.setObjectName(u"label_6")
        sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy7)
        self.label_6.setFont(font17)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_15 = QLabel(self.stage_title)
        self.label_15.setObjectName(u"label_15")
        sizePolicy7.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy7)
        self.label_15.setFont(font17)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_15)


        self.verticalLayout_2.addWidget(self.stage_title)

        self.stage_bar = QProgressBar(self.mission_box)
        self.stage_bar.setObjectName(u"stage_bar")
        self.stage_bar.setStyleSheet(u"QProgressBar {\n"
"	margin: 0px 20px;\n"
"	border-radius: 5px;\n"
"	background-color: #555770;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 5px;\n"
"	background-color: #73dfe7;\n"
"	border: 2px solid #555770;\n"
"}")
        self.stage_bar.setMinimum(0)
        self.stage_bar.setMaximum(6)
        self.stage_bar.setValue(0)
        self.stage_bar.setTextVisible(False)
        self.stage_bar.setInvertedAppearance(False)

        self.verticalLayout_2.addWidget(self.stage_bar)


        self.gridLayout_6.addWidget(self.mission_box, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 18))
        font18 = QFont()
        self.menubar.setFont(font18)
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"	background-color: #1c1c28;\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"	color: white;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    background: #a8a8a8;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #888888;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(40, 41, 61); /* sets background of the menu */\n"
"    border: 1px solid gray;\n"
"	color: white;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    /* sets background of menu item. set this to something non-transparent\n"
"        if you want menu color and menu item color to be different */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QMenu::item:selected { /* when user selects item using mouse or keyboard */\n"
"    /* background-color: #654321; */\n"
"	background-color: rgba(231, 231, 231, 20);\n"
"}\n"
"\n"
"QMenu::separator {\n"
"	height: 1px"
                        ";\n"
"    background: gray;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"	margin-top: 5px;\n"
"	margin-bottom: 5px;\n"
"}")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTest = QMenu(self.menubar)
        self.menuTest.setObjectName(u"menuTest")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuMQTT = QMenu(self.menubar)
        self.menuMQTT.setObjectName(u"menuMQTT")
        self.menuSet_State = QMenu(self.menubar)
        self.menuSet_State.setObjectName(u"menuSet_State")
        self.menuBreak_System = QMenu(self.menubar)
        self.menuBreak_System.setObjectName(u"menuBreak_System")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMQTT.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuBreak_System.menuAction())
        self.menubar.addAction(self.menuSet_State.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menuFile.addAction(self.actionCSVLocation)
        self.menuFile.addAction(self.actionOpen_simulation_file)
        self.menuTest.addAction(self.actionParachute)
        self.menuTest.addAction(self.actionPoll)
        self.menuTest.addAction(self.actionToggle_Container_Camera)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionPayload_On)
        self.menuTest.addAction(self.actionPayload_Off)
        self.menuTest.addAction(self.actionReset_Camera_Rotation)
        self.menuTest.addAction(self.actionCalibrate_Gimbal_IMU)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionForce_Polling_Payload)
        self.menuTest.addAction(self.actionUnforce_Polling_Payload)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionToggle_Custom_Packet)
        self.menuWindow.addAction(self.actionFull_Screen)
        self.menuWindow.addAction(self.actionExit)
        self.menuMQTT.addAction(self.actionEnable)
        self.menuSet_State.addAction(self.action0_PRELAUNCH)
        self.menuSet_State.addAction(self.action1_LAUNCH)
        self.menuSet_State.addAction(self.action2_PARADEPLOY)
        self.menuSet_State.addAction(self.action3_TPDEPLOY)
        self.menuSet_State.addAction(self.action4_RELEASED)
        self.menuSet_State.addAction(self.action5_LAND)
        self.menuBreak_System.addAction(self.actionRelease_Sequence)
        self.menuBreak_System.addAction(self.actionRelease)
        self.menuBreak_System.addAction(self.actionBreak)
        self.menuBreak_System.addAction(self.actionHalt_Sequence)
        self.menuBreak_System.addSeparator()
        self.menuBreak_System.addAction(self.actionMode0)
        self.menuBreak_System.addAction(self.actionMode1)
        self.menuBreak_System.addAction(self.actionMode_2)
        self.menuBreak_System.addAction(self.actionMode_3)
        self.menuBreak_System.addAction(self.actionMode_4)

        self.retranslateUi(MainWindow)

        self.cmdSendButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Descendere Ground Station", None))
        self.actionCSVLocation.setText(QCoreApplication.translate("MainWindow", u"Open CSV file location", None))
        self.actionReset_Camera_Rotation.setText(QCoreApplication.translate("MainWindow", u"Reset Camera Rotation", None))
        self.actionParachute.setText(QCoreApplication.translate("MainWindow", u"Deploy Parachute", None))
        self.actionForce_2nd_parachute_deployment.setText(QCoreApplication.translate("MainWindow", u"Force 2nd parachute deployment", None))
        self.actionForce_stop_payload_deployment.setText(QCoreApplication.translate("MainWindow", u"Force stop payload deployment", None))
        self.actionFull_Screen.setText(QCoreApplication.translate("MainWindow", u"Full Screen", None))
#if QT_CONFIG(shortcut)
        self.actionFull_Screen.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.actionForce_timed_payload_deployment.setText(QCoreApplication.translate("MainWindow", u"Force timed payload deployment", None))
        self.actionOpen_simulation_file.setText(QCoreApplication.translate("MainWindow", u"Open simulation file", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionEnable.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.actionDisable.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.actionPoll.setText(QCoreApplication.translate("MainWindow", u"Poll Payload", None))
        self.actionStart_break_sequence.setText(QCoreApplication.translate("MainWindow", u"Start break sequence", None))
        self.actionRelease_Sequence.setText(QCoreApplication.translate("MainWindow", u"Run Sequence", None))
        self.actionRelease.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.actionBreak.setText(QCoreApplication.translate("MainWindow", u"Break", None))
        self.actionCalibrate_Gimbal_IMU.setText(QCoreApplication.translate("MainWindow", u"Calibrate Gimbal IMU", None))
        self.actionHalt_Sequence.setText(QCoreApplication.translate("MainWindow", u"Halt Sequence", None))
        self.action0_PRELAUNCH.setText(QCoreApplication.translate("MainWindow", u"0 - PRELAUNCH", None))
        self.action1_LAUNCH.setText(QCoreApplication.translate("MainWindow", u"1 - LAUNCH", None))
        self.action2_PARADEPLOY.setText(QCoreApplication.translate("MainWindow", u"2 - APOGEE", None))
        self.action3_TPDEPLOY.setText(QCoreApplication.translate("MainWindow", u"3 - PARADEPLOY", None))
        self.action4_RELEASED.setText(QCoreApplication.translate("MainWindow", u"4 - TPDEPLOY", None))
        self.action5_LAND.setText(QCoreApplication.translate("MainWindow", u"5 - LAND", None))
        self.actionForce_Polling_Payload.setText(QCoreApplication.translate("MainWindow", u"Force Polling Payload", None))
        self.actionUnforce_Polling_Payload.setText(QCoreApplication.translate("MainWindow", u"Unforce Polling Payload", None))
        self.actionMode0.setText(QCoreApplication.translate("MainWindow", u"Mode 0 (Original)", None))
        self.actionMode1.setText(QCoreApplication.translate("MainWindow", u"Mode 1 (Fast Change)", None))
        self.actionPayload_On.setText(QCoreApplication.translate("MainWindow", u"Payload On", None))
        self.actionPayload_Off.setText(QCoreApplication.translate("MainWindow", u"Payload Off", None))
        self.actionToggle_Container_Camera.setText(QCoreApplication.translate("MainWindow", u"Toggle Container Camera", None))
        self.actionToggle_Custom_Packet.setText(QCoreApplication.translate("MainWindow", u"Toggle Custom Packet", None))
        self.actionMode_2.setText(QCoreApplication.translate("MainWindow", u"Mode 2 (\u0e0a\u0e30\u0e25\u0e2d)", None))
        self.actionMode_3.setText(QCoreApplication.translate("MainWindow", u"Mode 3 (change delay from 0.5 s to 1 s)", None))
        self.actionMode_4.setText(QCoreApplication.translate("MainWindow", u"Mode 4 (\u0e01\u0e25\u0e31\u0e1a\u0e17\u0e35\u0e48 120)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/logo/assets/descendere_logo_resized.png\"/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DESCENDERE #1022", None))
        self.mission_time.setText(QCoreApplication.translate("MainWindow", u"NOT STARTED", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"XBEE Port:", None))
        self.port_refresh_button.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Simulation File:", None))
        self.sim_file_display.setText("")
        self.sim_file_button.setText(QCoreApplication.translate("MainWindow", u"CHOOSE FILE", None))
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"GPS LOCATION", None))
        self.lng_title_2.setText(QCoreApplication.translate("MainWindow", u"Satellite Connected:", None))
        self.sats_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lat_title.setText(QCoreApplication.translate("MainWindow", u"Latitude:", None))
        self.lat_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lng_title.setText(QCoreApplication.translate("MainWindow", u"Longitude:", None))
        self.lng_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"CONTAINER", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"STATE:", None))
        self.c_state.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.container_battery_percent.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.pkg_count_label_3.setText(QCoreApplication.translate("MainWindow", u"Healthy Packets:", None))
        self.c_healthy_pkg_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pkg_count_label_2.setText(QCoreApplication.translate("MainWindow", u"Corrupted Packets:", None))
        self.c_corrupted_pkg_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.c_temp_label.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.c_temp_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.c_altitude_label.setText(QCoreApplication.translate("MainWindow", u"Altitude:", None))
        self.c_altitude_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.c_gps_altitude_label.setText(QCoreApplication.translate("MainWindow", u"GPS Altitude:", None))
        self.c_gps_altitude_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.c_voltage_label.setText(QCoreApplication.translate("MainWindow", u"Voltage:", None))
        self.c_voltage_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.title_6.setText(QCoreApplication.translate("MainWindow", u"TELEMETRY CONTROL", None))
        self.total_pkg_title.setText(QCoreApplication.translate("MainWindow", u" Received:", None))
        self.total_pkg_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_corrupted_pkg_title.setText(QCoreApplication.translate("MainWindow", u"Corrupted:", None))
        self.total_corrupted_pkg_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.last_cmd_title.setText(QCoreApplication.translate("MainWindow", u"Last Command:", None))
        self.last_cmd_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cmd_select_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Power ON", None))
        self.cmd_select_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Power OFF", None))
        self.cmd_select_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Set Time", None))
        self.cmd_select_box.setItemText(3, QCoreApplication.translate("MainWindow", u"SIM Enable", None))
        self.cmd_select_box.setItemText(4, QCoreApplication.translate("MainWindow", u"SIM Activate", None))
        self.cmd_select_box.setItemText(5, QCoreApplication.translate("MainWindow", u"SIM Disable", None))
        self.cmd_select_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Set Apogee", None))

        self.cmd_select_box.setCurrentText(QCoreApplication.translate("MainWindow", u"Power ON", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Preview:", None))
        self.cmd_preview.setText("")
        self.cmdSendButton_2.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.autoscroll_check.setText(QCoreApplication.translate("MainWindow", u"Autoscroll", None))
        self.telemetry_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.title_5.setText(QCoreApplication.translate("MainWindow", u"TETHERED PAYLOAD", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"STATE:", None))
        self.p_state.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.payload_battery_percent.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.pkg_count_label_7.setText(QCoreApplication.translate("MainWindow", u"Healthy Packets:", None))
        self.p_healthy_pkg_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pkg_count_label_8.setText(QCoreApplication.translate("MainWindow", u"Corrupted Packets:", None))
        self.p_corrupted_pkg_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.p_temp_label.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.p_temp_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_gyro_label.setText(QCoreApplication.translate("MainWindow", u"Gyroscope:", None))
        self.p_gyro_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_accel_label.setText(QCoreApplication.translate("MainWindow", u"Acceleration:", None))
        self.p_accel_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_ptr_err_label.setText(QCoreApplication.translate("MainWindow", u"Pointing Error:", None))
        self.p_ptr_err_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_voltage_label.setText(QCoreApplication.translate("MainWindow", u"Voltage:", None))
        self.p_voltage_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_mag_label.setText(QCoreApplication.translate("MainWindow", u"Magnetometor:", None))
        self.p_mag_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_altitude_label.setText(QCoreApplication.translate("MainWindow", u"Altitude:", None))
        self.p_altitude_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.elapsed_time.setText(QCoreApplication.translate("MainWindow", u"T + HH:MM:SS.ms", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PRELAUNCH", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LAUNCH", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"APOGEE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PARADEPLOY", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TPDEPLOY", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"LAND", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTest.setTitle(QCoreApplication.translate("MainWindow", u"Testing", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuMQTT.setTitle(QCoreApplication.translate("MainWindow", u"MQTT", None))
        self.menuSet_State.setTitle(QCoreApplication.translate("MainWindow", u"FSW State Overwrite", None))
        self.menuBreak_System.setTitle(QCoreApplication.translate("MainWindow", u"Brake System", None))
    # retranslateUi

