# Generated by Django 3.0 on 2020-11-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0036_auto_20201103_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_links',
            name='status',
            field=models.CharField(choices=[('FOR SALE', 'For Sale'), ('UNDERCONSTRUCTION', 'Underconstruction'), ('LEASED', 'Leased'), ('SOLD', 'Sold'), ('SPECIAL OFFER', 'Special Offer'), ('NEW ADDITION', 'New Addition'), ('RENTAL', 'Rental'), ('REDUCED', 'Reduced')], default=1, max_length=50, verbose_name='Status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604479574', max_length=200),
        ),
    ]