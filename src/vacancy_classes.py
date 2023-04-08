class Vacancy:
    """Class for a vacancy"""

    # Exchange rates USD to RUB and EUR to RUB dd. 07/04/2023
    EXCHANGE_RATE_USD = 81.13
    EXCHANGE_RATE_EUR = 88.91

    def __init__(self) -> None:
        """Initialize all necessary data for a vacancy"""

        self._name: str = None
        self._url: str = None
        self._salary_from: int = None
        self._salary_to: int = None
        self._salary_currency: str = None
        self._short_description: str = None
        self._company_name: str = None
        self._salary_for_sorting = None

    @staticmethod
    def top_vacancies(amount: int, data: list) -> list:
        """Sort all vacancies by their biggest salary and returns top N"""

        sorted_data = sorted(data, key=lambda x: x['З/п для сортировки'], reverse=True)
        return sorted_data[0:amount]

    def __lt__(self, other) -> bool:
        """Compare two vacancies by their biggest salary"""

        return self._salary_for_sorting < other._salary_for_sorting

    def __gt__(self, other) -> bool:
        """Compare two vacancies by their biggest salary"""

        return self._salary_for_sorting > other._salary_for_sorting

    @property
    def vacancy_data(self) -> dict:
        """Returns the dictionary with all necessary information"""

        return {"Название вакансии": self._name,
                "Ссылка на вакансию": self._url,
                "Нижняя граница з/п": self._salary_from,
                "Верхняя граница з/п": self._salary_to,
                "Валюта з/п": self._salary_currency,
                "З/п для сортировки": self._salary_for_sorting,
                "Краткое описание": self._short_description,
                "Компания": self._company_name
                }

    def __repr__(self):
        return self.__dict__


class HHVacancy(Vacancy):
    """Class vor vacancy from hh.ru"""

    def __init__(self, data: dict) -> None:
        """Initialize the class HHVacancy"""
        self.data: dict = data

        super().__init__()

        self._name: str = self.data['name']
        self._url: str = self.data['url']
        self._salary_from: int = self.__set_salary('from')
        self._salary_to: int = self.__set_salary('to')
        self._salary_currency: str = self.__set_currency()
        self._short_description: str = self.data['snippet']['responsibility']
        self._company_name: str = self.data['employer']['name']
        self._salary_for_sorting: int = self.__salary_for_sorting()

    def __set_salary(self, key: str) -> int:
        """Change salary from/to to proper int type in case of str or None type"""

        try:
            return int(self.data['salary'][key])
        except TypeError:
            return 0
        except ValueError:
            return 0

    def __set_currency(self) -> str:
        """Returns the information about the missing currency data in case of error"""

        try:
            return self.data['salary']['currency']
        except KeyError:
            return 'Данные о валюте отсутствуют'
        except TypeError:
            return 'Данные о валюте отсутствуют'

    def __salary_for_sorting(self) -> int:
        """Set salary for sorting as the biggest salary from 'salary from/to' in rub"""
        if self._salary_to == 0:
            self._salary_for_sorting = self._salary_from
        else:
            self._salary_for_sorting = self._salary_to
        # Convert usd/eur to rub
        if self._salary_currency.lower() == 'usd':
            self._salary_for_sorting = round(self._salary_for_sorting * self.EXCHANGE_RATE_USD)
        elif self._salary_currency.lower() == 'eur':
            self._salary_for_sorting = round(self._salary_for_sorting * self.EXCHANGE_RATE_EUR)

        return self._salary_for_sorting


class SJVacancy(Vacancy):
    """Class vor vacancy from superjob.ru"""

    def __init__(self, data: dict) -> None:
        """Initialize the class SJVacancy"""

        self.data: dict = data
        super().__init__()

        self._name: str = self.data['profession']
        self._url: str = self.data['link']
        self._salary_from: int = self.__set_salary('payment_from')
        self._salary_to: int = self.__set_salary('payment_to')
        self._salary_currency: str = self.data['currency']
        self._short_description: str = self.__set_short_description
        self._company_name: str = self.data['firm_name']
        self._salary_for_sorting = self.__salary_for_sorting()

    def __set_salary(self, key: str) -> int:
        """Change salary from/to to proper int type in case of str or None type"""

        try:
            return int(self.data[key])
        except ValueError:
            return 0
        except TypeError:
            return 0

    @property
    def __set_short_description(self) -> str:
        """Set correct description of vacancy in case of None"""

        if self.data['work'] is None:
            return "Нет описания работы"
        return self.data['work']

    def __salary_for_sorting(self) -> int:
        """Set salary for sorting as the biggest salary from 'salary from/to' in rub"""

        if self._salary_to == 0:
            self._salary_for_sorting = self._salary_from
        else:
            self._salary_for_sorting = self._salary_to

        # Convert usd/eur to rub
        if self._salary_currency.lower() == 'usd':
            self._salary_for_sorting = round(self._salary_for_sorting * self.EXCHANGE_RATE_USD)
        elif self._salary_currency.lower() == 'eur':
            self._salary_for_sorting = round(self._salary_for_sorting * self.EXCHANGE_RATE_EUR)

        return self._salary_for_sorting
