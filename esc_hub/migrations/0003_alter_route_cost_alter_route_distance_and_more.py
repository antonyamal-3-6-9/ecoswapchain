# Generated by Django 5.1.6 on 2025-04-02 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_hub', '0002_hub_district_hub_pincode_hub_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='distance',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='time',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='MSTPath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esc_hub.route')),
            ],
        ),
        migrations.CreateModel(
            name='MST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ManyToManyField(to='esc_hub.mstpath')),
            ],
        ),
    ]
