from django.db import models
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    """A description for a product"""
    name = models.CharField('product', max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_images/')

    def __str__(self):
        """Return a string rep. of the model"""
        return self.name

    def get_absolute_url(self):
        return reverse('products:products')


class ProductPhoto(models.Model):
    """Extra detailed photos of the product."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    detail_photo = models.ImageField(upload_to='detail_product_images/')

    def __str__(self):
        """Return string rep for ProductPhoto."""
        return self.detail_photo.name

    class Meta:
        verbose_name_plural = 'Product Photos'
