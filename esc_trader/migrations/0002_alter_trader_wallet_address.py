# Generated by Django 5.1.5 on 2025-02-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_trader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
