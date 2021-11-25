from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        email_valid = 'email' in data and data['email']
        confirm_password = 'confirm_password' in data and data['confirm_password'].strip()
        password_match = data['password'].strip() == data['confirm_password'].strip()
        validate_password(password=data['password'].strip())

        errors = {}
        if not confirm_password:
            errors['confirm_password'] = ['field cannot be empty']

        if not password_match:
            errors['password_match'] = ['Password do not match']

        if not email_valid:
            errors['email'] = ['Invalid email']

        if len(errors):
            raise serializers.ValidationError(errors)

        return data


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["phone_number"]

    def validate(self, data):
        errors = {}

        if len(errors):
            raise serializers.ValidationError(errors)

        return data
