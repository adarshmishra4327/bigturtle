# Generated by Django 3.0 on 2020-08-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.TextField(default=None),
        ),
    ]