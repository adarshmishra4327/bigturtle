# Generated by Django 3.2.9 on 2021-11-07 14:10

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20211107_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='hall',
            field=models.ImageField(upload_to=mainapp.models.user_directory_path),
        ),
    ]
