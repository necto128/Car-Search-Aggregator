from rest_framework import serializers

from apps.api.serializers import CarSerializers


class SearchCarSerialiserSwagger(CarSerializers):
    """
    Serializer for date car
    Extends CarSerializers to modify/add extra fields.
    """

    mark = serializers.CharField(default="Skoda")
    car_model = serializers.CharField(default="Octavia")
    generation = serializers.CharField(default="III")
    year_manufacture = serializers.DateField(default="2007")
    mileage = serializers.IntegerField(default=999000)
    type_price = serializers.ListField(
        child=serializers.CharField(), default=["BYN", "USD", "EUR"]
    )
    price = serializers.FloatField(default=2500)
    engine_type = serializers.ListField(
        child=serializers.CharField(), default=["A", "ДТ", "EV", "T+Э"]
    )
    body_type = serializers.CharField(default="Cедан")
    engine_capacity = serializers.FloatField(default=2.5)
    transmission = serializers.ListField(
        child=serializers.CharField(), default=["механическая", "автомат", "гибрид"]
    )
    engine_drive = serializers.ListField(
        child=serializers.CharField(), default=["передний", "задний", "полный"]
    )
