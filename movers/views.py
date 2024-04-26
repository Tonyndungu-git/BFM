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
