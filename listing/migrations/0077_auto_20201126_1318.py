# Generated by Django 3.0 on 2020-11-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0076_auto_20201126_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1606396704', max_length=200),
        ),
    ]
