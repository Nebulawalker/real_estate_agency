from django.contrib import admin

from .models import Flat, Claim, Owner

class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']
    list_display = ['address', 'price', 'new_building', 'construction_year']

class FlatAdminSettings(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'        
    ]
    list_filter = [
        'new_building',
        'rooms_number',
        'has_balcony'
    ]
    list_editable = ['new_building']
    raw_id_fields = ['liked_by']
    inlines = [OwnersInline]


class ClaimSettings(admin.ModelAdmin):
    raw_id_fields = ['flat']


class OwnerSettings(admin.ModelAdmin):
    raw_id_fields = ['flats']

admin.site.register(Flat, FlatAdminSettings)
admin.site.register(Claim, ClaimSettings)
admin.site.register(Owner, OwnerSettings)