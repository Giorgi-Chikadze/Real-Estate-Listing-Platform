from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)

class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='areas')
    name = models.CharField(max_length=100)