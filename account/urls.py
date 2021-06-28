from django.contrib import admin
from django.urls import path
from . import views
app_name = "account"

urlpatterns = [
    path('register/', views.registration_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('account/', views.account_view, name="account"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('deleteuser/', views.delete_user, name="delete_user"),



]
