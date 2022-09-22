"""
Imports
"""
from django.http import Http404
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Favourites


@login_required
def product_favourites(request):
    """
    A view to return the favourites page
    """

    try:
        all_favourites = Favourites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favourites_items = None
    else:
        favourites_items = all_favourites.products.all()

    if not favourites_items:
        messages.warning(request, 'No favourites added yet!')

    context = {
        'favourites_items': favourites_items
    }

    return render(request, "favourites/favourites.html", context)


def add_to_favourites(request, item_id):
    """
    A view to add product to favourites
    """

    product = get_object_or_404(Product, pk=item_id)
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        favourites = Favourites.objects.create(username=request.user)
    if product in favourites.products.all():
        messages.info(request, 'The product is already in favourites!')
    else:
        favourites.products.add(product)
        messages.info(request, 'The product was added to your favourites')
    return redirect(reverse('product_favourites'))


def remove_from_favourites(request, item_id):
    """
    A view to remove product to favourites
    """
    product = get_object_or_404(Product, pk=item_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)
    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.info(request, 'The product was removed to your favourites')
    else:
        messages.error(request, 'That product not in your favourites')
    return redirect(reverse('product_favourites'))
