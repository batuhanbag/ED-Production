from django import forms
from .models import Article, sendArticle


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "article_image"]


class ArticleSend(forms.ModelForm):

    class Meta:
        model = sendArticle
        fields = ["name", "email", "article_file", "article_image"]
