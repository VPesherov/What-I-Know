from django.contrib import admin
from .models import Person, Car


# Register your models here.
# создаём слеудющий код
@admin.register(Car) # указывает для какого класса наша админка
class CarAdmin(admin.ModelAdmin): # обязательно наследуемся от admin.ModelAdmin
    list_display = ['id', 'brand', 'model', 'color']
    list_filter = ['brand', 'model']
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']

