import requests
from pprint import pprint


# обычная функция без дополнительный полезей
def get_user_date(token):
    # ссылка на api и вызов метода users.get из api
    url = r'https://api.vk.com/method/users.get'
    # передали параметры, id - id юзера о котором хотим получить инфу
    # access_token - наш обязательный ключ, без него ничего работать не будет
    # v - версия - тоже обязательный параметр
    params = {'user_ids': '1', 'access_token': token, 'v': '5.131'}
    # используем get
    response = requests.get(url=url, params=params)
    # получаем результат ввиде json
    data = response.json()
    return data


# расширенная верхняя функция, тоже самое, но дополнительно передаём fields
def get_user_date_extended(token):
    url = r'https://api.vk.com/method/users.get'
    # параметр fields - дополнительная информация о пользователе, которую хотим получить
    fields = 'bdate,city,followers_count'
    # передаём fields дополнительным параметром
    params = {'user_ids': '1', 'access_token': token, 'v': '5.131', 'fields': fields}
    response = requests.get(url=url, params=params)
    data = response.json()
    return data


if __name__ == '__main__':
    with open('files/token.txt', 'rt') as token_file:
        token = token_file.readline()
    result = get_user_date(token)
    pprint(result)
    result = get_user_date_extended(token)
    pprint(result)
