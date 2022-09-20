"""
Imports
"""
from django.shortcuts import (render, redirect)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User

from checkout.models import Order

from .forms import ReturnsForm

from .models import Returns


def request_returns(request):
    """
    A view to return the request_return page
    """
    user_id = request.user.id

    username = request.user

    returns = Returns.objects.filter(username=username)

    new_return = request.POST.get("order_number")

    orders = Order.objects.filter(user_profile=user_id)

    returned = []

    for e in Returns.objects.all():
        returned = e.order_number

    if request.method == 'POST':
        form = ReturnsForm(request.POST)

        if form.is_valid():
            if new_return  not in returned:
                form.save()

                # email subject path
                subject = render_to_string(
                    'returns/returns_email/returns_email_subject.txt',
                    {'username': username})

                # email body path
                body = render_to_string(
                    'returns/returns_email/returns_email_body.txt',
                    {'username': username, 'new_return': new_return, })

                # user email
                user_email = request.user.email

                # send an request email from request page
                send_mail(
                    subject,
                    body,
                    'noreply@fastsupplies.co.uk',
                    [user_email],
                    fail_silently=False,
                    )

                messages.success(request, 'Return request was '
                                 'successfully submitted!')
                return redirect(reverse('request_returns'))
            else:
                messages.error(request, 'This order is already '
                               'in the return history!')
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
        'new_return': new_return
    }

    return render(request, "returns/request_returns.html", context)
