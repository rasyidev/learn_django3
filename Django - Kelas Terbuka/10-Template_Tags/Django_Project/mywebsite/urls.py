from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('', views.index),
	path('blog/', views.blog),
	path('contact/', views.contact),
	path('about/', views.about),
    path('admin/', admin.site.urls),
]
