from django.views import generic
from django.shortcuts import render
from .models import Product, About

# Create your views here.


def index(request):
	return render(request, 'homepage/index.html')


class ProductsView(generic.ListView):
	"""A list of all the products."""
	template_name = 'homepage/products.html'

	# Return all products
	def get_queryset(self):
		return Product.objects.all()

	# Define context to be passed to template
	def get_context_data(self, *, object_list=None, **kwargs):
		context = {'page': 'product', 'products': self.get_queryset()}
		return context


class DetailProductView(generic.DetailView):
	"""The view for displaying details about a product."""
	model = Product
	template_name = 'homepage/product_detail.html'
	context_object_name = 'product'


def about(request):
	"""Display about us page."""
	texts = About.objects.all()
	context = {'texts': texts, 'page': 'about'}
	return render(request, 'homepage/about.html', context)
