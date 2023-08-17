import unittest
from unittest import TestCase
from main import summarize, get_list, get_dict, multiply

# пометка 2 - есть некое число
SOME_NUMBER = 30


# давайте для каждой функции напишем свой класс, который будет всё это тестировать
class TestSummarize(TestCase):
    # первая проверка - на суммирование двух чисел
    # можно запускать тесты через треугольничек справа, а можно через консоль
    # python -m unittest tests.test_main
    def test_with_2_nums(self):
        x = 10
        y = 15
        res = summarize(x, y)
        expected = 25
        self.assertEquals(res, expected)

    # запустим ошибочный тест, посмотрим что выведет
    def test_with_2_negative(self):
        x = -20
        y = -29
        res = summarize(x, y)
        expected = -45
        self.assertGreater(res, expected)

    def test_result_in_range(self):
        x = 10
        y = 25
        range1 = range(35, 30)
        res = summarize(x, y)
        self.assertIn(res, range1)

    # этим тестом попробуем разобраться как будет выглядить то - что мы криво написали тест
    # в консоли он отобразит это количеством error
    def test_something(self):
        x = 10
        y = 20
        expected = 30
        res = summarize(10)
        self.assertEquals(res, expected)


class TestEtc(TestCase):
    # regex - сравнивая строку с регулякой
    def test_regex(self):
        pattern = '\d{2}-\d{2}-\d{4}'
        test_date1 = '25-06-2023'
        test_date2 = '28.09.2025'
        self.assertRegex(test_date1, pattern)
        # также можно указывать параметр msg, который выдасться при ошибке
        # self.assertRegex(test_date2, pattern, mgs='Wrong Date')

    # сравниваем списки по длинне и одинаковости элементов
    def test_list_length(self):
        list1 = [4, 3, 2, 1]
        res = get_list()
        self.assertCountEqual(res, list1)

    # проверка словарей на равенство и на структурированность элементов(идут в том же порядке)
    def test_dict(self):
        a = {'name': 'Ivan', 'city': 'Moscow', 'age': 29}
        res = get_dict()
        self.assertDictEqual(res, a)

    # пометка 1
    @unittest.expectedFailure
    def test_failure_unit_test(self):
        x, y = 19, 21
        res = summarize(x, y)
        self.assertFalse(res % 10 == 0)

    # пометка 2 - (условие, ответ при ошибке)
    @unittest.skipIf(SOME_NUMBER > 25, 'Too big value')
    def test_skipped_test(self):
        x, y = 20, 21
        res = multiply(x, y)
        expected = 420
        self.assertEquals(res, expected)


# далее перейдём к pytest

import pytest


# самое главное требование, чтоб название начиналось с test_
# и пишем функции
def test_multiply():
    x = 10
    y = 20
    res = multiply(x, y)
    expected = 200
    # тут мы используем как в python
    assert res == expected


def test_with_one_number():
    x = 20
    y = 22
    res = multiply(20, 22)
    expected = 0
    assert res == expected


# также можно объединить всё в класс
# главное чтоб класс начинался со слова Test

class TestMultiply:
    def test_something(self):
        x = 20
        y = 21
        res = multiply(20, 21)
        expected = 420
        assert res == expected

    # failed
    def test_something1(self):
        x = 20
        y = 21
        res = multiply(20, 21)
        expected = 421
        assert res == expected

    # помечаем его таким декоратором
    @pytest.mark.xfail
    # пометка 1 - он упал - значит всё нормально
    def test_failure(self):
        x = 20
        y = -10
        res = summarize(x, y)
        expected = 30
        assert res == expected

    # тут мы можем описывать кучу условий в отличии от unittest
    @pytest.mark.skipif(SOME_NUMBER > 25, reason='Too big value')
    def test_skip(self):
        x = 20
        y = -10
        res = summarize(x, y)
        expected = 30
        assert res == expected


# теперь попробуем указать тест который нам нужно чтоб была ошибка, то есть мы проверяем
# что на наборе данных у нас ошибка и эта ошибка и должна быть
# в этом нам помогут декораторы
# пометка 1

# теперь попробуем попропускать тесты на основании каких-то условий
# пометка 2
# в этом нам тоже помогут декораторы
# допустим у нас есть число, если больше этого числа то не выполняем тест

# теперь разберём вариант когда нам нужно один и тот же тест вызвать с разными параметрами
# кучу раз копировать было бы неудобно поэтому в pytest - есть особый случай
# это называется - параметризация
@pytest.mark.parametrize(
    'x,y,expected',
    [
        (20, 21, 420),
        (-10, 20, -200),
        (-10, -5, 50),
        (10, 11, 1110)
    ]
)
def test_with_params(x, y, expected):
    res = multiply(x, y)
    assert res == expected

# в итоге они запустятся как 4 разных теста
