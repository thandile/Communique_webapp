
from rest_framework import viewsets
from rest_framework import generics

from .serializers import *
from .permissions import IsActiveUser, IsSuperUser, IsProfileOrReadOnly

from programs.models import Program
from patients.models import Patient, Enrollment
from user.models import CommuniqueUser, Profile


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


class CommuniqueUserViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD CommuniqueUser models.

    Only superusers can access it.
    """
    queryset = CommuniqueUser.objects.all()
    serializer_class = CommuniqueUserSerializer
    permission_classes = (IsActiveUser, IsSuperUser,)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Profile models.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsActiveUser, IsProfileOrReadOnly,)


class ProfileLoginView(generics.RetrieveAPIView):
    """
    This endpoint retrieves a user's profile on successful login.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'