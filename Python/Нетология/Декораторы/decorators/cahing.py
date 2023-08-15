# задача - кэширование
# очень часто так бывает - что функция работает медленно но при этом при разных параметрах
# даёт одни и те же результаты - наприме 9 * 2 = 18 и 3 * 6 = 18
# результат один и данные разные - попробуем что-то с этим сделать
# и закэшировать данные - например при обращении к пользователю по api
# мы можем несколько раз обращаться к одному и тому же пользователю
# и данные у него не меняются
# попробуем решить это с помощью декоратора
from functools import wraps
from wrapper_continue import speed_check

MAX_SIZE = 100  # пометка 2


# пометка 2 - расширяем декоратор чтоб он мог сам принимать значение max_size
# просто дописать в функцию any_cache - нельзя будет ошибка
# но можно обмануть немного систему
# создаём ещё функцию которое обернём и в неё будет поступать только max_size
def cached(max_size=100):
    # нашу бывшую функцию пометим символом _
    def cached_(any_function):
        cache = {}

        @wraps(any_function)
        def new_function(*args, **kwargs):
            key = f'{args}{kwargs}'
            if key in cache:
                return cache[key]
            if len(cache) >= MAX_SIZE:
                cache.popitem()
            result = any_function(*args, **kwargs)
            cache[key] = result

            return result

        return new_function

    # пометка 2 - вернём нашу cached_
    return cached_


@speed_check
@cached(max_size=100)
def generate_big_array1(n):
    big_array = range(n)
    return list(big_array)


print('\n' + '-' * 20)
print()
generate_big_array1(10000000)
# во второй раз уже функция работает быстрее
generate_big_array1(10000000)
# но возникает следующая проблема - эти кэши хранятся в оперативки и при большом их количестве
# она легко забьётся
# давайте попробуем это исправить -> пометка 2
# готово!
