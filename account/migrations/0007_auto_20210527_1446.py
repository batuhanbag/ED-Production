# Generated by Django 2.1.5 on 2021-05-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210527_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_avatar',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf ekle'),
        ),
    ]
