# Generated by Django 3.2.9 on 2021-11-07 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0054_auto_20211107_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 14, 32, 59, 122366), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfoliobasic',
            name='timecreated',
            field=models.CharField(default='1636295579', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='timecreated',
            field=models.CharField(default='1636295579', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallerylinks',
            name='timecreated',
            field=models.CharField(default='1636295579', max_length=200),
        ),
    ]
