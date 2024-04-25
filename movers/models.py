from django.db import models

class Mover(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # Add more fields as needed
    
    def __str__(self):
        return self.name
    
class Quotation(models.Model):
    MOVING_TYPE_CHOICES = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
    ]

    HOUSE_SIZE_CHOICES = [
        ('1 Bedroom', '1 Bedroom'),
        ('2 Bedrooms', '2 Bedrooms'),
        ('3 Bedrooms', '3 Bedrooms'),
        ('4+ Bedrooms', '4+ Bedrooms'),
    ]

    moving_type = models.CharField(max_length=20, choices=MOVING_TYPE_CHOICES)
    moving_date = models.DateField()
    house_size = models.CharField(max_length=20, choices=HOUSE_SIZE_CHOICES)
    source_address = models.CharField(max_length=100, verbose_name="Moving From")
    destination_address = models.CharField(max_length=100, verbose_name="Moving To")
    current_house_type = models.CharField(max_length=100)
    destination_house_type = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    extra_services = models.TextField(blank=True)
    more_details = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quotation request by {self.first_name} {self.last_name}"

    def estimated_cost(self):
        # Add logic here to calculate estimated cost based on the quotation details
        # For example:
        # Calculate cost based on house size, distance, extra services, etc.
        return "Insert logic for estimated cost calculation"
