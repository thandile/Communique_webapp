from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer

"""
Views for the REST API
"""

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view set automatically provides 'list' and 'detail' actions for the
    User model via REST API
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
