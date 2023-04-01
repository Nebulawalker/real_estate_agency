from django.contrib import admin

from .models import Flat

class FlatSearchAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']


admin.site.register(Flat, FlatSearchAdmin)
