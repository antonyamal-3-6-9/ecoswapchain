# Generated by Django 5.1.6 on 2025-04-08 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_transaction', '0010_remove_nfttransaction_nft_id_and_more'),
        ('esc_wallet', '0005_delete_escrow'),
    ]

    operations = [
        migrations.CreateModel(
            name='EscrowTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_hash', models.CharField(db_index=True, max_length=200, unique=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('amount', models.BigIntegerField()),
                ('status', models.CharField(choices=[('HOLD', 'Hold'), ('COMPLETED', 'Completed'), ('RETURNED', 'Returned')], default='HOLD', max_length=20)),
                ('transfered_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_escrow_transactions', to='esc_wallet.wallet', verbose_name='Sender')),
                ('transfered_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_escrow_transactions', to='esc_wallet.wallet', verbose_name='Receiver')),
            ],
        ),
    ]
