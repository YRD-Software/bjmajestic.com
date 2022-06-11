from django.db import models

# Create your models here.
class About(models.Model):
	"""Text for about us."""
	title = "About"
	text = models.TextField('About Us')

	def __str__(self):
		"""Return string representation of the model"""
		return self.title

	class Meta:
		verbose_name_plural = 'About'
