from django.contrib import admin

from .models import Flat, Claim


class FlatAdminSettings(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owner_pure_phone'
    ]
    list_filter = [
        'new_building',
        'rooms_number',
        'has_balcony'
    ]
    list_editable = ['new_building']
    raw_id_fields = ['liked_by']


class ClaimSettings(admin.ModelAdmin):
    raw_id_fields = ['flat']

admin.site.register(Flat, FlatAdminSettings)
admin.site.register(Claim, ClaimSettings)