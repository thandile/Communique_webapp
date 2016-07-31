from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from .forms import *

"""
Views for the Web App
"""
class AccountListView(LoginRequiredMixin, ListView):
    """
    A view to list all accounts of the system.
    """
    model = User
    template_name = 'user/account_list.html'
    context_object_name = 'object_list'

class AccountCreateView(LoginRequiredMixin, CreateView):
    """
    A view to create an account.
    """
    form_class = UserForm
    model = User
    template_name = 'user/account_form.html'


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
