# pages/urls.py
from django.urls import path

from .views import HomePageView, AcercadePageView

urlpatterns = [
    path('acercade/', AcercadePageView.as_view(), name='acercade'), # new 
    path('', HomePageView.as_view(), name='home'),
]