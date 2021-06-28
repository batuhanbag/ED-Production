from django.contrib import admin
from django.urls import path
from . import views
app_name = "news"

urlpatterns = [


    path('', views.news, name="news"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('like/<int:id>', views.like_post_news, name="like_post"),
    path('comment/<int:id>', views.addComment, name="comment"),
    path('favourite_post/<int:id>', views.favourite_post, name="favourite_post"),

    # path('comment/<int:id>',views.addComment,name = "comment"),

]
