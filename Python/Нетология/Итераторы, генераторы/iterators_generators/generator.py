def hello_world():
    while True:
        # если питон видет yiels - то эта функция вернёт специальный итерабельный объект
        # который будет возвращать то что мы ему дадим (в данном случае Hello World!)
        yield 'Hello World!'


hello_world_generator = hello_world()
for item in hello_world_generator:
    print(item)
