# Generated by Django 5.1.6 on 2025-04-08 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_order', '0013_swaporder_price'),
        ('esc_transaction', '0013_alter_tokentransaction_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='swaporder',
            name='escrow_transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='esc_transaction.tokentransaction'),
        ),
    ]
