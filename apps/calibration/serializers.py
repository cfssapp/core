from rest_framework import serializers
from .models import Certificate, Comment, CommentImage, Activity, Comment2
from users.serializers import CustomUserSerializer


class CommentImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentImage
        fields ='__all__'
        # fields = ('file',)


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    image = CommentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields ='__all__'

class Comment2Serializer(serializers.ModelSerializer):
    image = CommentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Comment2
        fields ='__all__'


class CertificateSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments2 = Comment2Serializer(many=True, read_only=True)

    class Meta:
        model = Certificate
        fields ='__all__'



class ActivitySerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    certificate = CertificateSerializer(read_only=True)

    class Meta:
        model = Activity
        fields ='__all__'