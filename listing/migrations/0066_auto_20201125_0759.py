# Generated by Django 3.0 on 2020-11-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0065_auto_20201122_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='mortgage',
            field=models.IntegerField(default=None, null=True, verbose_name='Estimated Mortgage'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1606291178', max_length=200),
        ),
    ]
