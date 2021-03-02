from django.contrib import admin
from django.urls import path

from .import views

# app_name = "mywebsite"
urlpatterns = [
    path('login/', views.index, name='login'),
    path('logout/', views.logout, name='logout'),
    path('admin/', admin.site.urls),
]
