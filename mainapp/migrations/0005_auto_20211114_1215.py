# Generated by Django 3.2.4 on 2021-11-14 12:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_property_hall'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='design',
            new_name='Agriculture',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='bathroom',
            new_name='Four_BHK',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='hall',
            new_name='One_BHK',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='room',
            new_name='Tree_BHK',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='kitchen',
            new_name='Two_BHK',
        ),
        migrations.AddField(
            model_name='property',
            name='NA_plot',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='property/bathroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='Villa',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='property/design'),
            preserve_default=False,
        ),
    ]
