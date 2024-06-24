from django.shortcuts import render, redirect
from .models import Mover, Quotation, ContactMessage
from .forms import QuotationForm, ContactForm

def index(request):
    movers = Mover.objects.all()
    return render(request, 'movers/index.html', {'movers': movers})

def about(request):
    return render(request, 'movers/about.html')

def services_view(request):
    # Logic to handle the services view
    return render(request, 'movers/services.html')  # Example response

from django.shortcuts import render, get_object_or_404

# Example data structure
APARTMENTS = {
    'apartment1': {
        'title': 'Apartment 1',
        'description': '2 Bedroom, 1 Bathroom and toilet, Kasarani, Nairobi',
        'images': [
            'images/apartments11.jpg',
            'images/apartment12.jpg',
            'images/apartment13.jpg',
            'images/apartment14.jpg',
        ]
    },
    # 'apartment2': {
    #     'title': 'Apartment 2',
    #     'description': '3 Bedroom, 2 Bathroom, Suburbs',
    #     'images': [
    #         'images/apartment2.jpg',
    #         'images/apartment2_1.jpg',
    #         'images/apartment2_2.jpg',
    #         'images/apartment2_3.jpg',
    #         'images/apartment2_4.jpg',
    #     ]
    # },
    # Add more apartments as needed
}

def apartments(request):
    return render(request, 'movers/apartments.html', {'apartments': APARTMENTS})

def apartment_detail(request, apartment_name):
    apartment = get_object_or_404(APARTMENTS, apartment_name)
    return render(request, 'movers/apartment_detail.html', {'apartment': apartment})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save the message to the database
            contact_message = ContactMessage(name=name, email=email, message=message)
            contact_message.save()
            
            # Redirect to the thank you page upon successful submission
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'movers/contact.html', {'form': form})

def get_quote_view(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Quotation saved successfully.")
            return redirect('thank_you')
        else:
            print("Form errors:", form.errors)
    else:
        form = QuotationForm()
    
    return render(request, 'movers/get_quote.html', {'form': form})
def thank_you(request):
    return render(request, 'movers/thank_you.html')
