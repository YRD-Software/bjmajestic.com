from django.urls import path

from . import views

app_name = 'contact_us'
urlpatterns = [
    # Contact us page
    path('contact/', views.contact_us, name='contact')
]