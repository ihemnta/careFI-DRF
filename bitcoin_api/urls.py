from django.urls import path
from . import views



urlpatterns = [
    path('ping/', views.ping.as_view()),
    path('current-price/', views.fetchPrice, name="fetchPrice"),
    path('price-history/', views.BitcoinListAPIView.as_view()),
]