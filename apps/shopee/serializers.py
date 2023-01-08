from rest_framework import serializers
from .models import Cart, Product
from users.serializers import CustomUserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Product
        fields ='__all__'


class CartSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    # list = ProductSerializer(many=False, read_only=True)
    list = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields ='__all__'