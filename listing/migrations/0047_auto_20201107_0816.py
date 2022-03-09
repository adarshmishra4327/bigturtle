# Generated by Django 3.0 on 2020-11-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0046_auto_20201107_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='status',
            field=models.CharField(choices=[('FOR SALE', 'For Sale'), ('READY TO MOVE', 'Ready to Move'), ('UNDERCONSTRUCTION', 'Underconstruction'), ('LEASED', 'Leased'), ('SOLD', 'Sold'), ('SPECIAL OFFER', 'Special Offer'), ('NEW ADDITION', 'New Addition'), ('RENTAL', 'Rental'), ('REDUCED', 'Reduced')], max_length=20, verbose_name='Property Status'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604737013', max_length=200),
        ),
    ]