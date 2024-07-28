from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
