from django.contrib import admin
from .models import Mover, Quotation, ContactMessage



# Register your models here.

admin.site.register(Mover)
admin.site.register(Quotation)
admin.site.register(ContactMessage)