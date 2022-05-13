from django.db import models
from django.urls import reverse


# Create your models here.

class Product(models.Model): # FIXME: not working
	"""A description for a product"""
	id = models.IntegerField(primary_key=True)
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
	id = models.IntegerField(primary_key=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	detail_photo = models.ImageField(upload_to='detail_product_images/')

	def __str__(self):
		"""Return string rep for ProductPhoto."""
		return self.detail_photo.name

	class Meta:
		verbose_name_plural = 'Product Photos'


class About(models.Model):
	"""Text for about us."""
	id = models.IntegerField(primary_key=True)
	title = "About"
	text = models.TextField('About Us')

	def __str__(self):
		"""Return string representation of the model"""
		return self.title

	class Meta:
		verbose_name_plural = 'About'
