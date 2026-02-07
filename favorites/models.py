from django.db import models
from properties.models import Property

class Favorite(models.Model):
    user = models.ForeignKey('accounts.User', related_name='favorites', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='favorited_by', on_delete=models.CASCADE) 
