# реализуем стандартную функцию range в python
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.counter = self.start - 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= self.end:
            raise StopIteration

        return self.counter


# простой range - готов
for item in Range(1, 5):
    print(item)
