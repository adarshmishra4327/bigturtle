# Generated by Django 3.0 on 2020-11-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0031_auto_20201031_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='description',
            field=models.CharField(default=None, max_length=500, null=True, verbose_name='Property Description'),
        ),
        migrations.AddField(
            model_name='details',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Property Name'),
        ),
        migrations.AddField(
            model_name='details',
            name='price',
            field=models.CharField(default=1, max_length=50, verbose_name='Property Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='space',
            field=models.IntegerField(default=1, verbose_name='Property Space(Sqft)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='status',
            field=models.CharField(choices=[('FOR SALE', 'For Sale'), ('UNDERCONSTRUCTION', 'Underconstruction'), ('LEASED', 'Leased'), ('SOLD', 'Sold'), ('SPECIAL OFFER', 'Special Offer'), ('NEW ADDITION', 'New Addition'), ('RENTAL', 'Rental'), ('REDUCED', 'Reduced')], default=1, max_length=20, verbose_name='Property Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='type',
            field=models.CharField(choices=[('HOUSE', 'House'), ('APARTMENT', 'Apartment'), ('CONDO', 'Condo'), ('VILLA', 'Villa'), ('DUPLEX', 'Duplex')], default=1, max_length=20, verbose_name='Property Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='video',
            field=models.URLField(blank=True, verbose_name='Property Video'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604211055', max_length=200),
        ),
    ]