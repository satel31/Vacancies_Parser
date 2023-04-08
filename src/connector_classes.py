import os
from abc import ABC, abstractmethod
import json

class Connector(ABC):
    """Abstract class for writing information to some file"""

    @abstractmethod
    def insert(self, data_to_save):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def select_data(self, parameter, clue):
        pass

    @abstractmethod
    def select_by_salary(self, clue_from, clue_to):
        pass

    @abstractmethod
    def delete_data(self):
        pass

    @abstractmethod
    def delete_data_by_clue(self, parameter, clue):
        pass


class ConnectorJson(Connector):
    """Class for working with json file"""

    def __init__(self, filename='vacancies.json'):
        """Make file with given filename"""
        self.filepath = f'C:/Users/Satel/PycharmProjects/Coursework_4/src/{filename}'

        if filename[-5:] != '.json':
            raise NameError('Wrong format. Correct format filename.json')

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

    def insert(self, data_to_save: dict):
        """Write into the file hh vacancies object by object"""

        with open(self.filepath, 'a', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False)
            f.write(',')
            f.write('\n')

    @property
    def read_file(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            text_divided = f'[{text.strip().strip(",")}]'

        return json.loads(text_divided)

    def select_data(self, parameter, clue):
        """Select data by parameter and clue"""
        result = []

        data = self.read_file

        for item in data:
            try:
                if item[parameter].lower() == clue.lower() or clue.lower() in item[parameter].lower():
                    result.append(item)
            except KeyError:
                print('This parameter does not exist. Please choose another')

        if len(result) == 0:
            print('There is no data for this parameter ')
        return result

    def select_by_salary(self, clue_from, clue_to):
        """Select data by salary"""
        result = []

        data = self.read_file

        for item in data:
            if clue_to and clue_from:
                if item['Нижняя граница з/п'] >= clue_from and item['Верхняя граница з/п'] <= clue_to:
                    result.append(item)
            elif clue_to:
                if item['Верхняя граница з/п'] <= clue_to:
                    result.append(item)
            elif clue_from:
                if item['Нижняя граница з/п'] >= clue_from:
                    result.append(item)

        if len(result) == 0:
            print('There is no data for this parameter ')
        return result

    def delete_data(self):
        os.remove(self.filepath)

    def delete_data_by_clue(self, parameter, clue):
        result = []

        data = self.read_file

        if isinstance(clue, str):
            clue = clue.lower()

        for item in data:
            try:
                if item[parameter] != clue:
                    result.append(item)
            except KeyError:
                pass

        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)
            f.write(',')
            f.write('\n')


class ConnectorTXT(Connector):
    """Class for working with txt file"""

    def __init__(self, filename='vacancies.txt'):
        """Make file with given filename"""
        self.filepath = f'C:/Users/Satel/PycharmProjects/Coursework_4/src/{filename}'

        if filename[-4:] != '.txt':
            raise NameError('Wrong format. Correct format filename.txt')

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
        if new_name[-4:] == '.txt':
            os.rename(self.filepath, f'../src/{new_name}')
            self.__file = new_name
        else:
            raise NameError('Wrong format. Correct format filename.txt')

    def insert(self, data_to_save: dict):
        """Write into the file hh vacancies object by object"""

        with open(self.filepath, 'a', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False)
            f.write(',')
            f.write('\n')

    @property
    def read_file(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            text_divided = f'[{text.strip().strip(",")}]'

        return json.loads(text_divided)

    def select_data(self, parameter, clue):
        """Select data by parameter and clue"""
        result = []

        data = self.read_file

        for item in data:
            try:
                if item[parameter].lower() == clue.lower() or clue.lower() in item[parameter].lower():
                    result.append(item)
            except KeyError:
                print('This parameter does not exist. Please choose another')

        if len(result) == 0:
            print('There is no data for this parameter ')
        return result

    def select_by_salary(self, clue_from, clue_to):
        """Select data by salary"""
        result = []

        data = list(self.read_file)

        for item in data:
            if clue_to and clue_from:
                if item['Нижняя граница з/п'] >= clue_from and item['Верхняя граница з/п'] <= clue_to:
                    result.append(item)
            elif clue_to:
                if item['Верхняя граница з/п'] <= clue_to:
                    result.append(item)
            elif clue_from:
                if item['Нижняя граница з/п'] >= clue_from:
                    result.append(item)

        if len(result) == 0:
            print('There is no data for this parameter ')
        return result

    def delete_data(self):
        os.remove(self.filepath)

    def delete_data_by_clue(self, parameter, clue):
        result = []

        data = self.read_file

        if isinstance(clue, str):
            clue = clue.lower()

        for item in data:
            try:
                if item[parameter] != clue:
                    result.append(item)
            except KeyError:
                pass

        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)
            f.write(',')
            f.write('\n')
