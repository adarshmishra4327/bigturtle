# Generated by Django 3.0 on 2021-01-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0136_auto_20210120_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1611140661', max_length=200),
        ),
    ]
