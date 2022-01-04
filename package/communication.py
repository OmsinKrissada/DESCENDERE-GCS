from port import Port
from settings import TEAM_ID
from logger import logger


class TelemetryHandler:
    def __init__(self, port_name: str) -> None:
        self.port = Port(port_name, '\r')
        self.port.connect()

    def read(self):
        data = self.port.read()
        logger.debug(f'Incoming telemetry: {data}')
        return data

    def sendCommand(self, command: str, data: str = ''):
        packet = f'CMD,{TEAM_ID},{command},{data}'
        self.port.write(packet)
        logger.info(f'Outgoing telemetry: {packet}')

    def setPort(self, port_name: str):
        self.port.destroy()
        self.port = Port(port_name, '\r')


if __name__ == '__main__':
    th = TelemetryHandler('COM10')
    for i in range(10):
        print('reading')
        print(th.read())
