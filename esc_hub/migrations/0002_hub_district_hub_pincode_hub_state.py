# Generated by Django 5.1.6 on 2025-03-31 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_hub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hub',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hub',
            name='pincode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='hub',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
