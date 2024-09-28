from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name="Продукт", help_text="Введите название продукта")
    description = models.TextField(verbose_name='Описание', help_text="Введите описание продукта")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Цена',
                                help_text="Введите цену продукта")
