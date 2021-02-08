from rest_framework import serializers
from .models import Topic
from users.serializers import CustomUserSerializer


class TopicSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Topic
        fields ='__all__'