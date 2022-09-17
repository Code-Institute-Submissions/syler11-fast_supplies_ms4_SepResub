"""
Imports
"""
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.urls import reverse

from .models import Returns



def request_returns(request):
    """
    A view to return the request_return page
    """
    
    returns = Returns.objects.all()

    context = {
        'returns': returns
    }

    return render(request, "returns/request_returns.html", context)
