# Generated by Django 5.1.6 on 2025-04-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_order', '0010_address_district_address_district_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
