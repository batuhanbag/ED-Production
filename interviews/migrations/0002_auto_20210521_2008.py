# Generated by Django 2.1.5 on 2021-05-21 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='news',
            new_name='interviews',
        ),
    ]
