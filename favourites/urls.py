"""
Imports
"""
from django.urls import path
from . import views

urlpatterns = [
    path('favourites/', views.favourites, name='favourites'),
]