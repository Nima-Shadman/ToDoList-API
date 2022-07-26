from asyncore import read, write
from dataclasses import field
from pyexpat import model
from re import U
from rest_framework import serializers

from authentication.models import User

class RegisterSerilaizer(serializers.ModelSerializer):
    password  =serializers.CharField(
        max_length=128, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ('username','email','password',)

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password  =serializers.CharField(
        max_length=128, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ('email','username','password','token')
        read_only_fields = ['token']
        