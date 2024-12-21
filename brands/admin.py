from django.contrib import admin
from .models import Brand
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Brand, BrandAdmin)
