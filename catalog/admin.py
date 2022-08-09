from django.contrib import admin
from .models import Catalog

# Register your models here.
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('year',)

admin.site.register(Catalog, CatalogAdmin)