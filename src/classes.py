from ABC import ABC, abstractmethod
import requests

class Vacancy(ABC):
    """Abstract class for vacancies from different platforms"""

    @abstractmethod
    def get_vacancy_data(self):
        pass

    @abstractmethod
    def sort_vacancies(self):
        pass
class HHVacancy(Vacancy):
    pass

class SJVacancy(Vacancy):
    pass

hh_test = HHVacancy()
hh_test.get_vacancy_data()