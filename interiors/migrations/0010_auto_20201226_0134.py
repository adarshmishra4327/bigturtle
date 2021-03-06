# Generated by Django 3.0 on 2020-12-26 01:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0009_auto_20201226_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_type', models.CharField(choices=[('LIVING ROOM', 'LIVING ROOM'), ('KITCHEN', 'KITCHEN'), ('BATHROOM', 'BATHROOM'), ('BED ROOM', 'BED ROOM'), ('KIDS ROOM', 'KIDS ROOM')], max_length=200, verbose_name='Design Type')),
                ('name', models.CharField(max_length=200, verbose_name='Design Name')),
                ('summary', models.CharField(max_length=200, verbose_name='About Design(Few words)')),
                ('designer_name', models.CharField(max_length=200, verbose_name='Designer Name')),
                ('price', models.IntegerField(verbose_name='Starting Price(in Lakhs)')),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 1, 34, 14, 410235), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_id',
            field=models.CharField(default='WWTf5g', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='timecreated',
            field=models.CharField(default='1608946454', max_length=200),
        ),
    ]
