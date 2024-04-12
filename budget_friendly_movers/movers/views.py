from django.shortcuts import render
from .models import Mover

def index(request):
    movers = Mover.objects.all()
    return render(request, 'movers/index.html', {'movers': movers})

def about(request):
    return render(request, 'movers/about.html')
