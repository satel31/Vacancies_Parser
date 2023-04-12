from src.engine_requests import HHRequest, SJRequest
from src.connector_classes import ConnectorJson, ConnectorTXT, Connector
from src.user_interaction import user_interaction

if __name__ == '__main__':
    # Query for searching

    print('Добрый день! Введите поисковой запрос для поиска вакансий на платформах HeadHunter и SuperJob')
    search_query = input()

    # Query the name of the file
    print('Укажите формат файла, куда будут записаны результаты: json или txt')
    format_file = input()

    if format_file == 'json':
        print('Укажите имя файла, куда будут записаны результаты, в формате filename.json. '
              'По умолчанию файл будет называться vacancies.json. Укажите "ок", если согласны с названием')
        filename = input()
        if filename.lower() == 'ок':
            try:
                connection = ConnectorJson()
            except OSError:
                print('Файл уже существует. Хотите перезаписать файл? Введите да/нет')
                user_rewrite = input()
                if user_rewrite.lower() == 'да':
                    Connector.delete_data('src/vacancies.json')
                    connection = ConnectorJson()
                elif user_rewrite.lower() == 'нет':
                    print("Начните сначала")
        else:
            try:
                connection = ConnectorJson(filename)
            except OSError:
                print('Файл уже существует. Хотите перезаписать файл? Введите да/нет')
                user_rewrite = input()
                if user_rewrite.lower() == 'да':
                    Connector.delete_data(f'src/{filename}.json')
                    connection = ConnectorJson(filename)
                elif user_rewrite.lower() == 'нет':
                    print("Начните сначала")
    elif format_file == 'txt':
        print('Укажите имя файла, куда будут записаны результаты, в формате filename.txt. '
              'По умолчанию файл будет называться vacancies.txt. Укажите "ок", если согласны с названием')
        filename = input()
        if filename.lower() == 'ок':
            try:
                connection = ConnectorTXT()
            except OSError:
                print('Файл уже существует. Хотите перезаписать файл? Введите да/нет')
                user_rewrite = input()
                if user_rewrite.lower() == 'да':
                    Connector.delete_data('src/vacancies.txt')
                    connection = ConnectorTXT()
                elif user_rewrite.lower() == 'нет':
                    print("Начните сначала")
        else:
            try:
                connection = ConnectorTXT(filename)
            except OSError:
                print('Файл уже существует. Хотите перезаписать файл? Введите да/нет')
                user_rewrite = input()
                if user_rewrite.lower() == 'да':
                    Connector.delete_data(f'src/{filename}.txt')
                    connection = ConnectorTXT()
                elif user_rewrite.lower() == 'нет':
                    print("Начните сначала")
    else:
        print('К сожалению, такого формата нет. Начните сначала.')

    # Request for vacancies
    hh = HHRequest(search_query)
    sj = SJRequest(search_query)

    # Write to file
    hh.pass_by_page(connection)
    sj.pass_by_page(connection)

    print(f'Вакансии по Вашему запросу записаны в файл {connection.filename}')

    user_action = input('Вы хотите продолжить? Введите да/нет ')

    while user_action.lower() == 'да':
        user_interaction(connection)
        user_action = input('Вы хотите продолжить? Введите да/нет ')
