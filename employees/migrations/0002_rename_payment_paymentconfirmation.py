# Generated by Django 5.0.6 on 2024-06-21 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payment',
            new_name='PaymentConfirmation',
        ),
    ]
