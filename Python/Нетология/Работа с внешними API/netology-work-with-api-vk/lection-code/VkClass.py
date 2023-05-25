import requests
from pprint import pprint


# теперь переделаем код из main.py для работы как с классом
class VkApiHandler:
    base_url = 'https://api.vk.com/method/'

    def __init__(self, access_token, version='5.131'):
        self.params = {
            'access_token': access_token,
            'v': version
        }

    # будем передавать наш объект, а также id юзера который хотим получить
    def get_user_date(self, user_ids):
        # тут в отличии от main.py - будем брать основную часть ссылки из вне
        # ссылка на api и вызов метода users.get из api
        method_name = f'{self.base_url}users.get'
        # передали параметры, user_ids - id юзера о котором хотим получить инфу
        # а также вместо версии и ключа передаём
        # наш объект, который содержит эти ключ и версию в self.params
        # запись с двумя звёздочкми означает, что атрибут парамс нашего объекта self - будет раскладываться
        params = {'user_ids': user_ids, **self.params}
        # используем get
        response = requests.get(url=method_name, params=params)
        # получаем результат ввиде json
        data = response.json()
        return data

    # расширенная верхняя функция, тоже самое, но дополнительно передаём fields
    def get_user_date_extended(self, user_ids, fields):
        # тут в отличии от main.py - будем брать основную часть ссылки из вне
        # ссылка на api и вызов метода users.get из api
        method_name = f'{self.base_url}users.get'
        # параметр fields - дополнительная информация о пользователе, которую хотим получить
        # пример заполнения fields
        # fields = 'bdate,city,followers_count'
        # передаём fields дополнительным параметром
        params = {'user_ids': user_ids, 'fields': fields, **self.params}
        response = requests.get(url=method_name, params=params)
        data = response.json()
        return data

    # функция для поиска груп, q - строка поиска, sort - сортировка групп, count - количество групп
    def search_groups(self, q, sort, count):
        url = self.base_url + 'groups.search'
        # аналагично верхним функциям в api смотрим параметры, которые методу можно передать и передаём их
        params = {'q': q, 'sort': sort, 'count': count, **self.params}
        response = requests.get(url, params=params)
        data = response.json()
        # тут вернём сразу с ключом response
        return data['response']

    def search_news(self, q, count):
        url = self.base_url + 'newsfeed.search'
        params = {'q': q, 'count': count, **self.params}
        response = requests.get(url=url, params=params)
        data = response.json()
        return data['response']


if __name__ == '__main__':
    with open('files/token.txt', 'rt') as token_file:
        token = token_file.readline()

    vk = VkApiHandler(token, '5.131')

    result = vk.get_user_date('1')
    pprint(result)
    # также можно передевать несколько юзеров, выведутся все
    result = vk.get_user_date_extended('1,2,3', 'bdate,city,followers_count')
    pprint(result)
    pprint('-' * 30)
    # найдём все группы, которые содержат в названии python
    # отсортируем их по количеству (цифра 6 - значит сортировка по количеству)
    # 2 - количество групп которую хотим
    groups = vk.search_groups('python', 6, 2)
    pprint(groups)

    print('-' * 30)
    news = vk.search_news('авто', 20)
    pprint(news)
