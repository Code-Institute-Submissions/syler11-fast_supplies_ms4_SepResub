"""
Imports
"""
from django import forms
from .models import Returns


class ReturnsForm(forms.ModelForm):
    """
    Order form class
    """
    class Meta:
        """
        Meta info class
        """
        model = Returns
        fields = ('order_number', 'username', 'return_reason',
                  'additional_info',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black w-75 rounded-0'