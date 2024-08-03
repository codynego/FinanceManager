from django.db import models
from user.models import User

# Create your models here.
class Budget(models.Model):

    CATEGORY = (
        ("HOUSING", "HOUSING"),
        ("FOOD", "FOOD"),
        ("TRANSPORTATION", "TRANSAPORTATION"),
        ("FAMILY", "FAMILY"),
        ("HOUSING", "HOUSING"),
        ("OTHERS", "OTHERS")
    )

    PERIOD_CAT = (
        ("MONTHLY", "MONTHLY"),
        ("QUARTERLY", "QUARTERLY"),
        ("ANNUALLY", "ANNUALLY"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(null=False, max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=CATEGORY, max_length=20)
    period = models.CharField(max_length=20, choices=PERIOD_CAT)
    created_at = models.DateTimeField(auto_created=True)