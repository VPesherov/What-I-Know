from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def hello_view(request: HttpRequest) -> HttpResponse:
    context = {
        'test': 5,
        'array': [1, 5, 9]
    }
    return render(request, 'demo.html', context=context) # путь к шаблонку указывается относительно папки templates
    # name = request.GET.get("name")
    # age = int(request.GET.get("age", 20))  # 20 - это дефолтное значение - если ничего не найдено
    # return HttpResponse(f'Hello {name}, {age}')


def sum1(request, a, b):
    result = a + b
    return HttpResponse(f'Sum = {result}')
