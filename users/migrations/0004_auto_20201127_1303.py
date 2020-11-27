# Generated by Django 3.1.3 on 2020-11-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201127_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(max_length=128),
        ),
    ]
