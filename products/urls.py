from django.urls import path
from products.apps import ProductsConfig
# from products.views import add
from products.views import ProductsCreateAPIView, ProductsListAPIView, AddListView

app_name = ProductsConfig.name

urlpatterns = [
    path("", AddListView.as_view(), name="add_products"),
    path("products/create/", ProductsCreateAPIView.as_view(), name="products_create"),
    path("products/", ProductsListAPIView.as_view(), name="products_list"),
    # path('', add, name='add_product'),
    # path('add/', add, name='add_product'),
]
