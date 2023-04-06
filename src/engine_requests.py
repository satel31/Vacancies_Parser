from abc import ABC, abstractmethod
import requests
from src.vacancy_classes import HHVacancy, SJVacancy


class EngingeRequest(ABC):
    """Abstract class for getting data"""

    def __init__(self, key_word: str, per_page: int = 100) -> None:
        self.key_word = key_word
        self.per_page = per_page
        self.__url = None

    @abstractmethod
    def request_data(self):
        pass

    @abstractmethod
    def pass_by_page(self, filename):
        pass


class HHRequest(EngingeRequest):
    """Class for getting data from hh.ru"""

    def __init__(self, key_word: str, per_page: int = 100) -> None:
        """Initialize the request with parameters of request and url"""
        super().__init__(key_word, per_page)
        self.__url: str = "https://api.hh.ru/vacancies"

    def request_data(self, page: int = 0) -> dict:
        """Got data from hh.ru"""
        params: dict = {
            "text": self.key_word,
            "page": page,
            "per_page": self.per_page
        }

        response = requests.get(self.__url, params=params)

        if response.status_code == 200:
            vacancies = response.json()
            return vacancies
        else:
            print("Error:", response.status_code)

    def pass_by_page(self, connection) -> list:
        """Pass data page by page"""

        data = self.request_data()
        pages: int = data['pages']
        for p in range(pages):
            data_by_page = self.request_data(p)
            for i in data_by_page['items']:
                hh = HHVacancy(i)
                connection.insert_hh(hh.vacancy_data)


class SJRequest(EngingeRequest):
    """Class for getting data from superjob.ru"""

    def __init__(self, key_word: str, per_page: int = 100) -> None:
        """Initialize the request with parameters of request and url"""
        super().__init__(key_word, per_page)
        self.__url: str = "https://api.superjob.ru/2.0/vacancies/"
        self.__id: str = "v3.r.130655195.6dd0db9873b05e3698bd20bcb8beeaedcd44e706.d98c5a5d24022a2455003edce45e22f69469b9e3"

    def request_data(self, page: int = 0) -> dict:
        """Got data from superjob.ru"""
        secret_key = {'X-Api-App-Id': self.__id}
        params: dict = {
            "text": self.key_word,
            "page": page,
            "count": self.per_page
        }

        response = requests.get(self.__url, headers=secret_key, params=params)

        if response.status_code == 200:
            vacancies = response.json()
            return vacancies
        else:
            print("Error:", response.status_code)

    def pass_by_page(self, connection) -> dict:
        """Pass data page by page"""
        # Максимальное количество сущностей, выдаваемых API равно 500.
        # Это значит, например, при поиске резюме по 100 резюме на страницу, всего можно просмотреть 5 страниц.
        pages = int(500 / self.per_page)

        for p in range(pages):
            data_by_page = self.request_data(p)
            for i in data_by_page['objects']:
                sj = SJVacancy(i)
                connection.insert_sj(sj.vacancy_data)
