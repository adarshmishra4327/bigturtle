# Generated by Django 3.0 on 2021-01-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0137_auto_20210120_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1611165512', max_length=200),
        ),
    ]