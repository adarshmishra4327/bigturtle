# Generated by Django 3.0 on 2020-08-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_auto_20200829_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='property_gallery',
            field=models.FileField(blank=True, upload_to='property_gallery'),
        ),
    ]