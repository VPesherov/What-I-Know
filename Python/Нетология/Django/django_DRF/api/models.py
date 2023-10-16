from django.db import models


# Create your models here.

class Weapon(models.Model):
    power = models.IntegerField()
    rarity = models.CharField(max_length=50)
    value = models.IntegerField()
