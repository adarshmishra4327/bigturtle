# Generated by Django 3.0 on 2020-11-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0043_auto_20201107_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_information',
            name='description',
            field=models.CharField(default=None, max_length=500, null=True, verbose_name='Property Description'),
        ),
        migrations.AddField(
            model_name='basic_information',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Property Name'),
        ),
        migrations.AddField(
            model_name='basic_information',
            name='price',
            field=models.CharField(default=1, max_length=50, verbose_name='Property Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='space',
            field=models.IntegerField(default=1, verbose_name='Property Space(Sqft)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='status',
            field=models.CharField(choices=[('FOR SALE', 'For Sale'), ('UNDERCONSTRUCTION', 'Underconstruction'), ('LEASED', 'Leased'), ('SOLD', 'Sold'), ('SPECIAL OFFER', 'Special Offer'), ('NEW ADDITION', 'New Addition'), ('RENTAL', 'Rental'), ('REDUCED', 'Reduced')], default=1, max_length=20, verbose_name='Property Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='type',
            field=models.CharField(choices=[('COMMERCIAL', 'Commercial'), ('RESIDENTIAL', 'Residential'), ('APARTMENT', 'Apartment'), ('BEACH HOUSE', 'Beach House'), ('VILLA', 'Villa'), ('DUPLEX', 'Duplex')], default=1, max_length=20, verbose_name='Property Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='video',
            field=models.URLField(blank=True, verbose_name='Property Video'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='status',
            field=models.CharField(choices=[('FOR SALE', 'For Sale'), ('UNDERCONSTRUCTION', 'Underconstruction'), ('LEASED', 'Leased'), ('SOLD', 'Sold'), ('SPECIAL OFFER', 'Special Offer'), ('NEW ADDITION', 'New Addition'), ('RENTAL', 'Rental'), ('REDUCED', 'Reduced')], max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604736038', max_length=200),
        ),
    ]