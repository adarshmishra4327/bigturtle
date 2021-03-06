# Generated by Django 3.0 on 2020-08-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0005_auto_20200829_0549'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Features',
        ),
        migrations.AddField(
            model_name='details',
            name='bathrooms',
            field=models.IntegerField(default=None, verbose_name='No of Bathrooms'),
        ),
        migrations.AddField(
            model_name='details',
            name='beds',
            field=models.IntegerField(default=None, verbose_name='No of Beds'),
        ),
        migrations.AddField(
            model_name='details',
            name='condition',
            field=models.CharField(choices=[('NEW', 'New'), ('OLD', 'Old')], default='New', max_length=20, verbose_name='Property Condition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='property_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='details',
            name='year_built',
            field=models.IntegerField(default=None, verbose_name='Year Built'),
        ),
    ]
