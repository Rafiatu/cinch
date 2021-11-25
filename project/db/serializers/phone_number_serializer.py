from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(required=False)

    def validate(self, data):
        phone_number_valid = 'phone_number' in data and data['phone_number']

        errors = {}
        if not phone_number_valid:
            errors['phone_number'] = ['Please provide a valid phone number']

        if len(errors):
            raise serializers.ValidationError(errors)

        return data