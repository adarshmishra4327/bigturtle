# Generated by Django 3.2.4 on 2021-11-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0163_alter_gallery_timecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1638095985', max_length=200),
        ),
    ]