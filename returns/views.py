"""
Imports
"""
from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.urls import reverse

from .forms import ReturnsForm

from .models import Returns
from checkout.models import Order


def request_returns(request):
    """
    A view to return the request_return page
    """
    user_id = request.user.id

    username = request.user

    returns = Returns.objects.filter(username=user_id)

    order = Order.objects.filter(user_profile=user_id)

    if request.method == 'POST':
        form = ReturnsForm(request.POST, request.FILES)
        if form.is_valid():
            returns = form.save()
            messages.success(request, 'Return request was successfully submitted!')
            return redirect(reverse('request_returns'))
        else:
            messages.error(request,
                           'Failed to add return request. \
                            Please ensure the form is valid.')
    else:
        form = ReturnsForm()


    context = {
        'returns': returns,
        'form': form,
        'order': order,
        'username': username
    }

    return render(request, "returns/request_returns.html", context)
