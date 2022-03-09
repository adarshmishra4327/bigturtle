# Generated by Django 3.0 on 2020-08-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0011_auto_20200831_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='Basic_Information',
        ),
        migrations.RemoveField(
            model_name='property',
            name='Details',
        ),
        migrations.RemoveField(
            model_name='property',
            name='Features',
        ),
        migrations.RemoveField(
            model_name='property',
            name='Gallery',
        ),
        migrations.RemoveField(
            model_name='property',
            name='Location',
        ),
        migrations.AddField(
            model_name='property',
            name='basic_information',
            field=models.ManyToManyField(to='listing.Basic_Information'),
        ),
        migrations.AddField(
            model_name='property',
            name='details',
            field=models.ManyToManyField(to='listing.Details'),
        ),
        migrations.AddField(
            model_name='property',
            name='features',
            field=models.ManyToManyField(to='listing.Features'),
        ),
        migrations.AddField(
            model_name='property',
            name='gallery',
            field=models.ManyToManyField(to='listing.Gallery'),
        ),
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.ManyToManyField(to='listing.Location'),
        ),
    ]
