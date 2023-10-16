from rest_framework import serializers

from api.models import Weapon


# class WeaponSerializers(serializers.Serializer):
#     power = serializers.IntegerField()
#     rarity = serializers.CharField()


class WeaponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weapon # какую модель используем
        fields = ['power', 'rarity'] # какие свойства
