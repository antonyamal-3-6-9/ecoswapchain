# Generated by Django 5.1.6 on 2025-03-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_product', '0005_rename_additionalmaterials_product_additional_materials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materials',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='materials',
            field=models.ManyToManyField(related_name='products', to='esc_product.materials'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='name',
            field=models.CharField(choices=[('wood', 'Wood'), ('metal', 'Metal'), ('plastic', 'Plastic'), ('glass', 'Glass'), ('paper', 'Paper'), ('fabric', 'Fabric'), ('ceramic', 'Ceramic'), ('rubber', 'Rubber'), ('leather', 'Leather'), ('stone', 'Stone'), ('bamboo', 'Bamboo'), ('cotton', 'Cotton'), ('silk', 'Silk'), ('wool', 'Wool'), ('linen', 'Linen'), ('hemp', 'Hemp'), ('jute', 'Jute'), ('coir', 'Coir'), ('sisal', 'Sisal'), ('cork', 'Cork')], max_length=255, unique=True),
        ),
    ]
