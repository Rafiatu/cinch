from rest_framework import serializers
from db.models.account import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['updated_at', 'created_at']
