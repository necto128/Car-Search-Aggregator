from rest_framework import serializers


class CarSerializers(serializers.Serializer):
    """
    Serializer for date car
    """

    mark = serializers.CharField(max_length=20, min_length=2, required=True)
    car_model = serializers.CharField(min_length=1, required=False)
    # поколение
    generation = serializers.CharField(min_length=1, required=False)
    # год выпуска
    year_manufacture = serializers.DateField(format="%Y")
    # пробег
    mileage = serializers.IntegerField(required=False)
    # цена(р,д,е)
    type_price = serializers.ListField(
        child=serializers.CharField(), default=["BYN", "USD", "EUR"]
    )
    # цена
    price = serializers.FloatField(required=False)
    # тип двигателя(бен, дизель, эл, гибрид)
    engine_type = serializers.ListField(
        child=serializers.CharField(), default=["A", "ДТ", "EV", "T+Э"]
    )
    # тип кузова
    body_type = serializers.CharField(max_length=20, min_length=2, required=False)
    # обьём двигеля
    engine_capacity = serializers.FloatField(required=False)
    # коробка передач(авт,мех, гиб)
    transmission = serializers.ListField(
        child=serializers.CharField(), default=["механическая", "автомат", "гибрид"]
    )
    # привод(перед, зад, полный)
    engine_drive = serializers.ListField(
        child=serializers.CharField(), default=["передний", "задний", "полный"]
    )
