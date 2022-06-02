from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
	# Homepage
	path('', views.index, name='index'),
	# The product page.
	path('products/', views.ProductsView.as_view(), name='products'),
	# The product detail page.
	path('product/<int:pk>/', views.DetailProductView.as_view(), name='product_detail'),
	# About page.
	path('about/', views.about, name='about'),
]
