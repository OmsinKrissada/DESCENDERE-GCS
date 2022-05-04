from time import sleep
from port import Port
from settings import TEAM_ID
from logger import logger


class TelemetryHandler:
    terminating_char = '\r'

    def __init__(self, port_name: str) -> None:
        self.port = Port(port_name, self.terminating_char, baudrate=115200)
        self.port.connect()

    def read(self):
        data = self.port.read()
        logger.debug(f'Incoming telemetry: {data}')
        return data

    def sendCommand(self, command: str, data: str = ''):
        self.sendRawCommand(f'CMD,{TEAM_ID},{command},{data}\r')

    def sendRawCommand(self, text: str):
        for i in range(2):
            self.port.write(text)
        # sleep(0.1)
        logger.info(f'Outgoing telemetry: {text}')

    @staticmethod
    def previewSendCommand(command: str, data: str = ''):
        return f'CMD,{TEAM_ID},{command},{data}\r'

    def setPort(self, port_name: str):
        self.port.destroy()
        self.port = Port(port_name, self.terminating_char)
        self.port.connect()

    def destroy(self):
        self.port.destroy()


if __name__ == '__main__':
    th = TelemetryHandler('COM10')
    for i in range(10):
        print('reading')
        print(th.read())
