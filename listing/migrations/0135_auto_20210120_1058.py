# Generated by Django 3.0 on 2021-01-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0134_auto_20210120_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1611140281', max_length=200),
        ),
    ]