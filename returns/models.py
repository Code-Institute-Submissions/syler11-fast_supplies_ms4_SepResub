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

    RETURN_REASON_CHOICES = [
        ('wrong_item', 'Wrong Item'),
        ('damaged_item', 'Damaged Item'),
        ('item_not_received', 'Item Not Received'),
    ]

    order_number = models.ForeignKey(Order, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    username = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    return_reason = models.CharField(max_length=20, choices=RETURN_REASON_CHOICES,)
    return_request_date = models.DateTimeField(auto_now_add=True)
    additional_info = models.CharField(max_length=200, blank=True)


    def __str__(self):
        """
        Return Returns ordernumber name string
        """
        return str(self.order_number)
