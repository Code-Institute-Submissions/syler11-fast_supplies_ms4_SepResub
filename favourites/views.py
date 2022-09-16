"""
Imports
"""
from django.shortcuts import render


def favourites(request):
    """
    A view to return the favourites page
    """
    return render(request, "favourites/favourites.html")
