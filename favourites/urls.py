"""
Imports
"""
from django.urls import path
from . import views

urlpatterns = [
    path('product_favourites/', views.product_favourites, name='product_favourites'),
    path('add_to_favourites/<item_id>/',
         views.add_to_favourites, name='add_to_favourites'),
    path('remove_from_favourites/<item_id>/',
         views.remove_from_favourites, name='remove_from_favourites'),
]