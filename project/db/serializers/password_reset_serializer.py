from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


class PasswordResetSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["otp_code", "password", "confirm_password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        # This function checks if the user properly entered the data into the view
        validate_password(password=data['password'])
        password_match = data['password'] == data['confirm_password']
        otp_code = 'otp_code' in data and data['otp_code']

        errors = {}

        if not otp_code:
            errors['otp_code'] = ['Otp_code was not provided']

        if not password_match:
            errors['password_error'] = ['Password Mismatch']

        # If there are any errors, the serializer raises it
        if len(errors):
            raise serializers.ValidationError(errors)

        return data

    def update(self, instance, validated_data):
        # This function updates the password in the database after the validation has been done.
        instance.password = validated_data.get('password', instance.password)
        instance.set_password(instance.password)
        instance.save()

        return instance
