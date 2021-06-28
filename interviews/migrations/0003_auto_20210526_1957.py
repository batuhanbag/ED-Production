# Generated by Django 2.1.5 on 2021-05-26 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interviews', '0002_auto_20210521_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviews',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite_interviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interviews',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes_interviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interviews',
            name='read',
            field=models.IntegerField(default=0),
        ),
    ]