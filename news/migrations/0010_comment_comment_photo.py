# Generated by Django 2.1.5 on 2021-06-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_news_favourite_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_photo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Yoruma Fotoğraf Ekleyin'),
        ),
    ]