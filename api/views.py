
from rest_framework import viewsets

from .serializers import ProgramSerializer, PatientSerializer, EnrollmentSerializer
from .permissions import IsActiveUser

from programs.models import Program
from patients.models import Patient, Enrollment


class ProgramViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Program models.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that has created the Program
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class PatientViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Patient models.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that has created the Patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Enrollment models.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(enrolled_by=self.request.user)
