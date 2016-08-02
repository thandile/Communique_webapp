from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from .forms import *
from .models import *

"""
Views for the Web App
"""
class CommuniqueUserListView(LoginRequiredMixin, ListView):
    """
    A view to list all users of the system.
    """
    model = CommuniqueUser
    template_name = 'user/communique_user_list.html'
    context_object_name = 'communique_user_list'

class CommuniqueUserCreateView(LoginRequiredMixin, CreateView):
    """
    A view to create a Communique user.
    """
    form_class = CommuniqueUserForm
    model = CommuniqueUser
    template_name = 'user/communique_user_form.html'


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
