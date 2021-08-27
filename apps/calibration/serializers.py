from rest_framework import serializers
from .models import Certificate
from users.serializers import CustomUserSerializer

class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields ='__all__'


