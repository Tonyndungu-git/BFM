# movers/forms.py

from django import forms
from .models import Quotation

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'  # Use all fields from the Quotation model
