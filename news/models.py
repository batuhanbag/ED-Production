from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse


class News(models.Model):

    author = models.ForeignKey(
        "account.Account", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    news_image = models.FileField(
        blank=True, null=True, verbose_name="Habere Fotoğraf Ekleyiniz.")
    favourite_news = models.ManyToManyField(
        "account.Account", related_name='favourite_news', blank=True)
    likes = models.ManyToManyField(
        "account.Account", related_name='likesnew', blank=True)
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
        return reverse("news:detail", args=[self.id])


class Comment(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, verbose_name="Haber", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=256, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ["-comment_date"]
