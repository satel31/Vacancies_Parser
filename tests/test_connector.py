import os
import pytest
from src.connector_classes import ConnectorJson, ConnectorTXT

try:
    os.remove(f'../src/test_file_set.json')
    os.remove(f'../src/test_file.json')
    os.remove(f'../src/test_selector.json')
    os.remove(f'../src/test_delete.json')
    os.remove(f'../src/test_delete_clue.json')

    os.remove(f'../src/test_file_set.txt')
    os.remove(f'../src/test_file.txt')
    os.remove(f'../src/test_selector.txt')
    os.remove(f'../src/test_delete.txt')
    os.remove(f'../src/test_delete_clue.txt')
except FileNotFoundError:
    print('All test files have been removed')


@pytest.fixture
def test_connector():
    return ConnectorJson('test_file.json')


@pytest.fixture
def test_connector_get():
    return ConnectorJson('test_file_get.json')


@pytest.fixture
def data_to_write():
    return [{'Название вакансии': 'Data Scientist (Computer Vision)',
             'Ссылка на вакансию': 'https://www.superjob.ru/vakansii/prodavec-kassir-34322259.html',
             'Верхняя граница з/п': 50000,
             'Нижняя граница з/п': 10000,
             'Валюта з/п': 'rub',
             'Краткое описание': 'blablabla',
             'Компания': 'random'},
            {'Название вакансии': 'Data Scientist (Computer Vision)',
             'Ссылка на вакансию': 'https://api.hh.ru/areas/112',
             'Верхняя граница з/п': 20000, 'Нижняя граница з/п': 30000,
             'Валюта з/п': 'Данные о валюте отсутствуют',
             'Краткое описание': 'Разрабатывать модели машинного обучения.',
             'Компания': 'red_mad_robot'}]


def test_connector_json_init(test_connector):
    assert os.path.exists(test_connector.filepath) is True
    with pytest.raises(NameError, match="Неправильный формат файла. Верный формат: filename.json"):
        test_connector_bad = ConnectorJson('test_selector.txt')


def test_connector_json_init_same():
    with pytest.raises(OSError, match="Файл уже существует. Выберите другое название файла"):
        test_s = ConnectorJson('test_file.json')


def test_connector_json_get(test_connector_get):
    assert test_connector_get.filename == 'test_file_get.json'
    test_connector_get.filename = 'test_file_set.json'
    assert test_connector_get.filename == 'test_file_set.json'
    with pytest.raises(NameError, match="Неправильный формат файла. Верный формат: filename.json"):
        test_connector_get.filename = 'test_file_set.txt'


def test_connector_select(data_to_write):
    test_selector = ConnectorJson('test_selector.json')
    for i in data_to_write:
        test_selector.insert(i)
    assert test_selector.select_data('Валюта з/п', 'rub')[0] == data_to_write[0]
    assert test_selector.select_data('Валюта', 'rub') == []
    assert test_selector.select_data('Валюта з/п', 'usd') == []
    assert test_selector.select_by_salary(15000, 20000)[0]['Верхняя граница з/п'] == 20000
    assert test_selector.select_by_salary(None, 40000)[0]['Верхняя граница з/п'] == 20000
    assert test_selector.select_by_salary(10000, None)[0]['Верхняя граница з/п'] == 50000


def test_delete_data():
    test_delete = ConnectorJson('test_delete.json')
    test_delete.delete_data()


def test_delete_data_by_clue(data_to_write):
    test_del_clue = ConnectorJson('test_delete_clue.json')
    for i in data_to_write:
        test_del_clue.insert(i)
    test_del_clue.delete_data_by_clue('Нижняя граница з/п', 10000)
    assert len(test_del_clue.read_file()) == 1


def test_delete_data_by_clue(data_to_write):
    test_del_clue = ConnectorJson('test_delete_clue_2.json')
    for i in data_to_write:
        test_del_clue.insert(i)
    test_del_clue.delete_data_by_clue('Компания', 'red_mad_robot')
    assert len(test_del_clue.read_file()) == 1


@pytest.fixture
def test_connector_txt():
    return ConnectorTXT('test_file.txt')


@pytest.fixture
def test_connector_get_txt():
    return ConnectorTXT('test_file_get.txt')


def test_connector_txt_init(test_connector_txt):
    assert os.path.exists(test_connector_txt.filepath) is True
    with pytest.raises(NameError, match="Неправильный формат файла. Верный формат: filename.txt"):
        test_connector_bad = ConnectorTXT('test_selector.json')


def test_connector_txt_init_same():
    with pytest.raises(OSError, match="Файл уже существует. Выберите другое название файла"):
        test_s = ConnectorTXT('test_file.txt')


def test_connector_txt_get(test_connector_get_txt):
    assert test_connector_get_txt.filename == 'test_file_get.txt'
    test_connector_get_txt.filename = 'test_file_set.txt'
    assert test_connector_get_txt.filename == 'test_file_set.txt'
    with pytest.raises(NameError, match="Неправильный формат файла. Верный формат: filename.txt"):
        test_connector_get_txt.filename = 'test_file_set.json'


def test_connector_select_txt(data_to_write):
    test_selector = ConnectorTXT('test_selector.txt')
    for i in data_to_write:
        test_selector.insert(i)
    assert test_selector.select_data('Валюта з/п', 'rub')[0] == data_to_write[0]
    assert test_selector.select_data('Валюта', 'rub') == []
    assert test_selector.select_data('Валюта з/п', 'usd') == []
    assert test_selector.select_by_salary(15000, 20000)[0]['Верхняя граница з/п'] == 20000
    assert test_selector.select_by_salary(None, 40000)[0]['Верхняя граница з/п'] == 20000
    assert test_selector.select_by_salary(10000, None)[0]['Верхняя граница з/п'] == 50000


def test_delete_data_txt():
    test_delete = ConnectorTXT('test_delete.txt')
    test_delete.delete_data()


def test_delete_data_by_clue_txt(data_to_write):
    test_del_clue = ConnectorTXT('test_delete_clue.txt')
    for i in data_to_write:
        test_del_clue.insert(i)
    test_del_clue.delete_data_by_clue('Нижняя граница з/п', 10000)
    assert len(test_del_clue.read_file()) == 1


def test_delete_data_by_clue_txt(data_to_write):
    test_del_clue = ConnectorTXT('test_delete_clue_2.txt')
    for i in data_to_write:
        test_del_clue.insert(i)
    test_del_clue.delete_data_by_clue('Компания', 'red_mad_robot')
    assert len(test_del_clue.read_file()) == 1
