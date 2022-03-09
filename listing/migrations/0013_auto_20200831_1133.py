# Generated by Django 3.0 on 2020-08-31 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0012_auto_20200831_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basic_information',
            old_name='property_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='basic_information',
            old_name='property_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='basic_information',
            old_name='property_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='basic_information',
            old_name='property_space',
            new_name='space',
        ),
        migrations.RenameField(
            model_name='basic_information',
            old_name='property_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='basic_information',
            old_name='property_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='basic_information',
            old_name='property_video',
            new_name='video',
        ),
    ]