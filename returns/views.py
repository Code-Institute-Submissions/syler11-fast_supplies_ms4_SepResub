"""
Imports
"""
from django.http import Http404
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

    returns = Returns.objects.filter(username=username)

    new_return = request.POST.get("order_number")

    for e in Returns.objects.all():
        test = e.order_number

    orders = Order.objects.filter(user_profile=user_id)

    if request.method == 'POST':
        form = ReturnsForm(request.POST)
        if form.is_valid():
            if new_return  not in test:
                form.save()
                messages.success(request, 'Return request was successfully submitted!')
                return redirect(reverse('request_returns'))
            else:
                messages.error(request, 'This order is already in the return history!')
                return redirect(reverse('request_returns'))
        else:
            messages.error(request,
                           'Failed to add return request. \
                            Please ensure the form is valid.')
    else:
        form = ReturnsForm()

    context = {
        'returns': returns,
        'orders': orders,
        'form': form,
        'username': username
    }

    return render(request, "returns/request_returns.html", context)

