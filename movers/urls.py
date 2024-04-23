from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services_view, name='services'),
    # Other URL patterns...
    # Add more paths for other views
]
