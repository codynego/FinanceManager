from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'transaction_type', 'category', 'amount', 'transaction_date']