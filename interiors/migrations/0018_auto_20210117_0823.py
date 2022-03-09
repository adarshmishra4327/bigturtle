# Generated by Django 3.0 on 2021-01-17 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0017_auto_20201226_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='online_consultation',
            name='OTP',
        ),
        migrations.AddField(
            model_name='online_consultation',
            name='state',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default=1, max_length=200, verbose_name='State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='online_consultation',
            name='whatsapp',
            field=models.BooleanField(default=None, null=True, verbose_name='Send WhatsApp Update'),
        ),
        migrations.AddField(
            model_name='online_consultation',
            name='zipcode',
            field=models.CharField(default=1, max_length=200, verbose_name='Zip Code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='designer_id',
            field=models.CharField(default='DEZINEReROwMZ', max_length=200, verbose_name='Designer id'),
        ),
        migrations.AlterField(
            model_name='customer_review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 8, 23, 19, 343984), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='designs',
            name='design_id',
            field=models.CharField(default='DESNwYcUNf', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 8, 23, 19, 340947), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_id',
            field=models.CharField(default='PORTeDqY3Z', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='timecreated',
            field=models.CharField(default='1610871799', max_length=200),
        ),
    ]