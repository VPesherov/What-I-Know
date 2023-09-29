from django.db import models


# Create your models here.

# создадим модель автомобиль
class Car(models.Model):
    # поле brand - это поле varchar с максимальной длинной 50 символов
    brand = models.CharField(max_length=50)
    # max_length - является обязательным параметром
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    # Но на самом деле столбика не три, а четыре так как django автоматически добавляет столбик id
    # и отвечает за идентификацию каждой строки


# добавим ещё один класс, человек - который владеет автомобилем
class Person(models.Model):
    # у человека есть имя
    name = models.CharField(max_length=50)
    # а также у человека может быть автомобиль, а может и не быть
    # поэтому нам нужно связать его с нашим классом Car
    # здесь мы указываем с каким классом связать, а также указать параметр
    # on_delete - что делать если связанная запись исчезнет из базы данных
    # можно например поставить models.CASCADE - это будет значить, что если удалится
    # машина то, удалится и человек
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='owners')