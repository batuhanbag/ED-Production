from django.contrib import admin
from django.urls import path
from . import views
app_name = "journals"

urlpatterns = [


    path('', views.journals, name="journals"),




]
