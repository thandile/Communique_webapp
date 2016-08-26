
from rest_framework import viewsets

from .serializers import ProgramSerializer
from .permissions import IsActiveUser

from programs.models import Program


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