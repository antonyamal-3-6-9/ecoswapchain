# Generated by Django 5.1.6 on 2025-02-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_nft', '0005_alter_nft_owner_alter_nft_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
