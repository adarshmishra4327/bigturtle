# Generated by Django 3.0 on 2020-11-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0039_auto_20201104_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_information',
            name='approved_by',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Approved by'),
        ),
        migrations.AddField(
            model_name='basic_information',
            name='available_units',
            field=models.IntegerField(default=1, verbose_name='Available Units'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='commencement_certificate',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default=1, max_length=20, verbose_name='Commencement Certificate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='launch_year',
            field=models.IntegerField(default=1, verbose_name='Launch Year'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='project_area',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Property Area'),
        ),
        migrations.AddField(
            model_name='basic_information',
            name='total_no_of_floors',
            field=models.IntegerField(default=1, verbose_name='Total No of Floors'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='total_no_of_towers',
            field=models.IntegerField(default=1, verbose_name='Total No of Towers'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic_information',
            name='total_units',
            field=models.IntegerField(default=1, verbose_name='Total Units'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='property_id',
            field=models.CharField(max_length=200, verbose_name='RERA Id'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604735226', max_length=200),
        ),
    ]
