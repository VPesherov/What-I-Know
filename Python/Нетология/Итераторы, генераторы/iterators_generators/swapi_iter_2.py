import requests


class SwapiIter:

    def __init__(self):
        pass

    def __iter__(self):
        self.next_page = r'https://swapi.py4e.com/api/people/'
        self.results = []
        # в отличии от кода swapi_iter - тут более правильно будет двигаться по индексам героев
        # чем удалять их
        self.i = -1
        return self

    def __next__(self):
        # переходим к следующему индексу героя
        self.i += 1
        if self.i >= len(self.results):
            # проверяем есть ли следующая страница
            if not self.next_page:
                raise StopIteration
            # получаем api нашей следующей страницы
            data = requests.get(self.next_page).json()
            # передаём ей следующую страницу
            self.next_page = data['next']
            # получаем пачку результатов
            self.results = data['results']
            self.i = 0
        # если же персонажи есть то мы берём одного с конца - удаляем его и возвращаем с помощью pop
        return self.results[self.i]


for item in SwapiIter():
    print(item)
