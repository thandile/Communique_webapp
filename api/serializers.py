from rest_framework import serializers

from programs.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    """
    A serializer for the Program model.
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    last_modified_by = serializers.ReadOnlyField(source='last_modified_by.username')
    
    class Meta:
        model = Program
        fields = ('id', 'name', 'description', 'date_created', 'date_last_modified', 'is_open',
                  'created_by', 'last_modified_by')