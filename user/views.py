from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from functools import reduce
import operator

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from .forms import *
from .models import *

"""
Views for the Web App
"""
class CommuniqueUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view to list all users of the system. This is only available to logged in
    superusers of the system.

    If the user is logged in but is not a superuser, he/she will be redirected
    to the login page.
    """
    model = CommuniqueUser
    template_name = 'user/communique_user_list.html'
    context_object_name = 'communique_user_list'

    def test_func(self):
        """
        Returns whether the user making the request is a superuser.
        """
        return self.request.user.is_superuser

class CommuniqueUserSearchListView(CommuniqueUserListView):
    """
    A view to list users that satisfy the criteria of the provided query.
    This is only available to logged in superusers of the system.

    Should the user not be logged in or not a superuser, he/she will be
    redirected to the login page.
    """
    template_name = 'user/communique_user_list_search.html'

    def get_queryset(self):
        result = super(CommuniqueUserListView, self).get_queryset()

        query = self.request.GET.get('q')

        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                    (Q(username__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                    (Q(first_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                    (Q(last_name__icontains=q) for q in query_list))
            )

        return result

class CommuniqueUserCreateView(LoginRequiredMixin, UserPassesTestMixin,
    CreateView):
    """
    A view to create a Communique user. This is only available to logged in
    superusers of the system.

    Should the user not be logged in or not a superuser, he/she will be
    redirected to the login page.
    """
    form_class = CommuniqueUserCreationForm
    model = CommuniqueUser
    template_name = 'user/communique_user_form.html'

    def test_func(self):
        """
        Returns whether the user making the request is a superuser.
        """
        return self.request.user.is_superuser

class CommuniqueUserDetailView(LoginRequiredMixin, UserPassesTestMixin,
    DetailView):
    """
    A view to display information of a user. This is only availabel to logged in
    superusers of the system.

    Should the user not be logged in or not a superuser, he/she will be
    redirected to the login page.
    """
    model = CommuniqueUser
    template_name = 'user/communique_user_view.html'
    context_object_name = 'communique_user'

    def test_func(self):
        """
        Returns whether the user making the request is a superuser.
        """
        return self.request.user.is_superuser

class CommuniqueUserUpdateView(LoginRequiredMixin, UserPassesTestMixin,
    UpdateView):
    """
    A view to update the information for a user. This is only availabel to
    logged in superusers of the system.

    Should the user not be logged in or not a superuser, he/she will be
    redirected to the login page.
    """
    form_class = CommuniqueUserUpdateForm
    model = CommuniqueUser
    template_name = 'user/communique_user_update_form.html'
    context_object_name = 'communique_user'

    def test_func(self):
        """
        Returns whether the user making the request is a superuser.
        """
        return self.request.user.is_superuser

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
