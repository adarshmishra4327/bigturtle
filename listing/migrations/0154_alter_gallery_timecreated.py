# Generated by Django 3.2.9 on 2021-11-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0153_alter_gallery_timecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1636294250', max_length=200),
        ),
    ]
