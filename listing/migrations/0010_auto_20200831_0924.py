# Generated by Django 3.0 on 2020-08-31 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_complete_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Complete_details',
            new_name='Property',
        ),
    ]
