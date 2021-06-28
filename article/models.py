from django.db import models
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.files import FileField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.shortcuts import reverse
# Create your models here.


class Article(models.Model):

    category = (
        ('Yapay Zeka', 'Yapay Zeka'),
        ('Yazılım', 'Yazılım'),
        ('Kripto Para', 'Kripto Para'),
        ('Donanım', 'Donanım'),
    )

    author = models.ForeignKey(
        "account.Account", on_delete=models.CASCADE, verbose_name="Yazar ")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextUploadingField()
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(
        blank=True, null=True, verbose_name="Makaleye Fotoğraf Ekleyin")
    article_category = models.CharField(
        max_length=20, choices=category, default='Yazılım', verbose_name="Makale Kategori")
    likes = models.ManyToManyField(
        "account.Account", related_name='likes', blank=True)
    favourite = models.ManyToManyField(
        "account.Account", related_name='favourite', blank=True)
    read = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

    def total_likes(self):
        return self.likes.count()

    def total_read(self):
        return self.read.count()

    def get_absolute_url(self):
        return reverse("article:detail", args=[self.id])


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']


class sendArticle(models.Model):
    name = CharField(verbose_name="İsim", max_length=50)
    email = EmailField(verbose_name="E-mail")
    article_file = FileField(verbose_name="Makale Dosyası")
    article_image = FileField(verbose_name="Makale Resimi")
    send_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Yollanma Tarihi")

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-send_date']
