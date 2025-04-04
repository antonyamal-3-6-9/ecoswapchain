# Generated by Django 5.1.6 on 2025-03-31 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_hub', '0002_hub_district_hub_pincode_hub_state'),
        ('esc_order', '0008_alter_swaporder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingdetails',
            name='current_hub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_hub', to='esc_hub.hub'),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='destination_hub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='target_hub', to='esc_hub.hub'),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='product_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='source_hub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_hub', to='esc_hub.hub'),
        ),
    ]
