# Generated by Django 3.0 on 2020-10-31 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0026_auto_20201013_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200)),
                ('thumbnail', models.CharField(max_length=200)),
                ('image_1', models.CharField(max_length=200)),
                ('image_2', models.CharField(max_length=200)),
                ('image_3', models.CharField(max_length=200)),
                ('image_4', models.CharField(max_length=200)),
                ('image_5', models.CharField(max_length=200)),
                ('timecreated', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='property_gallery_1',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='property_gallery_2',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='property_gallery_3',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='property_gallery_4',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='property_gallery_5',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='property_thumbnail',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='basic_info',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='details',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='features',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='location',
        ),
        migrations.AddField(
            model_name='basic_information',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='Basic', to='listing.Listing'),
        ),
        migrations.AddField(
            model_name='details',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='Details', to='listing.Listing'),
        ),
        migrations.AddField(
            model_name='features',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='Features', to='listing.Listing'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image_1',
            field=models.ImageField(default=1, upload_to='images/image_1/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='image_2',
            field=models.ImageField(default=1, upload_to='images/image_2/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='image_3',
            field=models.ImageField(default=1, upload_to='images/image_3/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='image_4',
            field=models.ImageField(default=1, upload_to='images/image_4/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='image_5',
            field=models.ImageField(default=1, upload_to='images/image_5/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='property_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='images/thumbnail/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='timecreated',
            field=models.CharField(default='1604128639', max_length=200),
        ),
        migrations.AddField(
            model_name='location',
            name='listing',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='Location', to='listing.Listing'),
        ),
    ]