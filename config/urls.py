"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tiktok/',include('tiktok.urls')),
    path('instagram/',include('instagram.urls')),  
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)