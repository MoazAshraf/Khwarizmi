# Generated by Django 3.1.3 on 2020-11-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201127_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(max_length=64),
        ),
    ]
