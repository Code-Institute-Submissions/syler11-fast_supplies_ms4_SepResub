"""
Imports
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout configuration class
    """
    name = 'checkout'

    def ready(self):
        """
        Import checkout signals
        """
        import checkout.signals
