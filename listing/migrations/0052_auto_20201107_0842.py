# Generated by Django 3.0 on 2020-11-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0051_auto_20201107_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604738579', max_length=200),
        ),
    ]
