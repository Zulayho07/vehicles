from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Brand, Car
from .serializers import BrandSerializer, CarSerializer


class BrandListCreateAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarListCreateAPIView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()

        brand_id = self.request.query_params.get('brand_id')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if brand_id is not None:
            queryset = queryset.filter(brand_id=brand_id)

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)

        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer