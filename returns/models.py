"""
Imports
"""
from django.db import models
from django.contrib.auth.models import User

from checkout.models import Order


class Returns(models.Model):
    """
    Category model class
    """
    class Meta:
        """
        Meta info class
        """
        verbose_name_plural = "Returns"  \
            # Fixing issues in Django admin Returnss

    order_number = models.CharField(null=True, blank=True, max_length=50)
    username = models.CharField(null=True, blank=True, max_length=50)
    return_reason = models.CharField(max_length=100, blank=True)
    return_request_date = models.DateTimeField(auto_now_add=True)
    additional_info = models.CharField(max_length=200, blank=True)


    def __str__(self):
        """
        Return Returns ordernumber name string
        """
        return str(self.order_number)
