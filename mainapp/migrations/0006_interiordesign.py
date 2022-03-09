# Generated by Django 3.2.4 on 2021-11-14 12:15

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20211114_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interiordesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designer_id', models.CharField(max_length=122)),
                ('Designer_name', models.CharField(max_length=122)),
                ('About_Designer', models.CharField(max_length=122)),
                ('Expreance', models.CharField(max_length=122)),
                ('Project_completed', models.CharField(max_length=122)),
                ('propertyarea', models.CharField(max_length=122)),
                ('Award', models.CharField(max_length=122)),
                ('Livingroom', models.ImageField(upload_to=mainapp.models.user_directory_path)),
                ('Kitchen', models.ImageField(upload_to='property/kitchen')),
                ('Master_bedroom', models.ImageField(upload_to='property/room')),
                ('Guest_bedroom', models.ImageField(upload_to='property/bathroom')),
                ('Balconies', models.ImageField(upload_to='property/design')),
                ('Bathroom', models.ImageField(upload_to='property/design')),
                ('Miscellaneous', models.ImageField(upload_to='property/design')),
            ],
        ),
    ]