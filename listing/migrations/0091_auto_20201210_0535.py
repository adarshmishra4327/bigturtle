# Generated by Django 3.0 on 2020-12-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0090_auto_20201210_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1607578531', max_length=200),
        ),
    ]
