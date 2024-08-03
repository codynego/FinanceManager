from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'account', 'type', 'category', 'amount', 'date']
        