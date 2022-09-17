"""
Imports
"""
from django.db import models


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


    def __str__(self):
        """
        Return Returns ordernumber name string
        """
        return self.name
