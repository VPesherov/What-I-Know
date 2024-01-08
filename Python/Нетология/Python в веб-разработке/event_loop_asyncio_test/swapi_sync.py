import datetime

import requests


def get_person(person_id):
    response = requests.get(f"https://swapi.py4e.com/api/people/{person_id}/")
    return response.json()


def main():
    person_1 = get_person(1)
    person_2 = get_person(2)
    person_3 = get_person(3)
    person_4 = get_person(4)
    print(person_1['name'], person_2['name'], person_3['name'], person_4['name'])


if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    print(datetime.datetime.now() - start)
