from rest_framework import serializers
from .model import Patient, PilotProgram

class PilotProgramSerializer(serializers.ModelSerializer):
    """
    A serializer for the Pilot Program model.
    """
    class Meta:
        model = PilotProgram
        fields = ('id', 'name', 'description')

class PatientSerializer(serializers.ModelSerializer):
    """
    A serializer for the Patient model.
    """
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'birth_date')
