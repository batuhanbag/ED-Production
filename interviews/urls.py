from django.contrib import admin
from django.urls import path
from . import views
app_name = "interviews"

urlpatterns = [


    path('', views.interviews, name="interviews"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('comment/<int:id>', views.addComment, name="comment"),
    path('like/<int:id>', views.like_post_interviews,
         name="like_post_interviews"),
    path('favourite_post/<int:id>', views.favourite_post, name="favourite_post"),
    # path('comment/<int:id>',views.addComment,name = "comment"),

]
