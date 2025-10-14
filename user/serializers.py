from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError as DjangoValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=100, required=True, write_only=True, style={'input_type': 'password'})
    passwordcheck = serializers.CharField(min_length=8, max_length=100, required=True, write_only=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    username = serializers.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'passwordcheck', 'first_name', 'last_name']

    def validate_password(self, value):
        try:
            validate_password(value)
        except DjangoValidationError as e:
            raise serializers.ValidationError(list(e.messages))

        return value

    def validate(self, data):
        if data['password'] != data['passwordcheck']:
            raise serializers.ValidationError({
                "password_check": "Паролі не співпадають."
            })

        return data

    def create(self, validated_data):
        validated_data.pop('passwordcheck')
        user = User.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'],
                                        first_name=validated_data.get('first_name',''),
                                        last_name=validated_data.get('last_name',''))
        return user
