from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Shop
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)
    name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'role', 'first_name', 'last_name', 'name')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError('Passwords do not match')

        role = data.get('role')
        if role not in ['customer', 'shop']:
            raise serializers.ValidationError('Role can only be customer or shop')

        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        name = validated_data.pop('name', None)

        user = User.objects.create_user(**validated_data, password=password)

        if role == 'customer':
            first_name = validated_data.pop('first_name')
            last_name = validated_data.pop('last_name')
            Customer.objects.create(user=user, first_name=first_name, last_name=last_name)
        elif role == 'shop':
            Shop.objects.create(user=user, name=name)

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid username or password')
        else:
            raise serializers.ValidationError('Must include "username" and "password"')

        data['user'] = user
        return data
