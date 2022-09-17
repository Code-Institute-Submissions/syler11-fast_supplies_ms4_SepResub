"""
Imports
"""
from django.db import models


class Category(models.Model):
    """
    Category model class
    """
    class Meta:
        """
        Meta info class
        """
        verbose_name_plural = "Categories"  \
            # Fixing issues in Djanho admin Categorys

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Return category name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Return category name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    Product model class
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    quantity = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Returns product name
        """
        return self.name
