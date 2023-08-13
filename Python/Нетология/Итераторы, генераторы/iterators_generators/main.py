class HelloWorld:

    def __init__(self, n=5):
        self.n = n

    def __iter__(self):
        self.counter = 0
        # всегда возвращается экземпляр данного класса
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > self.n:
            raise StopIteration
        return 'Hello World!'


for item in HelloWorld():
    print(item)
