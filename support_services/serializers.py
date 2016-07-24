from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    """
    A serializer for the Service model class.
    """
    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'slug')
