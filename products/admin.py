""" Admin configuration for products app. """
from django.contrib import admin

from .models import Category, Product, ProductPhoto


class DetailPhotosInline(admin.TabularInline):
    """Inline form for adding extra photos to a product."""

    model = ProductPhoto
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    """Define how the Products page in admin is going to look."""

    fieldsets = [
        ("Product Details", {"fields": ["name", "description", "categories"]}),
    ]
    filter_horizontal = ("categories",)
    inlines = [DetailPhotosInline]
    list_display = ("name",)
    search_fields = ["name", "categories"]

    def save_model(self, request, obj, form, change):
        """Save product"""
        obj.save()
        files = request.FILES.getlist("photos")
        for a_file in files:
            temp_photo = ProductPhoto(product=obj, photo=a_file)
            temp_photo.save()


class ProductPhotoAdmin(admin.ModelAdmin):
    """Define how the Product Photos page in admin is going to look."""

    list_display = ("product", "photo")
    list_filter = ["product"]


class CategoryAdmin(admin.ModelAdmin):
    """Define how the Categories page in admin is going to look."""

    list_display = ("category",)
    search_fields = ["category"]


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
