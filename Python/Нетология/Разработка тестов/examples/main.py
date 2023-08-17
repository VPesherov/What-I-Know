def summarize(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def get_dict():
    return {'name': 'Ivan', 'age': 29, 'city': 'Moscow'}


def get_list():
    return [1, 2, 3, 4]


# для начала нужно понять что такое оператор assert
# assert - служит для того - чтоб проверять какие-то выражения на истинность

res = summarize(10, 20)
expected = 30
expected2 = 35

# тут всё ок
assert res == expected
# тут выбросит исключение
# assert res == expected2
