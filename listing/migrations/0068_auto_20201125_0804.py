# Generated by Django 3.0 on 2020-11-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0067_auto_20201125_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='converted_price',
            field=models.IntegerField(default=1, verbose_name='Price in Lakhs'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1606291435', max_length=200),
        ),
    ]
