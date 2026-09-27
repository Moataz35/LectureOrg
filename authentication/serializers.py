from .models import CustomUser
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return user

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['role']
