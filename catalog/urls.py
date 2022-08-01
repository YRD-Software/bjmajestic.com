from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    # Catalog page 
    path('catalog/', views.catalog, name='catalog'),
]