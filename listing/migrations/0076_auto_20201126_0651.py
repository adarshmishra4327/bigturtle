# Generated by Django 3.0 on 2020-11-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0075_auto_20201125_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1606373505', max_length=200),
        ),
        migrations.AlterField(
            model_name='register',
            name='comment',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name='Email Address'),
        ),
    ]
