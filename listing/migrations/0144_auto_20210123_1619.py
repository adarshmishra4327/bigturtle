# Generated by Django 3.0 on 2021-01-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0143_auto_20210123_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1611418768', max_length=200),
        ),
    ]
