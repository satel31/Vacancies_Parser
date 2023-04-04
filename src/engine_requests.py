from abc import ABC, abstractmethod
import requests


class EngingeRequest(ABC):
    """Abstract class for getting data"""

    @abstractmethod
    def request_data(self):
        pass

    @abstractmethod
    def pass_by_page(self):
        pass


class HHRequest(EngingeRequest):
    """Class for getting data from hh.ru"""

    def __init__(self, key_word, per_page=10) -> None:
        """Initialize the request with parameters of request and url"""
        self.key_word = key_word
        self.per_page = per_page
        self.url = "https://api.hh.ru/vacancies"

    def request_data(self, page=0) -> dict:
        """Got data from hh.ru"""
        params = {
            "text": self.key_word,
            "page": page,
            "per_page": self.per_page
        }
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            vacancies = response.json()
            return vacancies
        else:
            print("Error:", response.status_code)

    def pass_by_page(self):
        """Pass data page by page"""
        data = self.request_data()
        pages = data['pages']
        for p in range(pages):
            #pass thorough some other class?
            return self.request_data(p)



class SJRequest(EngingeRequest):
    def __init__(self):
        pass

    def request_data(self):
        pass

    def pass_by_page(self):
        pass
