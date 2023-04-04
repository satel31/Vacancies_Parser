from abc import ABC, abstractmethod

class Vacancy(ABC):
    """Abstract class for a vacancy"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class HHVacancy(Vacancy):
    """Class vor vacancies from hh.ru"""
    url = "https://api.hh.ru/vacancies"
    hh_vacancies = []
    AMOUNT_OF_VACANCIES = 5

    def __init__(self, key_word) -> None:
        """Initialize the class HHVacancy and make a dictionary with vacancies data"""
        self.key_word = key_word
        data: dict = self.get_vacancy_data()['items']
        for item in data:
            print(item)
            print()
            self.__name: str = item['name']
            self.__url: str = item['url']
            self.__salary_from: int = self.set_salary(item, 'from')
            self.__salary_to: int = self.set_salary(item, 'to')
            self.__salary_currency: str | None = self.set_currency(item)
            self.__salary_for_sort = self.key_for_sorting
            self.__short_description: str = item['snippet']['responsibility']
            self.__company_name: str = item['employer']['name']
            # записывать не в словарь, а в файл!!!
            self.hh_vacancies.append(self)
            print(self.hh_vacancies)
            print()
            print()

    def set_salary(self, vacancy, key):
        try:
            if isinstance(vacancy['salary'][key], int):
                return vacancy['salary'][key]
            else:
                return int(vacancy['salary'][key])
        except KeyError:
            return 0
        except TypeError:
            return 0

    def set_currency(self, vacancy):
        try:
            return vacancy['salary']['currency']
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def key_for_sorting(self):
        if self.__salary_to >= self.__salary_from:
            return self.__salary_to
        else:
            return self.__salary_from

    def sort_bigger_to_lower(self):
        self.hh_vacancies.sort(key=self.salary_to)

        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class SJVacancy(Vacancy):
    pass
