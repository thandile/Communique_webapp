from rest_framework import serializers

from programs.models import Program
from patients.models import Patient, Enrollment


class ProgramSerializer(serializers.ModelSerializer):
    """
    A serializer for the Program model.
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    last_modified_by = serializers.ReadOnlyField(source='last_modified_by.username')

    class Meta:
        model = Program
        fields = ('id', 'name', 'description', 'is_open', 'created_by', 'last_modified_by')
        read_only_fields = ('date_created', 'date_last_modified',)


class PatientSerializer(serializers.ModelSerializer):
    """
    A serializer for the Patient model.
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    last_modified_by = serializers.ReadOnlyField(source='last_modified_by.username')

    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'birth_date', 'identifier', 'location',
                  'contact_number', 'reference_health_centre', 'enrolled_programs')
        read_only_fields = ('date_created', 'date_last_modified',)


class EnrollmentSerializer(serializers.ModelSerializer):
    """
    A serializer for the Enrollment model.
    """
    enrolled_by = serializers.ReadOnlyField(source='enrolled_by.username')

    class Meta:
        model = Patient
        fields = ('id', 'patient', 'program', 'comment', 'is_active', 'enrolled_by')
        read_only_fields = ('date_enrolled',)