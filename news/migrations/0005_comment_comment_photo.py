# Generated by Django 2.1.5 on 2021-05-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210527_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_photo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf'),
        ),
    ]
