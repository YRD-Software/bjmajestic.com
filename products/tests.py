from django.test import TestCase
from django.urls import reverse
from .models import Product, About
# Create your tests here.


def create_product(name, description='Default text.', photo='A photo'):
    """Create a fake product."""
    return Product.objects.create(name=name, description=description, photo=photo)


class ProductsIndexViewTests(TestCase):
    """A test class to check if product page is working properly."""

    def test_no_products(self):
        """Test an empty products page."""
        response = self.client.get(reverse('products:products'))
        self.assertContains(
            response, 'There are no products yet. Check back later! :)')

    def test_shows_products(self):
        """Test products page with one product."""
        create_product(name='Test Product')
        response = self.client.get(reverse('products:products'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['products'], [
                                 '<Product: Test Product>'])

    def test_create_missing_field_product(self):
        """Test creating a product with a missing field."""
        product = Product.objects.create(name='Test Product')
        with self.assertRaisesMessage(ValueError, "attribute has no file associated with it"):
            self.client.get(
                reverse('products:product_detail', args=(product.id,)))


class ProductPhotoDetailViewTests(TestCase):
    """A test class for ProductPhoto class and its view."""

    def test_show_product_detail(self):
        """Test product detail view."""
        product = create_product(name='Test Product')
        response = self.client.get(
            reverse('products:product_detail', args=(product.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name)

    def test_show_non_exist_product_detail(self):
        """Test non exist product detail view."""
        product = create_product(name='Test Product')
        response = self.client.get(
            reverse('products:product_detail', args=(product.id + 3,)))
        self.assertEqual(response.status_code, 404)


class AboutPageTests(TestCase):
    """A test class for About Page."""

    def test_show_about_us(self):
        about = About.objects.create(text='About us')
        response = self.client.get(reverse('products:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, about.text)
        self.assertTemplateUsed(response, 'homepage/about.html')


class IndexViewTests(TestCase):
    """A test class for Index Page."""

    def test_show_index(self):
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage/index.html')
