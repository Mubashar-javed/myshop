from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    """form for creating new order"""

    class Meta:
        model = Order
        exclude = ['updated', 'created', 'paid']
