from django import forms

from .models import Coupons


class CouponAppplyForm(forms.ModelForm):
    class Meta:
        model = Coupons
        fields = ['code']
