from rest_framework import serializers
from .models import FoodItem, FoodOrder, FoodAvatar

class FoodAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodAvatar
        fields ='__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    
    # avatar = FoodAvatarSerializer(read_only=True)
    # avatar = serializers.ImageField(source='avatar.file')

    class Meta:
        model = FoodItem
        fields ='__all__'

    def to_representation(self, instance):
        rep = super(FoodItemSerializer, self).to_representation(instance)
        # rep['avatar'] = FoodAvatarSerializer(instance.avatar.file).data
        rep['avatar'] = FoodAvatarSerializer(instance.file).data
        return rep


class FoodOrderSerializer(serializers.ModelSerializer):
    items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = FoodOrder
        fields ='__all__'