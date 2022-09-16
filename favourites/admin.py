"""
Imports
"""
from django.contrib import admin
from .models import Favourites

# Register your models here.


class FavouritesAdmin(admin.ModelAdmin):
    """
    Favourites admin  model class
    """
    list_display = (
        'username',
    )
    list_filter = (
        'username',
    )
    search_fields = (
       'username',
    )

    ordering = ('username',)


admin.site.register(Favourites, FavouritesAdmin)
