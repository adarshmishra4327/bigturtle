# Generated by Django 3.0 on 2021-01-18 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0124_auto_20210118_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1610942698', max_length=200),
        ),
    ]