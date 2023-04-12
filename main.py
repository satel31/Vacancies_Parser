from src.engine_requests import HHRequest, SJRequest
from src.connector_classes import ConnectorJson, ConnectorTXT
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
            connection = ConnectorJson()
        else:
            connection = ConnectorJson(filename)
    elif format_file == 'txt':
        print('Укажите имя файла, куда будут записаны результаты, в формате filename.txt. '
              'По умолчанию файл будет называться vacancies.txt. Укажите "ок", если согласны с названием')
        filename = input()
        if filename.lower() == 'ок':
            connection = ConnectorTXT()
        else:
            connection = ConnectorTXT(filename)
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
