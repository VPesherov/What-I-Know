from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Weapon
from .serializers import WeaponSerializers


# с помощью декоратора указываем на какие методы реагировать в данном случае укажем GET
@api_view(['GET'])
def demo(request):
    data = {'message': 'Hello'}  # создадим произвольный словарь
    return Response(data)  # специальный класс который возвращает словарь


@api_view(['GET'])
def demo1(request):
    weapons = Weapon.objects.all()  # Достанем все оружия из нашей модели
    ser = WeaponSerializers(weapons, many=True) # отдадим наш объект и передадим параметр mane=True это укажет нашем сериализатору
                                                # что таких объектов много
    return Response(ser.data)  # специальный класс который возвращает словарь в данном случае ser.data


@api_view(['GET', 'POST'])
def demo2(request):
    if request.method == 'GET':
        weapons = Weapon.objects.all()  # Достанем все оружия из нашей модели
        ser = WeaponSerializers(weapons, many=True) # отдадим наш объект и передадим параметр mane=True это укажет нашем сериализатору
                                                    # что таких объектов много
        return Response(ser.data)  # специальный класс который возвращает словарь в данном случае ser.data
    if request.method == 'POST':
        return Response({'status': 'OK'})
