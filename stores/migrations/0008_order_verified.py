# Generated by Django 4.2 on 2023-06-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_category_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
