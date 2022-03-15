import PyQt5
from PyQt5 import QtGui
import serial

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QSlider, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Servo Test')
    w.setGeometry(50, 50, 320, 200)
    slider = QSlider(Qt.Horizontal, w)
    slider.setGeometry(30, 40, 200, 30)
    slider.setMinimum(0)
    slider.setMaximum(180)
    slider.setValue(90)
    label = QLabel(w)
    font = QtGui.QFont()
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(50)
    font.setFamily('Consolas')
    label.setFont(font)
    slider.valueChanged.connect(lambda x: label.setText(str(x)))
    slider.valueChanged.connect(lambda x: write(x))
    slider.valueChanged.connect(lambda: label.adjustSize())
    w.show()

    sys.exit(app.exec_())


s = serial.Serial('COM10')


def write(value: int):
    byte = value.to_bytes(1, 'little')
    print(byte)
    s.write(byte)


if __name__ == '__main__':
    main()
