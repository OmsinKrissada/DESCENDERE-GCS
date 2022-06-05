
import os
import os.path as _op
import numpy as _np
import dataclasses as _dataclasses
from typing import Union as _Union
from collections import OrderedDict as _Dict
from lib.logger import logger


@_dataclasses.dataclass(order=True, eq=True)
class Coordinate:
    """
    A class of coordinate consisting of latitude, longitude, altitude
    """
    latitude: _Union[int, float, str, None]
    longitude: _Union[int, float, str, None]
    altitude: _Union[int, float, str, None]

    def __post_init__(self):
        """
        Convert to float
        :return:
        """
        if self.latitude is None:
            self.latitude = 0.0
        else:
            self.latitude = float(self.latitude)

        if self.longitude is None:
            self.longitude = 0.0
        else:
            self.longitude = float(self.longitude)

        if self.altitude is None:
            self.altitude = 0.0
        else:
            self.altitude = float(self.altitude)

    def __bool__(self):
        return self.__len__() > 0

    def __len__(self):
        return len([x for x in [self.latitude, self.longitude, self.altitude] if x])


class LoadDirectory:
    def __init__(self, dir_filename: str, save_name: str, delim_extension: str, /, *,
                 earth_save_name: str = 'gearthcoord_save', device_id: _Union[int, str] = '1',
                 folder_name: str = 'data') -> None:
        """
        A class to create and manage directory and files in directory for
        special use cases in the ground control station.
        :param save_name: File name for delimited file
        :param delim_extension: File extension for delimited file
        :param earth_save_name: File name for Coordinate KML file
        :param dir_filename: Directory path must input '__file__' every time
        :param device_id: Device identification number or test number for files
        :param folder_name" Subfolder name for all data and temporary files to be saved
        """
        self.dir_filename = dir_filename
        self.global_path = self.getRootPath()
        self.device_id = str(device_id)
        self.save_name = save_name
        self.pre_save = earth_save_name
        self.extension = delim_extension
        if self.extension[0] == '.':
            self.extension = self.extension[1:]
        self.folder_name = folder_name
        self.name_temp_coord = 'tempcoord' + self.device_id + '.tmp'
        self.name_earth_coord = 'gearthcoord' + self.device_id + '.kml'
        self.name_earth_live = 'gearthlive' + self.device_id + '.kml'
        self.path_csv = ''
        self.path_raw = ''
        self.path_save_coord = ''
        self.path_temp_coord = self.__makeAbsolutePath(self.name_temp_coord)
        self.path_earth_coord = self.__makeAbsolutePath(self.name_earth_coord)
        self.path_earth_live = self.__makeAbsolutePath(self.name_earth_live)
        self.pos_save = 0
        self.pos_earth = 0

        self.earth_live_pre = '<?xml version="1.0" encoding="UTF-8"?>\n' + \
                              '<kml xmlns="http://www.opengis.net/kml/2.2" ' \
                              'xmlns:gx="http://www.google.com/kml/ext/2.2">\n' + \
                              '<NetworkLink>\n' + \
                              '<Link>\n<href>'
        self.earth_live_post = '</href>\n<refreshMode>onInterval</refreshMode>\n' + \
                               '<refreshInterval>1</refreshInterval>\n' + \
                               '</Link>\n' + \
                               '</NetworkLink>\n' + \
                               '</kml>\n'

        self.earth_coord_0 = '<kml xmlns="http://www.opengis.net/kml/2.2" ' \
                             'xmlns:gx="http://www.google.com/kml/ext/2.2">\n' + \
                             '<Folder>\n' + \
                             '<name>Log</name>\n' + \
                             '<Placemark>\n' + \
                             '<name>Device Path Plotting</name>\n' + \
                             '<Style>\n' + \
                             '<LineStyle>\n<color>'
        self.earth_coord_1 = '</color>\n<colorMode>normal</colorMode>\n' + \
                             '<width>3</width>\n' + \
                             '</LineStyle>\n' + \
                             '<PolyStyle>\n' + \
                             '<color>99000000</color>\n' + \
                             '<fill>1</fill>\n' + \
                             '</PolyStyle>\n' + \
                             '</Style>\n' + \
                             '<LineString>\n' + \
                             '<extrude>1</extrude>\n' + \
                             '<gx:altitudeMode>absolute</gx:altitudeMode>\n' + \
                             '<coordinates>\n'
        self.earth_coord_2 = '\n</coordinates>\n' + \
                             '</LineString>\n' + \
                             '</Placemark>\n' + \
                             '</Folder>\n' + \
                             '</kml>'

        self.all_coord = []

        self.__checkFolder()
        self.__checkPath()
        self.__renewPath()

    def __checkFolder(self) -> None:
        """
        Check if subfolder exists.
        :return:
        """
        self.createFolder(self.folder_name)
        logger.debug('Checked folder.')
        return

    def __checkPath(self, data_no: int = 1) -> None:
        """
        Check file name with iteration until the files are unique.
        :param data_no: Number to start file name iteration check
        :return:
        """
        self.__checkFolder()
        self.path_csv = self.__makeAbsolutePath(self.save_name + '_' + self.device_id +
                                                '_' + str(data_no) + '.' + self.extension)
        self.path_raw = self.__makeAbsolutePath(self.save_name + '_raw_' + self.device_id +
                                                '_' + str(data_no) + '.txt')
        self.path_save_coord = self.__makeAbsolutePath(self.pre_save + '_' + self.device_id +
                                                       '_' + str(data_no) + '.kml')
        while _op.isfile(self.path_csv) or _op.isfile(self.path_save_coord):
            data_no += 1
            self.path_csv = self.__makeAbsolutePath(self.save_name + '_' + self.device_id +
                                                    '_' + str(data_no) + '.' + self.extension)
            self.path_raw = self.__makeAbsolutePath(self.save_name + '_raw_' + self.device_id +
                                                    '_' + str(data_no) + '.txt')
            self.path_save_coord = self.__makeAbsolutePath(self.pre_save + '_' + self.device_id +
                                                           '_' + str(data_no) + '.kml')
        logger.debug('Checked path.')
        return

    def __makeAbsolutePath(self, filename) -> str:
        """
        Returns full absolute path with folder and file name.
        :param filename: File name
        :return: Path to file
        """
        folder = self.folder_name + '/' + filename
        path = _op.join(self.global_path, folder)
        logger.debug('Absolute path created.')
        return str(path)

    def __renewPath(self) -> None:
        """
        Renews path, clears old temporary files and creates a new one.
        :return:
        """
        if _op.isfile(self.path_temp_coord):
            os.remove(self.path_temp_coord)
        if _op.isfile(self.path_earth_coord):
            os.remove(self.path_earth_coord)
        if not _op.isfile(self.path_earth_live):
            self.createEarthLive(filename=self.path_earth_live,
                                 coord_filename=self.path_earth_coord)
        logger.debug('Path renewed.')
        return

    def appendEarthCoord(self, coords: Coordinate, /, *,
                         color: _Union[str, tuple] = 'ff00ffff', echo=False) -> str:
        """
        Append new coordinates to Google Earth KML coordinates file.
        :param coords: Dictionary of coordinates containing keys: latitude, longitude, altitude
        :param color: Color code ARGB in tuple or ABGR in hexadecimal string
        :return: String of Google Earth KML coordinates file
        """

        __color = ''
        if isinstance(color, tuple) and len(color) == 4:
            for code in reversed(color):
                __color += '{:02x}'.format(code)
        else:
            __color = color
        try:
            __latitude = '{:.6f}'.format(coords.latitude)
        except KeyError:
            raise KeyError(
                'Key error raised! Check for latitude key spelling.')
        try:
            __longitude = '{:.6f}'.format(coords.longitude)
        except KeyError:
            raise KeyError(
                'Key error raised! Check for longitude key spelling.')
        try:
            __altitude = '{:.2f}'.format(coords.altitude)
        except KeyError:
            raise KeyError(
                'Key error raised! Check for altitude key spelling.')

        __coord = ','.join([__longitude, __latitude, __altitude])
        if len(self.all_coord) <= 2:
            self.all_coord.append(__coord)

        # with open(self.path_temp_coord, mode='a+', encoding='utf-8') as f_temp:
        #     f_temp.write(__coord)
        if len(self.all_coord) == 1:
            with open(self.path_earth_coord, mode='w', encoding='utf-8') as f_gearth:
                f_gearth.write(self.earth_coord_0)
                f_gearth.write(__color)
                f_gearth.write(self.earth_coord_1)
                f_gearth.writelines(self.all_coord)
                f_gearth.write(self.earth_coord_2)
            with open(self.path_save_coord, mode='w', encoding='utf-8') as f_save:
                f_save.write(self.earth_coord_0)
                f_save.write(__color)
                f_save.write(self.earth_coord_1)
                f_save.writelines(self.all_coord)
                f_save.write(self.earth_coord_2)
        else:
            self.pos_earth = self.insertLine(
                self.path_earth_coord, -4, __coord, self.pos_earth)
            self.pos_save = self.insertLine(
                self.path_save_coord, -4, __coord, self.pos_save)
        logger.debug('Earth Coord File appended successfully!')
        if echo:
            return self.earth_coord_0 + color + self.earth_coord_1 + '\n'.join(__coord) + self.earth_coord_2
        return ''

    def appendDelimitedFile(self, *args: _Union[_np.ndarray, list, str], delimiter: str = ',') -> list:
        """
        Append a data file in a form of delimited string file, e.g., CSV.
        :param raw_data: Raw data, either full string with delimiter or a list of data
        :param delimiter: String delimiter
        :return: Raw data
        """
        __raw_data = []
        __raw_data_str = ''
        for raw_data in args:
            if raw_data:
                if isinstance(raw_data, list):
                    __raw_data.append(delimiter.join(
                        [str(dat) for dat in raw_data]))
                elif isinstance(raw_data, _np.ndarray):
                    __raw_data.append(delimiter.join(
                        [str(dat) for dat in raw_data]))
                elif isinstance(raw_data, str):
                    __raw_data_str += raw_data.strip()
                else:
                    __raw_data.append(str(raw_data).strip())
        if __raw_data:
            with open(self.path_csv, 'a', encoding='utf-8') as _file:
                __lst_tmp = [''.join([__data, '\n']) for __data in __raw_data]
                _file.writelines(__lst_tmp)
                logger.debug('Delimited File appended successfully!')
        if __raw_data_str:
            with open(self.path_raw, 'a', encoding='utf-8') as _file:
                _file.writelines([__raw_data_str, '\n'])
                logger.debug('Raw Data File appended successfully!')
        return __raw_data

    def getRootPath(self) -> str:
        """
        Get a root path
        :return: Root path
        """
        __filename = self.dir_filename
        return _op.abspath(_op.dirname(__filename))

    def createEarthLive(self, *, filename: str, coord_filename: str) -> str:
        """
        Create or overwrite Google Earth Live Feed KML file.
        :param filename: Google Earth Live Feed KML File path or name
        :param coord_filename: Google Earth Coordinates KML File path or name
        :return:
        """
        with open(filename, mode='w', encoding='utf-8') as f:
            f.writelines(self.earth_live_pre)
            f.writelines(coord_filename)
            f.writelines(self.earth_live_post)

        logger.debug('Earth Live File created successfully!')

        return ''

    @staticmethod
    def dictToList(raw_dict: _Union[_Dict, dict], tuple_data: _Union[list, tuple, set, dict]) -> list:
        return [raw_dict[key_avail] if key_avail in raw_dict else '' for key_avail in tuple_data]

    @staticmethod
    def createFolder(folder_name) -> None:
        """
        Create a directory (folder)
        :param folder_name: Folder or Subfolder name
        :return:
        """
        if not _op.exists(folder_name):
            os.makedirs(folder_name)
        return

    @staticmethod
    def insertLine(filename: str, lineno: int, text, latest_pos=0):
        """
        This static method inserts a line into mth line (m >= 0) which
        is an optimized alternative of rewriting the whole file.
        :param filename: File name or file path (str)
        :param lineno: Line number, can be absolute (>= 0) or relative to last element (< 0)
        :param text: Object which str() is callable to insert
        :return: None
        """
        last_end = []
        _p_file = 0
        with open(filename, "r+", encoding='utf-8') as fro:
            if latest_pos == 0:
                if lineno < 0:
                    _max_line = LoadDirectory.getLineCount(fro)
                    _lineno = _max_line + lineno
                else:
                    _lineno = lineno
                fro.seek(0)
                if _lineno < 0:
                    _lineno = 0
                _pos = 0
                _line = fro.readline()
                while _line:
                    if _pos == _lineno - 1:
                        _p_file = fro.tell()
                    if _pos >= _lineno:
                        last_end.append(_line)
                    _line = fro.readline()
                    _pos += 1
                fro.seek(_p_file)
            else:
                fro.seek(latest_pos)
                _line = fro.readline()
                while _line:
                    last_end.append(_line)
                    _line = fro.readline()
                fro.seek(latest_pos)
            fro.write(str(text) + '\n')
            new_latest_pos = fro.tell()
            fro.writelines(last_end)
        return new_latest_pos

    @staticmethod
    def blocks(file_object, size=2 ** 16):
        while True:
            b = file_object.read(size)
            if not b:
                break
            yield b

    @staticmethod
    def getLineCount(file_object):
        return sum(bl.count("\n") for bl in LoadDirectory.blocks(file_object))


# def updateMap(self, coords: tuple):
#     if coords[1] != 0 and coords[0] != 0:
#         self.coords += f'{coords[1]},{coords[0]},{self.c_altitude_data[-1]}\n'

#     with open('data.kml', 'w') as file:
#         file.writelines('''<?xml version="1.0" encoding="UTF-8"?>
# <kml xmlns="http://www.opengis.net/kml/2.2">
# <Document>
#     <name>DESCENDERE Container</name>
#     <Placemark>
#         <name>Flight Track</name>
#         <Style>
#             <LineStyle>
#                 <color>ff00ff00</color>
#                 <colorMode>normal</colorMode>
#                 <width>2</width>
#             </LineStyle>
#             <PolyStyle>
#                 <color>99000000</color>
#                 <fill>1</fill>
#             </PolyStyle>
#         </Style>
#         <LineString>
#             <extrude>1</extrude>
#             <tessellate>1</tessellate>
#             <altitudeMode>absolute</altitudeMode>
#             <coordinates>\n''')
#         file.writelines(self.coords)
#         file.writelines(
#             '\n' + '''</coordinates>
#         </LineString>
#     </Placemark>
# </Document>
# </kml>''')
