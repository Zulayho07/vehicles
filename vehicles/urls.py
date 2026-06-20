from django.urls import path
from .views import (BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView,
    CarListCreateAPIView, CarRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('brands/', BrandListCreateAPIView.as_view()),
    path('brands/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view()),

    path('cars/', CarListCreateAPIView.as_view()),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view()),
]