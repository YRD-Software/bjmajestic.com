from django.shortcuts import render

# Create your views here.
def catalog(request):
    """Display catalog page."""
    context = {'page': 'catalog'}
    return render(request, 'catalog/catalog.html', context)