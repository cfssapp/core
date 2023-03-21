from rest_framework import serializers
from .models import TelegramSN, TelegramComment, TelegramUser


class TelegramUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields ='__all__'

class TelegramCommentSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer(read_only=True)

    class Meta:
        model = TelegramComment
        fields ='__all__'


class TelegramSNSerializer(serializers.ModelSerializer):
    comments = TelegramCommentSerializer(many=True, read_only=True)

    class Meta:
        model = TelegramSN
        fields ='__all__'



