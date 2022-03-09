# Generated by Django 3.0 on 2021-01-18 05:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0020_auto_20210118_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliogallerylinks',
            name='interior',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='portfoliogallerylinks', to='interiors.Interior'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='designer_id',
            field=models.CharField(default='DEZINERjJBNR6', max_length=200, verbose_name='Designer id'),
        ),
        migrations.AlterField(
            model_name='customer_review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 5, 25, 42, 398807), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='designs',
            name='design_id',
            field=models.CharField(default='DESNjsY2Pl', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portfoliobasic',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 5, 25, 42, 395101), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfoliobasic',
            name='timecreated',
            field=models.CharField(default='1610947542', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='portfolio_id',
            field=models.CharField(default='PORT9DBqBV', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='timecreated',
            field=models.CharField(default='1610947542', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallerylinks',
            name='timecreated',
            field=models.CharField(default='1610947542', max_length=200),
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]