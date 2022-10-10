from django.views import generic
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect
from .models import Category, Product, Tag

# Create your views here.


def index(request):
    return render(request, 'homepage/index.html', {'page': 'home'})


class ProductsView(generic.ListView):
    """A list of all the products."""
    template_name = 'homepage/products.html'
    model = Product

    def get_categories(self):
        """Get all the categories."""
        return Category.objects.all()

    def get_tags(self):
        """Get all the tags."""
        return Tag.objects.all()

    def get_context_data(self, *args, object_list=None, **kwargs):
        """Get the context data."""
        context = {'page': 'product', 'products': self.get_queryset(
        ), 'categories': self.get_categories(), 'tags': self.get_tags()}
        return context

    def post(self, request): # TODO: Make this work.
        form = forms.Form(request.POST)
        if form.is_valid():
            print(form.data)
        return redirect('products:products')


class DetailProductView(generic.DetailView):
    """The view for displaying details about a product."""
    model = Product
    template_name = 'homepage/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["similar_products"] = [1, 2, 3]
        return context
