from django.shortcuts import render
from rest_framework import viewsets
from .models import Property, PropertyImage, Amenity
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from properties.serializers import (PropertyDetailSerializer, PropertyListSerializer,
                                    PropertyImageSerializer, AmenitySerializer)

class PropertyMOdelviewset(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    filter_backends = DjangoFilterBackend
    search_fields = ['title', 'address']
    ordering_fields = ['price']

    def get_serializer_class(self):
        if self.action == 'list':
            return PropertyListSerializer
        elif self.action == 'retrieve':
            return PropertyDetailSerializer
        return PropertyListSerializer
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        
        property_instance = self.get_object()

        property_instance.view_count += 1

        return response