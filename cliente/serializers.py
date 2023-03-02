from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if not email and not username:
            raise serializers.ValidationError('Se requiere correo electrónico o nombre de usuario')

        if email:
            try:
                User.objects.get(email=email)
                raise serializers.ValidationError('Email ya se encuentra en uso')
            except User.DoesNotExist:
                pass

        if username:
            try:
                User.objects.get(username=username)
                raise serializers.ValidationError('Username ya se encuentra en uso')
            except User.DoesNotExist:
                pass

        user = User(email=email, username=username)
        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {'password': serializer_errors['password']}
            )

        return data

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        if email:
            user = User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)
