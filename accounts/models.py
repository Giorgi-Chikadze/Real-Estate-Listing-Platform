from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class AgentProfile(models.Model):
    user = models.OneToOneField('accounts.User', related_name="agent_profile", on_delete=models.CASCADE)
    phone = models.CharField(max_length=32, unique=True)
    agency_name = models.CharField(max_length=255, unique=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to="agents")
    is_verified = models.BooleanField(default=False)



    




