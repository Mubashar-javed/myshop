from django.contrib import admin
from .models import Coupons


@admin.register(Coupons)
class CouponsAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    search_fields = ['code']
    list_filter = ['active', 'valid_from', 'valid_to', ]

