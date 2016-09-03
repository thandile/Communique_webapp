from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import *
from .models import *


class CommuniqueUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view to list all users of the system. This is only available to logged in, active superusers of the system.

    If any of the criteria is failed, the user will be redirected to the login page.
    """
    model = CommuniqueUser
    template_name = 'user/communique_user_list.html'
    context_object_name = 'communique_user_list'

    def test_func(self):
        """
        Returns whether the user making the request is a superuser and is active.
        """
        current_user = self.request.user
        return current_user.is_superuser and current_user.is_active


class CommuniqueUserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view to create a Communique user. This is only available to logged in active superusers of the system.

    If the criteria fails, the user will be redirected to the login page.
    """
    form_class = CommuniqueUserCreationForm
    model = CommuniqueUser
    template_name = 'user/communique_user_form.html'

    def test_func(self):
        """
        Returns whether the user making the request is an active superuser.
        """
        current_user = self.request.user
        return current_user.is_superuser and current_user.is_active


class CommuniqueUserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view to display information of a user. This is only available to logged in active superusers of the system.

    If the criteria fails, the user will be redirected to the login page.
    """
    model = CommuniqueUser
    template_name = 'user/communique_user_view.html'
    context_object_name = 'communique_user'

    def test_func(self):
        """
        Returns whether the user making the request is an active superuser.
        """
        current_user = self.request.user
        return current_user.is_active and current_user.is_superuser


class CommuniqueUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to update the information for a user. This is only available to active logged in superusers of the system.

    If the criteria fails, the user will be redirected to the login page.
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


class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view to display the details of a user. This is only available to an active logged in user who is trying to access
    his/her own details.

    If the criteria fails, the user will be redirected to the login page.
    """
    model = Profile
    template_name = 'user/profile_view.html'
    context_object_name = 'user_profile'

    def test_func(self):
        """
        Returns whether the user is making request to view his/her profile and is an active user.
        """

        return (str(self.request.user.pk) == str(self.kwargs['pk'])) and self.request.user.is_active


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to update a user's profile. This is only available to an active logged in user that is trying to update
    his/her own profile.

    If the criteria fails, the user will be redirected to the login page.
    """
    form_class = ProfileUpdateForm
    model = Profile
    template_name = 'user/profile_update_form.html'
    context_object_name = 'user_profile'

    def test_func(self):
        """
        Returns whether the user making requests to his/her own profiles and is an active user.
        """
        return (str(self.request.user.pk) == str(self.kwargs['pk'])) and self.request.user.is_active

