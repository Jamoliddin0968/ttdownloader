"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path,include
from .functions import TTDonwloadView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tiktok/',TTDonwloadView.as_view(),name = "tiktok"),
    path('instagram/',include('instagram.urls')),  
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)