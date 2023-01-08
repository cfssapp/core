from rest_framework import serializers
from .models import Certificate, Comment, CommentImage, Activity
from users.serializers import CustomUserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields ='__all__'


class CertificateSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Certificate
        fields ='__all__'