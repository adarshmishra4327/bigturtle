# Generated by Django 3.0 on 2021-01-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0141_auto_20210122_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1611320161', max_length=200),
        ),
    ]