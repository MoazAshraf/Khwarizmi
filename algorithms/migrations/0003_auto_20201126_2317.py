# Generated by Django 3.1.3 on 2020-11-26 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algorithm',
            old_name='content',
            new_name='description',
        ),
    ]
