from django.contrib import admin
from django.urls import path, include

from . import views
from about import views as aboutViews
from blog import views as blogViews

urlpatterns = [
	path('', views.index),
	path('blog/', include('blog.urls')),
	path('about/', aboutViews.index),
    path('admin/', admin.site.urls),
]
