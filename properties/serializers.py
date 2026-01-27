from rest_framework import serializers
from properties.models import Property, PropertyImage, Amenity

class PropertyLIstSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')
    area_name = serializers.CharField(source='area.name', read_only=True, allow_null=True)
    primary_image = serializers.SerializerMethodField()
    
    class Meta:
        model = property
        fields = ['title', 'price', 'property_type', 
                  'status','bedrooms','bathrooms','area_sq_m',
                  'created_at']
        read_only_fields = ['created_at']

    def get_primary_image(self,obj):
        first_image = obj.images.first()
        if first_image:
            request = self.context.get('request')
            if request:
                 return request.build_absolute_uri(first_image.image.url)
            return first_image.image.url
    
        return None