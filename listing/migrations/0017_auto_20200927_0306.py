# Generated by Django 3.0 on 2020-09-27 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0016_auto_20200912_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_information',
            name='price',
            field=models.IntegerField(verbose_name='Property Price'),
        ),
    ]