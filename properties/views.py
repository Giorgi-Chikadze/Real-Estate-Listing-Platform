from django.shortcuts import render
from rest_framework import viewsets
from .models import Property, PropertyImage, Amenity
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class PropertyMOdelviewset(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    filter_backends = DjangoFilterBackend
    search_fields = ['title', 'address']
    ordering_fields = ['price']

    