# Generated by Django 3.1.3 on 2020-11-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0004_auto_20201126_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
