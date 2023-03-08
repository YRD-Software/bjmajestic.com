from django.views import generic
from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def index(request):
    return render(request, "homepage/index.html", {"page": "home"})


class ProductsView(generic.ListView):
    """A list of all the products."""

    template_name = "homepage/products.html"
    model = Product

    # Define context to be passed to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "product"
        context["categories"] = Category.objects.all()
        # If a category is specified, filter products by that category
        if self.kwargs.get("category"):
            print(self.kwargs.get("category").title())
            context["products"] = Product.objects.filter(
                categories__category=self.kwargs.get("category").title()
            )
            context["title"] = self.kwargs.get("category").title()
            context[
                "message"
            ] = f"""There are currently no products in the {self.kwargs.get('category')} category.
            Check back later! :)"""
        else:
            context["products"] = Product.objects.all()
            context["title"] = "Categories"
            context["message"] = "There are no products yet. Check back later! :)"
        return context


class DetailProductView(generic.DetailView):
    """The view for displaying details about a product."""

    model = Product
    template_name = "homepage/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["similar_products"] = [1, 2, 3]
        return context
