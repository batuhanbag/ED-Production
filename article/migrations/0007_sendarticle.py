# Generated by Django 2.1.5 on 2021-05-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_read'),
    ]

    operations = [
        migrations.CreateModel(
            name='sendArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('article_file', models.FileField(upload_to='', verbose_name='Makale Dosyası')),
                ('article_image', models.FileField(upload_to='', verbose_name='Makale Resimi')),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='Yollanma Tarihi')),
            ],
            options={
                'ordering': ['-send_date'],
            },
        ),
    ]
