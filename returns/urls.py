"""
Imports
"""
from django.urls import path
from . import views

urlpatterns = [
    path('request_returns/', views.request_returns, name='request_returns'),
]