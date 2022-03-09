# Generated by Django 3.0 on 2020-11-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0054_auto_20201107_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='type',
            new_name='propertytype',
        ),
        migrations.AlterField(
            model_name='basic_information',
            name='propertytype',
            field=models.CharField(choices=[('COMMERCIAL', 'Commercial'), ('RESIDENTIAL', 'Residential'), ('APARTMENT', 'Apartment'), ('BEACH HOUSE', 'Beach House'), ('VILLA', 'Villa'), ('DUPLEX', 'Duplex')], max_length=20, verbose_name='PropertyType'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604738973', max_length=200),
        ),
    ]
