from django.shortcuts import render
from .models import Mover
from .forms import QuotationForm


def index(request):
    movers = Mover.objects.all()
    return render(request, 'movers/index.html', {'movers': movers})

def about(request):
    return render(request, 'movers/about.html')



def services_view(request):
    # Logic to handle the services view
    return render(request, 'movers/services.html')  # Example response

def contact_us(request):
    # Render the contact us page template
    return render(request, 'movers/contact.html')

# movers/views.py


def get_quote_view(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the valid form data to the database
            # Optionally, you can redirect to a success page
            return render(request, 'movers/quote_success.html')
    else:
        form = QuotationForm()
    
    return render(request, 'movers/get_quote.html', {'form': form})
