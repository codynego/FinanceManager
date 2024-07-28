from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import SavingsAccount
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class AccountListView(generics.ListCreateAPIView):
    queryset = SavingsAccount.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []
