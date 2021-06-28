from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
# Create your models here.


class Journals(models.Model):

    author = models.ForeignKey(
        "account.Account", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    journals_file = models.FileField(
        blank=True, null=True, verbose_name="Derginin Dosyasını Ekleyiniz")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    journals_image = models.FileField(
        blank=True, null=True, verbose_name="Dergiye Kapak Fotoğraf Ekleyiniz.")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
