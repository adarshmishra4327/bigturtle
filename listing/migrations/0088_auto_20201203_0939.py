# Generated by Django 3.0 on 2020-12-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0087_auto_20201127_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_listings',
            name='builder',
            field=models.CharField(choices=[('Any Builder', 'Any Builder'), ('Amsa', 'Amsa'), ('Shobha', 'Shobha'), ('Sarita', 'Sarita')], max_length=50, verbose_name='Builder'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1606988352', max_length=200),
        ),
    ]
