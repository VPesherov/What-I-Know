import datetime
from functools import wraps

# а теперь попробуем обернуть нашу функцию foo
# переименовали wrapper в printable
# убираем args и kwargs
def printable(any_functions):
    @wraps(any_functions) # пометка 1
    # создаём новую функцию
    # которая выполняет всё то же самое что и раньше делал wrapper c args и kwargs
    def new_function(*args, **kwargs):
        print(f'Сейчас будет вызвана функция {any_functions}\nС аргументами: {args}, {kwargs}')
        # также можно сделать более красивый принт
        print(f'Сейчас будет вызвана функция {any_functions.__name__}\nС аргументами: {args}, {kwargs}')
        result = any_functions(*args, **kwargs)
        print('Выполнение закончено')
        print(f'Результат {result}')
        return result

    # и возвращаем новую фунцкиб
    return new_function


@printable  # равносильно тому foo = printable(foo)
def foo(a, b):
    return f'{a}{b}'


@printable  # и обарачивать сколько угодно функций
def bar():
    print('bar')


# здесь будет лежать наша new_function
# но мы её не вызываем, а возвращает только объект функции!
# foo = wrapper(foo)
# foo(1, 4)
# теперь мы просто можем её вызывать и будет работать наш printable

foo(1, 'test')
print('-' * 20)
bar()


# функции можно обарачивать в несколько декораторов

def speed_check(any_functions):
    @wraps(any_functions) # пометка 1
    def new_functions(*args, **kwargs):
        start = datetime.datetime.now()
        any_functions(*args, **kwargs)
        finish = datetime.datetime.now() - start
        print(f'Время работы функции: {any_functions} равно {finish}')

    return new_functions

# вот тут возникает проблема - мы теряем метаданные функции
# то есть в консоли теряется начальное именование нашей функции и её ячейка
# это может вызвать некоторые трудности в дальнейшем
@printable
@speed_check
def generate_big_array():
    big_array = range(10000)
    return list(big_array)


print('-' * 20)
big_array = generate_big_array()

print(generate_big_array)
# решить эту проблему нам поможет декоратор wraps
# from functools import wraps
# этот декоратор очень интересный - так как он принимает аргументы
# прописывать его надо перед new_function - в коде - пометка 1
# и теперь
print(generate_big_array) # и теперь наши мета данные не теряются
