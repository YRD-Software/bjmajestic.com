from django.views import generic
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
	return render(request, 'homepage/index.html', {'page': 'home'})


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
 
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["similar_products"] = [1,2,3] 
		return context
	

