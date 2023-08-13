def foo():
    # в отлии от return - yield - может быть много
    yield 1
    yield '0'
    yield None


foo_gen = foo()
print(foo_gen)

for item in foo_gen:
    print(item)
