from re import error
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class PasswordSerializer(serializers.Serializer):
    """
    Serializers for update password
    """
    old_password = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        """
        This method validates the password value is equal to confirm_password value
        """
        old_password = 'old_password' in data and data['old_password']
        password = 'password' in data and data['password']
        confirm_password = 'confirm_password' in data and data['confirm_password']
        errors = {}

        if not old_password:
            errors['old_password'] = ['Old password was not provided']

        if not password:
            errors['password'] = ['Password was not provided']
        
        if not confirm_password:
            errors['confirm_password'] = 'confirm password field cannot be empty'

        if len(errors):
            raise serializers.ValidationError(errors)

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("The two password fields don't match.")
        validate_password(data['password'], self.context['user'])

        return data

    def validate_old_password(self, value):
        """
        This method validates the old_password
        """
        user = self.context['user']
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect. Please enter it again.')
        return value

    def save(self):
        """
        This method saves the password to the user's details
        """
        password = self.validated_data['password']
        user = self.context['user']
        user.set_password(password)
        user.save()
        return user
