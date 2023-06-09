# Generated by Django 4.2 on 2023-06-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrents', '0014_alter_brand_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.ImageField(upload_to='slider')),
                ('title', models.CharField(max_length=255, null=True)),
                ('sub_title', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
