# Generated by Django 5.1.6 on 2025-03-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_order', '0003_alter_message_sender_alter_swaporder_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='house_no_or_name',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='landmark',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
    ]
