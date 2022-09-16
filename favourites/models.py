"""
Imports
"""
from django.db import models
from django.contrib.auth.models import User

from products.models import Product



class Favourites(models.Model):
    """
    Favourites model class
    """
    class Meta:
        """
        Meta info class
        """
        verbose_name_plural = "Favourites"  \
        # Fixing issues in Django admin Favouritess

    products = models.ManyToManyField(Product, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        """
        Returns favourites name
        """
        return self.username

