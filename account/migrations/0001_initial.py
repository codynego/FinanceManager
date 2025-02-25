# Generated by Django 5.0.7 on 2024-07-28 20:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_type', models.CharField(default='savings', max_length=20)),
                ('currency', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('baseaccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.baseaccount')),
                ('interest_rate', models.DecimalField(decimal_places=2, default=10, max_digits=10)),
                ('interest_earned', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            bases=('account.baseaccount',),
        ),
    ]
