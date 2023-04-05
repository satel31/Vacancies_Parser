import os
from abc import ABC, abstractmethod
import json


class Connector(ABC):
    """Abstract class for writing information to some file"""

    @abstractmethod
    def insert_hh(self, data_to_save):
        pass

    @abstractmethod
    def insert_sj(self, data_to_save):
        pass

    @abstractmethod
    def select_data_all(self, clue):
        pass

    @abstractmethod
    def select_data(self):
        pass


class ConnectorJson(Connector):
    """Class for working with json file"""

    def __init__(self, filename='vacancies.json'):
        """Make file with given filename"""
        self.filepath = f'..\Coursework_4\src\{filename}'

        if not os.path.exists(self.filepath):
            file = open(self.filepath, 'w', encoding='utf8')
            file.close()
        else:
            raise OSError('File already exists. Choose a different filename')

        self.__file = filename

    @property
    def filename(self):
        """Getter for filename"""
        return self.__file

    @filename.setter
    def filename(self, new_name):
        """Setter for new filename"""
        if new_name[-5:] == '.json':
            os.rename(self.filepath, f'../src/{new_name}')
            self.__file = new_name
        else:
            raise NameError('Wrong format. Correct format filename.json')

    def insert_hh(self, data_to_save: dict):
        """Write into the file hh vacancies object by object"""

        with open(self.filepath, 'a', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False)
            f.write(',')
            f.write('\n')

    def insert_sj(self, data_to_save):
        """Write into the file sj vacancies object by object"""

        with open(self.filepath, 'a', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False)
            f.write(',')
            f.write('\n')

    def select_data_all(self, clue):
        pass

    def select_data(self):
        pass
