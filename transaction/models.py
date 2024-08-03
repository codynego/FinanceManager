from django.db import models
from user.models import User
from account.models import SavingsAccount
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Transaction(models.Model):
    TRANS_TYPE = (
        ("INCOME", "INCOME"),
        ("EXPENSE", "EXPENSE")
    )

    TRANS_CATEGORY = (
        ("HOUSING", "HOUSING"),
        ("FOOD", "FOOD"),
        ("TRANSPORTATION", "TRANSAPORTATION"),
        ("FAMILY", "FAMILY"),
        ("HOUSING", "HOUSING"),
        ("OTHERS", "OTHERS")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    type = models.CharField(choices=TRANS_TYPE, max_length=20)
    category = models.CharField(choices=TRANS_CATEGORY, max_length=20)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
    # account_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # account = GenericForeignKey(SavingsAccount, on_delete=models.CASCADE)
