from django.contrib import admin
from django.urls import path

from products.views import ProductsCreateAPIView, ProductsListAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/create/", ProductsCreateAPIView.as_view(), name="products-create"),
    path("products/", ProductsListAPIView.as_view(), name="products-list"),
]
