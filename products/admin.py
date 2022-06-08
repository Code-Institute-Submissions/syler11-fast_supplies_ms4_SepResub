"""
Imports
"""
from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    Product admin  model class
    """
    list_display = (
        'sku',
        'name',
        'category',
        'quantity',
        'price',
        'rating',
        'image',
    )
    list_filter = (
        'sku',
        'name',
        'category',
        'price',
    )
    search_fields = (
        'sku',
        'name',
        'category',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin model class
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
