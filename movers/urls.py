from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services_view, name='services'),
    path('contact/', views.contact_us, name='contact'),
    path('get_quote/', views.get_quote_view, name='get_quote'),
    path('thank_you/', views.thank_you, name='thank_you'),
    
    # Other URL patterns...
    # Add more paths for other views
]
