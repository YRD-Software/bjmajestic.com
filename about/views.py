from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
	"""Display about us page."""
	texts = About.objects.all()
	context = {'texts': texts, 'page': 'about'}
	return render(request, 'about/about.html', context)
