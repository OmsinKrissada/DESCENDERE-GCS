import glob
import serial
import string
import sys

from serial.serialutil import SerialException
from logger import logger


class Port:
    def __init__(self, port_name: str, terminate_char: str, begin_char: str = None, baudrate=9600,  key=None):
        self.port_name = port_name
        self.baudrate = baudrate
        self.terminate_char = terminate_char
        self.key = key
        self.begin_char = begin_char
        self.device = None
        self.connected = False
        logger.debug('port init called')

    @staticmethod
    def list():
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()

                result.append(port)
            except serial.SerialException:
                pass    # legit 'except pass' here
            except Exception as e:
                logger.error(
                    f'An error occured during port check ({port}): {e}')
        if(result.__len__() == 0):
            logger.warning('No ports available')
        else:
            logger.info(f'{",".join(result)} available')
        return result

    def write(self, text: str):
        try:
            self.device.write(text.encode('utf-8'))
        except Exception as e:
            logger.error(f"Cannot write to {self.device}: {e}")

    def connect(self):
        if self.connected:
            logger.warning(
                f'Port {self.port_name} is already connected from port.py perspective.')
            return
        self.connected = True
        logger.debug('port connect called')
        try:
            self.device = serial.Serial(
                self.port_name, baudrate=self.baudrate, timeout=60)
            logger.info(f'Connected to port {self.device}')
        except Exception as e:
            logger.error(f"Cannot connect to port {self.device}: {e}")

    def read(self):
        combined = ''
        current_char = None
        while current_char != self.terminate_char:
            if self.device is None:
                raise DisconnectException
            try:
                # logger.debug('Trying to read from port')
                current_char = self.device.read().decode('utf-8')
                if current_char is None:
                    logger.debug(
                        'Received None while trying to read from port')
                    return
            except SerialException as e:
                logger.error(
                    f'Error reading/decoding character from serial: {e}')
                raise DisconnectException
            # logger.debug('Append while loop: ' +
            #              current_char)
            if self.begin_char is not None and current_char == self.begin_char:
                combined = ''
            if current_char in string.printable:
                combined += current_char
            # try:
            #     current_char = self.device.read().decode('utf-8')
            # except:
            #     pass
        combined = combined.replace('\r', '').replace('\n', '')
        return combined

    def reading(self):
        if self.device is None:
            print("No Serial device found! Try .connect to start device")
            return
        if self.key is not None:
            return self.reading_key()
        else:
            return self.reading_split()

    def reading_split(self):
        recieved = self.read().split(",")
        if len(recieved) != 0:
            with open(self.path, "at") as file:
                file.write(','.join(recieved))
                file.write('\n')

        return recieved

    def destroy(self):
        try:
            self.device.close()
        except Exception as e:
            logger.error(f'Unable to close serial port {self.port_name}: {e}')


class DisconnectException(Exception):
    pass


if __name__ == "__main__":
    ports = Port.list()
    for index, port in enumerate(ports):
        print(f'{index+1}:{port}')
    # selected_port = ports[int(input("Choose port :"))-1]
    # COM = Port(selected_port, '$')
    # COM.connect()
    # print(f'saving file to {COM.path}')
    # while True:
        # COM.reading()
