from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    is_active = serializers.BooleanField(required=False)

    status = serializers.CharField(required=False)
    currentAuthority = serializers.CharField(required=False)
    success = serializers.CharField(required=False)

    class Meta:
        model = NewUser
        fields = ('id', 'email', 'user_name', 'password', 'is_active', 'avatar', 'status', 'currentAuthority', 'success')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
