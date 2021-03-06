# Generated by Django 2.1.5 on 2021-06-12 11:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210529_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_photo',
        ),
        migrations.RemoveField(
            model_name='news',
            name='favourite_news',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_image2',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_image3',
        ),
        migrations.RemoveField(
            model_name='news',
            name='read',
        ),
        migrations.AlterField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likesnew', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Habere Fotoğraf Ekleyiniz.'),
        ),
    ]
