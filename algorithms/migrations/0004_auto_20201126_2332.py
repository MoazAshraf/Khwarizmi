# Generated by Django 3.1.3 on 2020-11-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0003_auto_20201126_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
