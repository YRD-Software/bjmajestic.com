""" Admin configuration for products app. """
from django.contrib import admin

from .models import Category, Product, ProductPhoto


class DetailPhotosInline(admin.TabularInline):
    """Inline form for adding extra photos to a product."""

    model = ProductPhoto
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    """Define how the Products page in admin is going to look."""

    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Details", {"fields": ["description", "categories"]}),
        ("Main Image", {"fields": ["photo"]}),
    ]
    filter_horizontal = ("categories",)
    inlines = [DetailPhotosInline]
    list_display = ("name",)
    search_fields = ["name"]


class ProductPhotoAdmin(admin.ModelAdmin):
    """Define how the Product Photos page in admin is going to look."""

    list_display = ("product", "detail_photo")
    list_filter = ["product"]


class CategoryAdmin(admin.ModelAdmin):
    """Define how the Categories page in admin is going to look."""

    list_display = ("category",)
    search_fields = ["category"]


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
