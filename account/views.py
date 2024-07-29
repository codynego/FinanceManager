from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework import status
from .models import SavingsAccount
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminPermission
from rest_framework.decorators import action
from rest_framework.views import APIView


# Create your views here.

class AccountView(viewsets.ModelViewSet):
    queryset = SavingsAccount.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AdminPermission]

class UserAccount(APIView):
    def get(self, request):
        try:
            account = SavingsAccount.objects.get(user=request.user)
            serializer = AccountSerializer(account)
            return Response({"data": serializer.data, "status": status.HTTP_200_OK, "message": "account retrieved"})
        except:
            return Response({"data": None, "status": status.HTTP_404_NOT_FOUND, "message": "account not found"})

class UserAccountView(viewsets.ModelViewSet):
    queryset = SavingsAccount.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


    @action(detail=False, methods=['get'])
    def list(self, request):
        try:
            data = SavingsAccount.objects.get(user=request.user)
            serializer = self.serializer_class(data)
            return Response({"data": serializer.data, "status":status.HTTP_200_OK, "message": "Account retrieved succesfully"})
        except Exception:
            return Response({"data": None, "status":status.HTTP_404_NOT_FOUND, "message": "user Account found"})



# class AccountListView(generics.ListCreateAPIView):
#     queryset = SavingsAccount.objects.all()
#     serializer_class = AccountSerializer
#     permission_classes = [GetAccountPermission]

# class AccountDetailView(generics.RetrieveUpdateAPIView):
#     queryset = SavingsAccount.objects.all()
#     serializer_class = AccountSerializer
#     permission_classes = [IsAuthenticated]
