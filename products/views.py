from rest_framework import generics
from products.models import Products
from products.serializers import ProductsSerializer


class ProductsCreateAPIView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
