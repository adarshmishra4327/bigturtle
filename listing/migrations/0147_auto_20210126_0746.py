# Generated by Django 3.0 on 2021-01-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0146_auto_20210125_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1611647189', max_length=200),
        ),
    ]
