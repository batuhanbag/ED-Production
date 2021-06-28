from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [

    path('detail/<int:id>', views.detail, name="detail"),
    path('', views.articles, name="articles"),
    path('comment/<int:id>', views.addComment, name="comment"),
    path('like/<int:id>', views.like_post_article, name="like_post"),
    path('favourite_post/<int:id>', views.favourite_post, name="favourite_post"),
    path('favourite_list/', views.favourite_list, name="favourite_list"),
]
