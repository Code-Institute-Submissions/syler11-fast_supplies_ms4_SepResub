"""
Imports
"""
from django.http import Http404
from django.shortcuts import (render, redirect, get_object_or_404)
from django.core.mail import send_mail
from django.template.loader import render_to_string
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

    user_email = request.user.email

    username = request.user

    rtrn = Returns.objects.all()

    returns = Returns.objects.filter(username=username)

    new_return = request.POST.get("order_number")

    orders = Order.objects.filter(user_profile=user_id)

    if request.method == 'POST':
        form = ReturnsForm(request.POST)
        for e in Returns.objects.all():
            test = e.order_number

        if form.is_valid():
            if new_return  not in test:
                form.save()

                # email subject path
                subject = render_to_string(
                    'returns/returns_email/returns_email_subject.txt',
                    {'username': username})
            
                # email body path
                body = render_to_string(
                    'returns/returns_email/returns_email_body.txt',
                    {'username': username, 'orders': orders, 'returns': returns, 'new_return': new_return, 'rtrn': rtrn})

                # send an request email from request page
                send_mail(
                    subject,
                    body,
                    'noreply@fastsupplies.co.uk',
                    ['nemeth.szilard82@gmail.com'],
                    fail_silently=False,
                    )

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
        'username': username,
        'rtrn': rtrn,
        'new_return': new_return
    }

    return render(request, "returns/request_returns.html", context)

