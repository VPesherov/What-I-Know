def foo():
    print('Call')


# разница между функцией и переменной - то что
# функцию мы можем вызвать а переменную нет
a = None
foo()

# но при этом мы можем и выводить нашу функцию без вызова
print(a)
# вывод покажет в какой ячейке памяти она находится
print(foo)

# а теперь давайте саму функцию положим в переменную а
a = foo
# всё работает и даже можно вызвать её
print(a)
a()


# на самом деле разница между функцией и переменной в магическом методе
# __call__

class Foo:
    def __call__(self, *args, **kwargs):
        print('call')


foo = Foo()
foo()


# мы даже можем нашу функцию положить в словарик
def foo():
    print('Call 1')
    pass


data = {'a': foo, 'b': foo}
data['c'] = foo
data['d'] = sum

# попробуем её вызвать
data['a']()
result = data['d']([1, 2, 3])
print(result)


# что нам это даёт? А то что мы можем передавать функцию в другие функции
# попробуем это реализовать

def wrapper(any_functions, *args, **kwargs):
    print(f'Сейчас будет вызвана функция {any_functions}')
    result = any_functions(*args, **kwargs)
    print('Выполнение закончено')
    print(f'Результат {result}')
    return result


# функция any - возвращает True если есть хотя бы один True
wrapper(any, (True, False, True))


# всё работает

# также это работает и с нашими личными функциями

def foo(a, b):
    return f'{a}{b}'


result = wrapper(foo, 4, 'bla')
print(result)

# продолжение в wrapper_continue.py
