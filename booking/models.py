from django.db import models
from properties.models import Property

class VievingBooking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]


    user = models.ForeignKey('accounts.User', related_name="booking", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name="booked_property", on_delete=models.CASCADE)
    date = models.DateTimeField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


