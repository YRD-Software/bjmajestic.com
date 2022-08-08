from django.shortcuts import render
from .models import Catalog

# Create your views here.
def catalog(request):
    """Display catalog page."""
    catalogs = Catalog.objects.order_by('-year')
    context = {'page': 'catalog', 'catalogs': catalogs}
    return render(request, 'catalog/catalog.html', context)