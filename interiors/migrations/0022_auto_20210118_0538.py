# Generated by Django 3.0 on 2021-01-18 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0021_auto_20210118_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliobasic',
            name='aboutyourself',
            field=models.CharField(default=1, max_length=500, verbose_name='About Designer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliobasic',
            name='designer_id',
            field=models.CharField(default=1, max_length=200, verbose_name='Designer Id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliobasic',
            name='experience',
            field=models.IntegerField(default=1, verbose_name='Experience (In Years)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliobasic',
            name='name',
            field=models.CharField(default=1, max_length=200, verbose_name='Designer Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='designer_id',
            field=models.CharField(max_length=200, verbose_name='Designer Id'),
        ),
        migrations.AlterField(
            model_name='customer_review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 5, 38, 33, 131417), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='designs',
            name='design_id',
            field=models.CharField(default='DESN0uRwuO', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portfoliobasic',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 5, 38, 33, 127752), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfoliobasic',
            name='timecreated',
            field=models.CharField(default='1610948313', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='portfolio_id',
            field=models.CharField(max_length=200, verbose_name='Portfolio Id'),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='timecreated',
            field=models.CharField(default='1610948313', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallerylinks',
            name='timecreated',
            field=models.CharField(default='1610948313', max_length=200),
        ),
    ]
