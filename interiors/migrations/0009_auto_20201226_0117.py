# Generated by Django 3.0 on 2020-12-26 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0008_auto_20201226_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 1, 17, 45, 22965), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_id',
            field=models.CharField(default='c0qNNa', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='timecreated',
            field=models.CharField(default='1608945465', max_length=200),
        ),
    ]
