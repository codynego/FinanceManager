from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Budget
from .serializers import BudgetSerializer

# Create your views here.

class BudgetViewAdmin(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permissions = [IsAuthenticated]
