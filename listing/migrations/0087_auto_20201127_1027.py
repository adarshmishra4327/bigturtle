# Generated by Django 3.0 on 2020-11-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0086_auto_20201127_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_listings',
            name='location',
            field=models.CharField(choices=[('Any_Location', 'Any_Location'), ('BANGALORE', 'BANGALORE')], max_length=50, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1606472871', max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='City',
            field=models.CharField(choices=[('BANGALORE', 'BANGALORE')], max_length=20, verbose_name='City'),
        ),
    ]
