from rest_framework import serializers
from properties.models import Property, PropertyImage, Amenity

class PropertyListSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True, allow_null=True)
    area_name = serializers.CharField(source='area.name', read_only=True, allow_null=True)
    primary_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Property
        fields = ['title', 'price', 'property_type', 
                  'status','bedrooms','bathrooms','area_sq_m',
                  'created_at', 'city_name', 'area_name', 'primary_image']
        read_only_fields = ['created_at']

    def get_primary_image(self,obj):
        first_image = obj.images.first()
        if first_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_image.image.url)
            return first_image.image.url
    
        return None


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id','name']

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class PropertyDetailSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')
    images = PropertyImageSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    area_name = serializers.CharField(source='area.name', read_only=True, allow_null=True)
    
    class Meta:
        model = Property
        fields = ['agent','title', 'price', 'description',
                   'property_type','address','area','city','amenities', 'images']

class PropertyCreateSerializer(serializers.ModelSerializer):
    amenities = serializers.PrimaryKeyRelatedField(many=True, queryset=Amenity.objects.all(), required=False)

    class Meta:
        model = Property
        fields = ['title', 'price', 'property_type', 
                  'status','bedrooms','bathrooms','area_sq_m',
                  'created_at', 'city_name', 'area_name', 'primary_image']
        
    def validate_price(self, value):
        if value <= 0:
            return serializers.ValidationError('price should be more than 0')
        return value
    
    def validate_title(self, value):
        if len(value) < 10:
            return serializers.ValidationError('The title mus be longer')
        return value
    
    def validate(self,data):
        if data.get('area') and data.get('city'):
            if data.get('area.city') != data.get('city'):
                return serializers.ValidationError('Area must belong to the city')
            return data