from rest_framework import serializers
from .models import Topic, Post
from users.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields ='__all__'


class TopicSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields ='__all__'