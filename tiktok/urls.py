from django.urls import path
from .views import TTDonwloadView
urlpatterns = [
    path('',TTDonwloadView.as_view(),name = "tiktok"),
]
