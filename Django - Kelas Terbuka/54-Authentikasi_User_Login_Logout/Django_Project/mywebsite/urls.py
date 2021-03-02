from django.contrib import admin
from django.urls import path

from .import views

# app_name = "mywebsite"
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('user-area/', views.user_area, name='user_area'),
    path('logout/', views.logout, name='logout'),
    path('admin/', admin.site.urls),
]
