# Generated by Django 5.0.6 on 2024-06-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_delete_partnerlocation_warehouse_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='category',
            field=models.CharField(choices=[('Entrepôt', 'Entrepôt'), ('Supermarché', 'Supermarché'), ('Centre commercial', 'Centre commercial')], max_length=20),
        ),
    ]
