from rest_framework import serializers
from .models import Certificate, Comment
from users.serializers import CustomUserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields ='__all__'


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields ='__all__'


