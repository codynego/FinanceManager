from django.db import models
from user import User


# Create your models here.


class BaseAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=False)
    balance = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)