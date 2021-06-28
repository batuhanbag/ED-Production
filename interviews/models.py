from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
# Create your models here.


class Interviews(models.Model):

    author = models.ForeignKey(
        "account.Account", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    interviews_content = RichTextField()
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    interviews_image = models.FileField(
        blank=True, null=True, verbose_name="Röportaj'a Kapak Fotoğrafı Ekleyiniz.")
    interviews_image2 = models.FileField(
        blank=True, null=True, verbose_name="Röportaj'a 2.Fotoğraf veya Video Ekleyiniz.")
    interviews_image3 = models.FileField(
        blank=True, null=True, verbose_name="Röportaj'a 3.Fotoğraf veya Video Ekleyiniz.")
    likes = models.ManyToManyField(
        "account.Account", related_name='likes_interviews', blank=True)
    favourite_interviews = models.ManyToManyField(
        "account.Account", related_name='favourite_interviews', blank=True)
    read = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def total_read(self):
        return self.read.count()

    def get_absolute_url(self):
        return reverse("interviews:detail", args=[self.id])

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    interviews = models.ForeignKey(Interviews, on_delete=models.CASCADE,
                                   verbose_name="Röportaj", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=256, verbose_name="Yorum")
    comment_photo = models.FileField(
        blank=True, null=True, verbose_name="Fotoğraf")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ["-comment_date"]
