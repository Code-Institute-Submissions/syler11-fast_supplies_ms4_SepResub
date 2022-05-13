from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('returns/', views.returns, name='returns'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]
