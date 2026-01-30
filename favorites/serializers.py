from rest_framework import serializers
from .models import Favorite
from properties.models import Property

class FavoriteSerializer(serializers.ModelSerializer):
    property_id = serializers.IntegerField(write_only = True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Favorite
        fields = ["id", "user", "property", "property_id"]

    def validate_property_id(self, value):
        if not Property.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid Property id, The Property Doesn't Exist")
        return value
    
    def create(self, validated_data):
        property_id = validated_data.pop('property_id')
        user = validated_data.pop("user")

        property = Property.objects.get(id = property_id)

        favorite, created = Favorite.objects.get_or_create(user=user, property = property)

        if not created:
            raise serializers.ValidationError("This Property is Already in Favorites")
        
        return favorite
