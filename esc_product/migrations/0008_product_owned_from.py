# Generated by Django 5.1.6 on 2025-04-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_product', '0007_remove_product_additional_materials_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owned_from',
            field=models.DateField(auto_now=True),
        ),
    ]
