from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
	# About page.
	path('about/', views.about, name='about'),
]
