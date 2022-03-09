# Generated by Django 3.0 on 2020-10-31 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0030_auto_20201031_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_information',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='basic', to='listing.Listing'),
        ),
        migrations.AlterField(
            model_name='details',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='listing.Listing'),
        ),
        migrations.AlterField(
            model_name='features',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='listing.Listing'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604139885', max_length=200),
        ),
        migrations.AlterField(
            model_name='gallery_links',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='gallery_links', to='listing.Listing'),
        ),
        migrations.AlterField(
            model_name='location',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='listing.Listing'),
        ),
    ]
