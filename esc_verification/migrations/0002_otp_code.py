# Generated by Django 5.1.5 on 2025-02-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_verification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='code',
            field=models.IntegerField(null=True),
        ),
    ]
