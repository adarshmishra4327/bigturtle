# Generated by Django 3.0 on 2020-12-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0094_auto_20201210_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1608190649', max_length=200),
        ),
    ]
