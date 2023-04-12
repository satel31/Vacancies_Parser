from src.connector_classes import ConnectorJson, ConnectorTXT, Connector
from src.vacancy_classes import Vacancy


def user_interaction(connection):
    """Ask the user for some action. Repeats, untill the user says no"""

    print('Теперь Вы можете:\n'
          '1) Найти новые вакансии\n'
          '2) Сортировка вакансий\n'
          '3) Вывести топ вакансии по уровню з/п\n'
          '4) Удалить вакансии\n'
          '5) Вывести все вакансии\n'
          '6) Переименовать файл\n'
          '7) Удалить файл')

    parameters_to_sort = '1) Название вакансии\n' \
                         '2) Нижняя граница з/п\n' \
                         '3) Верхняя граница з/п\n' \
                         '4) Нижняя граница з/п и верхняя граница з/п\n' \
                         '5) Валюта з/п\n' \
                         '6) Компания'

    user_action: str = input('Введите действие, как указано выше, без цифры')

    if user_action == 'Сортировка вакансий':
        print(f'Выберите один из доступных параметров для сортировки:\n {parameters_to_sort}')
        user_parameter_sort: str = input()

        if user_parameter_sort == 'Нижняя граница з/п':
            print('Введите сумму для сортировки')
            clue_from = int(input())
            clue_to = None
            result: list = connection.select_by_salary(clue_from, clue_to)

        elif user_parameter_sort == 'Верхняя граница з/п':
            print('Введите сумму для сортировки')
            clue_from = None
            clue_to = int(input())
            result: list = connection.select_by_salary(clue_from, clue_to)

        elif user_parameter_sort == 'Нижняя граница з/п и верхняя граница з/п':
            print('Введите суммы для сортировки в формате ХХХ - ХХХ')
            clues = input().split(' - ')
            clue_from = int(clues[0])
            clue_to = int(clues[1])
            result: list = connection.select_by_salary(clue_from, clue_to)

        else:
            print('Введите ключевое слово для сортировки')
            clue = input()
            result: list = connection.select_data(user_parameter_sort, clue)

        for item in result:
            print(item)

    elif user_action == 'Вывести топ вакансии по уровню з/п':
        print('Введите количество вакансий в топе')
        amount = int(input())
        data: list = connection.read_file()
        result: list = Vacancy.top_vacancies(amount, data)

        for item in result:
            print(item)

    elif user_action == 'Удалить вакансии':
        print(f'Выберите один из доступных параметров для сортировки:{parameters_to_sort}')
        user_parameter_del = input()
        print('Введите ключевое слово для удаления')

        if user_parameter_del == 'Нижняя граница з/п' or user_parameter_del == 'Верхняя граница з/п':
            clue_del = int(input())
            connection.delete_by_clue(user_parameter_del, clue_del)

        elif user_parameter_del == 'Нижняя граница з/п и верхняя граница з/п':
            print('Введите суммы для сортировки в формате ХХХ - ХХХ')
            clues = input().split(' - ')
            clue_from = int(clues[0])
            clue_to = int(clues[1])
            connection.delete_by_clue(user_parameter_del, clue_from)
            connection.delete_by_clue(user_parameter_del, clue_to)

        else:
            clue_del = input()
            connection.delete_data_by_clue(user_parameter_del, clue_del)

    elif user_action == 'Вывести все вакансии':
        result: list = connection.read_file()

        for item in result:
            print(item)

    elif user_action == 'Удалить файл':
        Connector.delete_data(connection.filepath)
        print('Работа завершена. Файл успешно удалён')

    elif user_action == 'Найти новые вакансии':
        print('Введите поисковой запрос для поиска вакансий на платформах HeadHunter и SuperJob')
        search_query = input()

        # Request for vacancies
        hh_new = HHRequest(search_query)
        sj_new = SJRequest(search_query)

        # Write to file
        hh_new.pass_by_page(connection)
        sj_new.pass_by_page(connection)

    elif user_action == 'Переименовать файл':

        print('Введите новое имя файл в формате filename.json или filename.txt в соответствии с актуальным форматом файла')
        new_filename = input()
        connection.filename = new_filename
        print(f'Имя файла изменено на {connection.filename}')
    else:
        print('К сожалению такое действие невозможно. Попробуйте ещё раз. Не забывайте указывать действия, как в образце')
