from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Brand, Car, Comment
from .serializers import BrandSerializer, CarSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly



class BrandApiViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CarAPIViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

#
# class BrandListCreateAPIView(ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#
# class BrandRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#
# class CarListCreateAPIView(ListCreateAPIView):
#     serializer_class = CarSerializer
#
#     def get_queryset(self):
#         queryset = Car.objects.all()
#
#         brand_id = self.request.query_params.get('brand_id')
#         min_price = self.request.query_params.get('min_price')
#         max_price = self.request.query_params.get('max_price')
#
#         if brand_id is not None:
#             queryset = queryset.filter(brand_id=brand_id)
#
#         if min_price is not None:
#             queryset = queryset.filter(price__gte=min_price)
#
#         if max_price is not None:
#             queryset = queryset.filter(price__lte=max_price)
#
#         return queryset
#
#
# class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = [IsAdminOrReadOnly]
#
#
#
# class CommentListCreateAPIView(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#
#     def perform_create(self, serializer):
#         serializer.validated_date['user'] = self.request.user
#         serializer.validated_date['car_id'] = self.kwargs.get('car_id')
#         serializer.save()
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context.update({"request": self.request})
#         return context
#
#
#
# class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthorOrReadOnly]
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context.update({"request": self.request})
#         return context
#



