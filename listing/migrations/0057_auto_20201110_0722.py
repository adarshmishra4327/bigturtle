# Generated by Django 3.0 on 2020-11-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0056_auto_20201107_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604992968', max_length=200),
        ),
    ]
