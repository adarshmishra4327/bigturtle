# Generated by Django 3.0 on 2021-01-22 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0036_auto_20210122_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 12, 56, 1, 138777), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='designgallery',
            name='designer_id',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Designer Id'),
        ),
        migrations.AlterField(
            model_name='portfoliobasic',
            name='timecreated',
            field=models.CharField(default='1611320161', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='timecreated',
            field=models.CharField(default='1611320161', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallerylinks',
            name='timecreated',
            field=models.CharField(default='1611320161', max_length=200),
        ),
    ]
