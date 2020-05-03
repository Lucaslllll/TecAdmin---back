# Generated by Django 2.2.4 on 2020-05-03 22:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200502_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='techay_user',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='user_client',
            name='link_site',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='vote',
            name='images',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='foto'),
        ),
    ]
