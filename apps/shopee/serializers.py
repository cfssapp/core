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
    products = ProductSerializer(many=True, read_only=True)

    list = serializers.CharField(source='products')

    class Meta:
        model = Cart
        fields ='__all__'