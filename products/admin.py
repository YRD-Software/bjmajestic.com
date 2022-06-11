from django.contrib import admin

from .models import Product, ProductPhoto


class DetailPhotosInline(admin.TabularInline):
    """Allow admin to edit ProductPhoto objects through Product admin page."""
    model = ProductPhoto
    extra = 2


# Define how the model is displayed on administration page.

class ProductAdmin(admin.ModelAdmin):
    """Define how the Products page in admin is going to look."""
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Details', {'fields': ['description', ]}),
        ('Main Image', {'fields': ['photo']}),
    ]
    inlines = [DetailPhotosInline]
    list_display = ('name',)
    search_fields = ['name']


class ProductPhotoAdmin(admin.ModelAdmin):
    """Define how the Product Photos page in admin is going to look."""
    list_display = ('product', 'detail_photo')
    list_filter = ['product']


# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
