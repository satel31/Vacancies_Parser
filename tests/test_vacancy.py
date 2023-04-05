import pytest
from src.engine_requests import HHRequest, SJRequest
from src.vacancy import HHVacancy, SJVacancy


# test for HHVacancy class

@pytest.fixture
def hh():
    test_data = {'name': 'Data Scientist (Computer Vision)',
                 'url': 'https://api.hh.ru/areas/112',
                 'salary': {'from': None, "to": None},
                 'employer': {'id': '567799', 'name': 'red_mad_robot'},
                 'snippet': {'responsibility': 'Разрабатывать модели машинного обучения.'}}
    return HHVacancy(test_data)


def test_hh_init(hh):
    """Test of initialization of HHVacancy"""
    assert hh.vacancy_data == {'Название вакансии': 'Data Scientist (Computer Vision)',
                               'Ссылка на вакансию': 'https://api.hh.ru/areas/112',
                               'Верхняя граница з/п': 0, 'Нижняя граница з/п': 0,
                               'Валюта з/п': 'Данные о валюте отсутствуют',
                               'Краткое описание': 'Разрабатывать модели машинного обучения.',
                               'Компания': 'red_mad_robot'}


def test_hh_init_2():
    """Test of initialization of HHVacancy with other data"""
    test_data = {'name': 'Data Scientist (Computer Vision)',
                 'url': 'https://api.hh.ru/areas/112',
                 'salary': {'from': 10000, "to": "null"},
                 'employer': {'id': '567799', 'name': 'red_mad_robot'},
                 'snippet': {'responsibility': 'Разрабатывать модели машинного обучения.'}}
    hh_test = HHVacancy(test_data)
    assert hh_test.vacancy_data['Верхняя граница з/п'] == 0
    assert hh_test.vacancy_data['Нижняя граница з/п'] == 10000

# test for SJVacancy class

@pytest.fixture
def sj():
    test_data = {'profession': 'Data Scientist (Computer Vision)',
                 'link': 'https://www.superjob.ru/vakansii/prodavec-kassir-34322259.html',
                 'payment_from': None,
                 'payment_to': None,
                 'currency': 'rub',
                 'work': 'blablabla',
                 'firm_name': 'random',
                 }
    return SJVacancy(test_data)

def test_sj_init(sj):
    """Test of initialization of SJVacancy"""
    assert sj.vacancy_data == {'Название вакансии': 'Data Scientist (Computer Vision)',
                               'Ссылка на вакансию': 'https://www.superjob.ru/vakansii/prodavec-kassir-34322259.html',
                               'Нижняя граница з/п': 0,
                               'Верхняя граница з/п': 0,
                               'Валюта з/п': 'rub',
                               'Краткое описание': 'blablabla',
                               'Компания': 'random'}

def test_sj_init_2():
    """Test of initialization of SJVacancy with other data"""
    test_data = {'profession': 'Data Scientist (Computer Vision)',
                 'link': 'https://www.superjob.ru/vakansii/prodavec-kassir-34322259.html',
                 'payment_from': 10000,
                 'payment_to': '',
                 'currency': 'rub',
                 'work': None,
                 'firm_name': 'random',
                 }
    sj_test = SJVacancy(test_data)
    assert sj_test.vacancy_data['Верхняя граница з/п'] == 0
    assert sj_test.vacancy_data['Нижняя граница з/п'] == 10000
    assert sj_test.vacancy_data['Краткое описание'] == "Нет описания работы"