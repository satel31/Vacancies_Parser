from abc import ABC, abstractmethod

class Vacancy(ABC):
    """Abstract class for a vacancy"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def vacancy_data(self):
        pass


class HHVacancy(Vacancy):
    """Class vor vacancy from hh.ru"""

    def __init__(self, data: dict) -> None:
        """Initialize the class HHVacancy"""
        self.data: dict = data

        self.__name: str = self.data['name']
        self.__url: str = self.data['url']
        self.__salary_from: int = self.set_salary('from')
        self.__salary_to: int = self.set_salary('to')
        self.__salary_currency: str = self.set_currency()
        self.__short_description: str = self.data['snippet']['responsibility']
        self.__company_name: str = self.data['employer']['name']

    def set_salary(self, key) -> int:
        """Change salary from/to to proper int type in case of str or None type"""
        try:
            return int(self.data['salary'][key])
        except TypeError:
            return 0
        except ValueError:
            return 0

    def set_currency(self) -> str:
        """Returns the information about the missing currency data in case of error"""
        try:
            return self.data['salary']['currency']
        except KeyError:
            return 'Данные о валюте отсутствуют'
        except TypeError:
            return 'Данные о валюте отсутствуют'
    @property
    def vacancy_data(self) -> dict:
        """Returns the dictionaty woth all necessary information"""
        return {"Название вакансии": self.__name,
                "Ссылка на вакансию": self.__url,
                "Нижняя граница з/п": self.__salary_from,
                "Верхняя граница з/п": self.__salary_to,
                "Валюта з/п": self.__salary_currency,
                "Краткое описание": self.__short_description,
                "Компания": self.__company_name
                }


class SJVacancy(Vacancy):
    """Class vor vacancy from superjob.ru"""

    def __init__(self, data: dict) -> None:
        """Initialize the class SJVacancy"""
        self.data: dict = data

        self.__name: str = self.data['profession']
        self.__url: str = self.data['link']
        self.__salary_from: int = self.set_salary('payment_from')
        self.__salary_to: int = self.set_salary('payment_to')
        self.__salary_currency: str = self.data['currency']
        self.__short_description: str = self.set_short_description
        self.__company_name: str = self.data['firm_name']

    def set_salary(self, key) -> int:
        """Change salary from/to to proper int type in case of str or None type"""
        try:
            return int(self.data[key])
        except ValueError:
            return 0
        except TypeError:
            return 0

    @property
    def set_short_description(self):
        if self.data['work'] is None:
            return "Нет описания работы"
        return self.data['work']

    @property
    def vacancy_data(self) -> dict:
        """Returns the dictionaty woth all necessary information"""
        return {"Название вакансии": self.__name,
                "Ссылка на вакансию": self.__url,
                "Нижняя граница з/п": self.__salary_from,
                "Верхняя граница з/п": self.__salary_to,
                "Валюта з/п": self.__salary_currency,
                "Краткое описание": self.__short_description,
                "Компания": self.__company_name
                }
