from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from account.permissions import AdminPermission
from rest_framework.permissions import AllowAny,IsAuthenticated

# Create your views here.


class TransactionViewAdmin(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AdminPermission]

class TransactionViewUser(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)