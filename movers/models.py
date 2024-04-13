from django.db import models

class Mover(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # Add more fields as needed
    
    def __str__(self):
        return self.name
