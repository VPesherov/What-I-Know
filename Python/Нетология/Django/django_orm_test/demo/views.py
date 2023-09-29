from django.http import HttpResponse
from django.shortcuts import render

from demo.models import Car, Person

import random


# Create your views here.

def create_car(request):
    car = Car(brand=random.choice(['B1', 'B2', 'B3']), model=random.choice(['M1', 'M2', 'M3']),
              color=random.choice(['color1', 'color2', 'color3']))
    car.save()
    return HttpResponse(f'Все получилось! Новая машина {car.brand}, {car.model}')


def list_car(request):
    car_objects = Car.objects.all()
    cars = [f'{c.id}: {c.brand}, {c.model}, {c.color} | {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))


def list_car_filter(request):
    car_objects = Car.objects.filter(brand__contains='2')
    cars = [f'{c.id}: {c.brand}, {c.model}, {c.color}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        # Person(name='P', car=car).save() первый способ
        Person.objects.create(name='P', car=car) # таким способом сразу создаётся объект и делать save - не надо
    return HttpResponse('Успех!')


def list_person(request):
    person_objects = Person.objects.all()
    persons = [f'{person.id}: {person.name}, {person.car.model}' for person in person_objects]
    return HttpResponse('<br>'.join(persons))
