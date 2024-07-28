from rest_framework import serializers
from .models import SavingsAccount


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavingsAccount
        fields = ["user", "balance", "account_type", "currency"]