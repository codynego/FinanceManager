from rest_framework import serializers
from .models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Budget
        fields = "__all__"