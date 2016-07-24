from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    A serializer for the default Django User model class.
    """
    class Meta:
        model = User
        fields = ('id', 'username')
