from django.urls import path
from .views import IGRamDownloadView
urlpatterns = [
    path('',IGRamDownloadView.as_view(),name = "instagram"),
]
