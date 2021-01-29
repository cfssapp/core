from rest_framework import serializers
from .models import FoodItem, FoodOrder, FoodAvatar, Address, Csv, SalesData, FakeData2

class FoodAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodAvatar
        fields ='__all__'
        # fields = ('file',)


class CsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Csv
        fields ='__all__'
        # fields = ('file',)


class FoodItemSerializer(serializers.ModelSerializer):
    avatar = FoodAvatarSerializer(read_only=True)

    class Meta:
        model = FoodItem
        fields ='__all__'


class FoodOrderSerializer(serializers.ModelSerializer):
    items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = FoodOrder
        fields ='__all__'


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields ='__all__'


# Fake data
class SalesDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesData
        fields = ('x','y')

class FakeDataSerializer(serializers.ModelSerializer):
    salesData = SalesDataSerializer(many=True, read_only=True)

    class Meta:
        model = FakeData2
        fields = ('salesData',)