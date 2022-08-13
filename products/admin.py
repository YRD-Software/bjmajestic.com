from django.contrib import admin

from .models import Product, ProductPhoto, Category, Tag


class DetailPhotosInline(admin.TabularInline):
    """Allow admin to edit ProductPhoto objects through Product admin page."""
    verbose_name = 'Detailed Product Photo'
    model = ProductPhoto
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    """Define how the Products page in admin is going to look."""
    fieldsets = [
        ("PRODUCT INFO", {'fields': ['name', "description", "category", "tag"]}),
        ('MAIN PRODUCT PHOTO', {'fields': ['photo']}),
    ]
    inlines = [DetailPhotosInline]
    list_display = ('name', 'category',)
    search_fields = ['name', 'category']
    list_filter = ['category', 'tag']


class ProductPhotoAdmin(admin.ModelAdmin):
    """Define how the Product Photos page in admin is going to look."""
    list_display = ('product', 'detail_photo')
    list_filter = ['product']


# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
admin.site.register(Category)
admin.site.register(Tag)
