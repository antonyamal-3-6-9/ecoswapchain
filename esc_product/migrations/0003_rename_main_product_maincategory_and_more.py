# Generated by Django 5.1.6 on 2025-02-25 20:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_product', '0002_maincategory_rootcategory_remove_product_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='main',
            new_name='mainCategory',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='root',
            new_name='rootCategory',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additionalImages', to='esc_product.product'),
        ),
    ]
