# Generated by Django 5.0.7 on 2024-07-29 21:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_alter_baseaccount_account_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_created=True)),
                ('transaction_type', models.CharField(choices=[('INCOME', 'INCOME'), ('EXPENSE', 'EXPENSES')], max_length=20)),
                ('category', models.CharField(choices=[('HOUSING', 'HOUSING'), ('FOOD', 'FOOD'), ('TRANSPORTATION', 'TRANSAPORTATION'), ('FAMILY', 'FAMILY'), ('HOUSING', 'HOUSING'), ('OTHERS', 'OTHERS')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.CharField(max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.savingsaccount')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
