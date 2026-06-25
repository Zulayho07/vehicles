from django.urls import path, include
# from .views import (BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView,
#                     CarListCreateAPIView, CarRetrieveUpdateDestroyAPIView, CommentListCreateAPIView,
#                     CommentRetrieveUpdateDestroyAPIView)
from rest_framework.routers import SimpleRouter

from .views import BrandApiViewSet, CarAPIViewSet


router=SimpleRouter()
router.register('categories', BrandApiViewSet)
router.register('cars', CarAPIViewSet)


urlpatterns = [
    path('', include(router.urls))

    # path('brands/', BrandListCreateAPIView.as_view()),
    # path('brands/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view()),
    #
    # path('cars/', CarListCreateAPIView.as_view()),
    # path('cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view()),
    #
    # path('comments/', CommentListCreateAPIView.as_view()),
    # path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
]
