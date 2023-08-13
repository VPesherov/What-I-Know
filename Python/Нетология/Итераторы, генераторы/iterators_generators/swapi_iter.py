import requests


class SwapiIter:

    def __init__(self):
        pass

    def __iter__(self):
        self.next_page = r'https://swapi.py4e.com/api/people/'
        self.results = []
        return self

    def __next__(self):
        # если персонажей в списке не осталось - то
        if len(self.results) == 0:
            # проверяем есть ли следующая страница
            if not self.next_page:
                raise StopIteration
            # получаем api нашей следующей страницы
            data = requests.get(self.next_page).json()
            # передаём ей следующую страницу
            self.next_page = data['next']
            # получаем пачку результатов
            self.results = data['results']
        # если же персонажи есть то мы берём одного с конца - удаляем его и возвращаем с помощью pop
        return self.results.pop()


for item in SwapiIter():
    print(item)