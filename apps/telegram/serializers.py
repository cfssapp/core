from rest_framework import serializers
from .models import TelegramSN, TelegramComment
from users.serializers import CustomUserSerializer



class TelegramCommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = TelegramComment
        fields ='__all__'


class TelegramSNSerializer(serializers.ModelSerializer):
    comments = TelegramCommentSerializer(many=True, read_only=True)

    class Meta:
        model = TelegramSN
        fields ='__all__'



