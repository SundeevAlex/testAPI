from django.contrib import admin
from .models import Products


@admin.register(Products)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)
    search_fields = ('name', 'description', 'price',)
    list_filter = ('name', 'description', 'price',)
