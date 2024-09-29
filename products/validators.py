from rest_framework.serializers import ValidationError


class NameValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not dict(value).get(self.field):
            raise ValidationError('Поле "Название продукта" не может быть пустым!')


class PriceValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if int(dict(value).get(self.field)) < 0:
            raise ValidationError('Цена не может быть отрицательной!')
