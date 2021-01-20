from rest_framework import serializers
from .models import FoodItem, FoodOrder

class FoodItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodItem
        fields ='__all__'

class FoodOrderSerializer(serializers.ModelSerializer):
    items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = FoodOrder
        fields ='__all__'