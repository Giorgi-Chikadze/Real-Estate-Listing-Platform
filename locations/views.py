from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import Area, City
from .serializers import AreaSerializer, CitySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class CityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']



class AreaViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        city_id = self.kwargs.get('city_pk')

        if city_id:
            queryset = queryset.filter(city_id=city_id)

        return queryset

