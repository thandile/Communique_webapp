from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PatientSerializer, PilotProgramSerializer
from .models import Patient, PilotProgram

"""
Views for the REST API
"""

class PatientViewSet(viewsets.ModelViewSet):
    """
    A view set that automatically provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions for the Patient model via REST API.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticated,)

class PilotProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A view set that automatically provides `list` and `detail` actions for the
    Pilot Program model via REST API.
    """
    queryset = PilotProgram.objects.all()
    serializer_class = PilotProgramSerializer
