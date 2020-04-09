from django import forms

PRODUCT_QUANTITY_CHOICE = [(i, str(i)) for i in range(20)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(coerce=int, choices=PRODUCT_QUANTITY_CHOICE)
    update = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=False)
