# Generated by Django 4.2 on 2023-07-10 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrents', '0023_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
