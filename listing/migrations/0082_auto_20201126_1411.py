# Generated by Django 3.0 on 2020-11-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0081_auto_20201126_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1606399871', max_length=200),
        ),
    ]
