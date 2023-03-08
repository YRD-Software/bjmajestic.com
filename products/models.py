""" This module contains the models for the products app."""
import uuid
from django.db import models
from django.urls import reverse


def unique_file_path(instance, filename):
    # Generate a unique file name
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return '/'.join([instance.__class__.__name__.lower(), filename])


# Create your models here.
class Category(models.Model):
    """A category for a product"""

    category = models.CharField("category", max_length=30)

    def __str__(self):
        """Return a string rep. of the model"""
        return str(self.category)

    class Meta:
        """Meta class for Category."""

        verbose_name_plural = "Categories"


class Product(models.Model):
    """A description for a product"""

    name = models.CharField("product", max_length=30)
    description = models.TextField()
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        """Return a string rep. of the model"""
        return str(self.name)

    def get_absolute_url(self):
        """Return a url to access a detail record for this product."""
        return reverse("products:products")


class ProductPhoto(models.Model):
    """Extra detailed photos of the product."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=unique_file_path, blank=True, null=True)

    def __str__(self):
        """Return string rep for ProductPhoto."""
        return self.photo.name

    class Meta:
        """Meta class for ProductPhoto."""

        verbose_name_plural = "Product Photos"
