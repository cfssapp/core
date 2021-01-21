from rest_framework import serializers
from .models import FoodItem, FoodOrder, FoodAvatar

class FoodAvatarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodAvatar
        fields ='__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    avatar = FoodAvatarSerializer(use_url=True)

    class Meta:
        model = FoodItem
        fields ='__all__'

class FoodOrderSerializer(serializers.ModelSerializer):
    items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = FoodOrder
        fields ='__all__'