from django.db import models
from django.contrib.auth.models import User
from properties.models import Property

class Favorite(models.model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='favorited_by', on_delete=models.CASCADE) 
