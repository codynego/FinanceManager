# Generated by Django 5.0.7 on 2024-08-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_rename_transaction_date_transaction_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
