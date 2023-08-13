import requests


def get_swapi_people():
    next_page = r'https://swapi.py4e.com/api/people/'
    while next_page:
        data = requests.get(next_page).json()
        next_page = data['next']
        results = data['results']
        for item in results:
            yield item


for item in get_swapi_people():
    print(item)
