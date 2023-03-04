""" This module contains the models for the products app."""
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    """A category for a product"""
    category = models.CharField('category', max_length=30)

    def __str__(self):
        """Return a string rep. of the model"""
        return str(self.category)

    class Meta:
        """Meta class for Category."""
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """A description for a product"""
    name = models.CharField('product', max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_images/')
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        """Return a string rep. of the model"""
        return str(self.name)

    def get_absolute_url(self):
        """Return a url to access a detail record for this product."""
        return reverse('products:products')


class ProductPhoto(models.Model):
    """Extra detailed photos of the product."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    detail_photo = models.ImageField(upload_to='detail_product_images/')

    def __str__(self):
        """Return string rep for ProductPhoto."""
        return self.detail_photo.name

    class Meta:
        """Meta class for ProductPhoto."""
        verbose_name_plural = 'Product Photos'
