# Generated by Django 3.0 on 2020-11-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0053_auto_20201107_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604738806', max_length=200),
        ),
    ]