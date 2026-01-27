from rest_framework import serializers
from .models import Area, City




class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name']



class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name', 'city']

    
