from rest_framework import generics
from products.models import Products
from products.serializers import ProductsSerializer
from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy


class ProductsCreateAPIView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class AddListView(ListView):
    model = Products

    def get_queryset(self):
        queryset = Products.objects.all()
        return queryset
