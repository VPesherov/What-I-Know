from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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
    ser = WeaponSerializers(weapons,
                            many=True)  # отдадим наш объект и передадим параметр mane=True это укажет нашем сериализатору
    # что таких объектов много
    return Response(ser.data)  # специальный класс который возвращает словарь в данном случае ser.data


@api_view(['GET', 'POST'])
def demo2(request):
    if request.method == 'GET':
        weapons = Weapon.objects.all()  # Достанем все оружия из нашей модели
        ser = WeaponSerializers(weapons,
                                many=True)  # отдадим наш объект и передадим параметр mane=True это укажет нашем сериализатору
        # что таких объектов много
        return Response(ser.data)  # специальный класс который возвращает словарь в данном случае ser.data
    if request.method == 'POST':
        return Response({'status': 'OK'})


class DemoView(APIView):
    def get(self, request):
        weapons = Weapon.objects.all()  # Достанем все оружия из нашей модели
        ser = WeaponSerializers(weapons,
                                many=True)  # отдадим наш объект и передадим параметр mane=True это укажет нашем сериализатору
        # что таких объектов много
        return Response(ser.data)  # специальный класс который возвращает словарь в данном случае ser.data

    def post(self, requests):
        return Response({'status': 'OK demo 3'})


class DemoView1(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializers

    def post(self, request):
        return Response({'status': 'OK DemoView1'})


class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializers
