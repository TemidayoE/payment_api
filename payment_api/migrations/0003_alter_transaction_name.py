# Generated by Django 5.1.5 on 2025-01-24 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_api', '0002_transaction_name_alter_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
