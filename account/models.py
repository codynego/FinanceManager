from django.db import models
from user import User
from datetime import datetime


# Create your models here.


class BaseAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=False)
    balance = models.DecimalField(decimal_places=2)
    account_type = models.CharField(default="savings")
    currency = models.CharField(max_lenght=10, null=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)


class SavingsAccount(BaseAccount):
    DEFAULT_INTEREST_RATE = 10
    interest_rate = models.DecimalField(default=DEFAULT_INTEREST_RATE)
    interest_earned = models.DecimalField(decimal_places=2, null=True)


    def calculate_interest(self):
        #current_day = datetime.now() - self.created_at
        daily_interest = self.DEFAULT_INTEREST_RATE / 365
        self.interest_earned += self.balance * daily_interest
        return self.interest_earned