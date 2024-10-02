from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name="Продукт", help_text="Введите название продукта", null=True, blank=True)
    description = models.TextField(verbose_name='Описание', help_text="Введите описание продукта", null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена',
                                help_text="Введите цену продукта")
