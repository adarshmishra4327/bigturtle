# Generated by Django 3.0 on 2020-11-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0060_auto_20201110_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic_information',
            name='price',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604993039', max_length=200),
        ),
    ]