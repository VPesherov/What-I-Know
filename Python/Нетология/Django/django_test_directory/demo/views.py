from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello World!')
