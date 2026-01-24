from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AgentProfile(models.Model):
    user = models.OneToOneField(User, related_name="agents", on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(unique=True)
    agency_name = models.CharField(max_length=255, unique=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to="media/properties")
    is_verified = models.BooleanField()



    




