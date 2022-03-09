# Generated by Django 3.2.9 on 2021-11-07 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0047_auto_20211107_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 13, 40, 42, 242637), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfoliobasic',
            name='timecreated',
            field=models.CharField(default='1636292442', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='timecreated',
            field=models.CharField(default='1636292442', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallerylinks',
            name='timecreated',
            field=models.CharField(default='1636292442', max_length=200),
        ),
    ]