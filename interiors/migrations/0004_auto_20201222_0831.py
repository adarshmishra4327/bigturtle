# Generated by Django 3.0 on 2020-12-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0003_auto_20201222_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='timecreated',
            field=models.CharField(default='1608625903', max_length=200),
        ),
    ]