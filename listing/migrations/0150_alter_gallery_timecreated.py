# Generated by Django 3.2.9 on 2021-11-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0149_alter_gallery_timecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1636208648', max_length=200),
        ),
    ]
