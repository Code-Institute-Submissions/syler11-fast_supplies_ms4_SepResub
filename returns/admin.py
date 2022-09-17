"""
Imports
"""
from django.contrib import admin
from .models import Returns

# Register your models here.


class ReturnsAdmin(admin.ModelAdmin):
    """
    Favourites admin  model class
    """
    list_display = (
        'username',
        'return_reason',
        'return_request_date',
    )
    list_filter = (
        'username',
        'return_reason',
        'return_request_date',
    )
    search_fields = (
       'username',
       'return_reason',
        'return_request_date',
    )

    ordering = ('username',)


admin.site.register(Returns, ReturnsAdmin)
