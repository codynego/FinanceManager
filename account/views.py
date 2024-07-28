from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework import status
from .models import SavingsAccount
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import GetAccountPermission

# Create your views here.

class AccountView(viewsets.ModelViewSet):
    queryset = SavingsAccount.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [GetAccountPermission]

# class AccountListView(generics.ListCreateAPIView):
#     queryset = SavingsAccount.objects.all()
#     serializer_class = AccountSerializer
#     permission_classes = [GetAccountPermission]

# class AccountDetailView(generics.RetrieveUpdateAPIView):
#     queryset = SavingsAccount.objects.all()
#     serializer_class = AccountSerializer
#     permission_classes = [IsAuthenticated]
