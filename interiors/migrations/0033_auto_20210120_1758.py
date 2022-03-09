# Generated by Django 3.0 on 2021-01-20 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0032_auto_20210120_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designer_id', models.CharField(max_length=200, verbose_name='Designer Id')),
                ('design_image', models.ImageField(upload_to='images/image_1/')),
                ('design_type', models.CharField(choices=[('LIVING ROOM', 'LIVING ROOM'), ('MODULAR KITCHEN', 'MODULAR KITCHEN'), ('BATHROOM', 'BATHROOM'), ('BED ROOM', 'BED ROOM'), ('KIDS ROOM', 'KIDS ROOM')], max_length=200, verbose_name='Design Type')),
                ('price', models.IntegerField(verbose_name='Starting Price(in lakhs)')),
            ],
        ),
        migrations.AlterField(
            model_name='customer_review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 17, 58, 32, 748078), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfoliobasic',
            name='timecreated',
            field=models.CharField(default='1611165512', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='timecreated',
            field=models.CharField(default='1611165512', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliogallerylinks',
            name='timecreated',
            field=models.CharField(default='1611165512', max_length=200),
        ),
    ]