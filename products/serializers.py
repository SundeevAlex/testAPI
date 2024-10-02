from rest_framework.serializers import ModelSerializer
from products.models import Products
from products.validators import NameValidator, PriceValidator


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        validators = [NameValidator(field='name'), PriceValidator(field='price')]
