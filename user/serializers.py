from rest_framework import Serializer
from .models import User



class UserSerializer(Serializer.ModelSerializer):
    password = Serializer.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    