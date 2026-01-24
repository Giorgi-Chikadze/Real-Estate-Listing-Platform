from django.db import models
from accounts.models import AgentProfile
from locations.models import Area

# Create your models here.
class Property(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    area_sq_m = models.PositiveIntegerField()
    
    class PropertyType(models.TextChoices):
        HOUSE = "house", "House"
        APARTMENT = "apartment", "Apartment"
        LAND = "land", "Land"

    class Status(models.TextChoices):
        FOR_SALE = "for_sale", "For Sale"
        FOR_RENT = "for_rent", "For Rent"

    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices
    )

    address = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/')

class Amenity(models.Model):
    name = models.CharField()
    properties = models.ManyToManyField(Property, related_name='amenities')


