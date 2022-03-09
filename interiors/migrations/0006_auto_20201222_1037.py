# Generated by Django 3.0 on 2020-12-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0005_auto_20201222_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_feedback',
            name='designer_name',
            field=models.CharField(default=1, max_length=200, verbose_name='Designer Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer_feedback',
            name='city',
            field=models.CharField(max_length=200, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='customer_feedback',
            name='feedback',
            field=models.CharField(max_length=200, verbose_name='Feedback'),
        ),
        migrations.AlterField(
            model_name='customer_feedback',
            name='location',
            field=models.CharField(max_length=200, verbose_name='Customer Location'),
        ),
        migrations.AlterField(
            model_name='customer_feedback',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Customer Name'),
        ),
        migrations.AlterField(
            model_name='customer_feedback',
            name='project_date',
            field=models.CharField(max_length=200, verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='customer_feedback',
            name='type_of_property',
            field=models.CharField(choices=[('1 BHK', '1 BHK'), ('2 BHK', '2 BHK'), ('3 BHK', '3 BHK'), ('4 BHK', '4 BHK'), ('5 BHK', '5 BHK'), ('6+ BHK', '6+ BHK'), ('INDEPENDENT HOUSE', 'INDEPENDENT HOUSE')], max_length=200, verbose_name='Type of Property'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='timecreated',
            field=models.CharField(default='1608633436', max_length=200),
        ),
    ]