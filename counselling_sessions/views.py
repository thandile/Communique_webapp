from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy

from .models import *


class CounsellingSessionTypeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that retrieves all the available session types.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_list.html'
    context_object_name = 'counselling_session_type_list'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class CounsellingSessionTypeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of a session type.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_form.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        counselling_session_type = form.save(commit=False)
        # update the created by and last modified by fields
        counselling_session_type.created_by = self.request.user
        counselling_session_type.last_modified_by = self.request.user

        return super(CounsellingSessionTypeCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class CounsellingSessionTypeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view that handles displaying details of a session type.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_view.html'
    context_object_name = 'counselling_session_type'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class CounsellingSessionTypeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view that handles updating of a session type.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = CounsellingSessionType
    fields = ['name', 'description']
    template_name = 'counselling_sessions/counselling_session_type_update_form.html'
    context_object_name = 'counselling_session_type'

    def form_valid(self, form):
        session_type = form.save(commit=False)
        # update the last modified field
        session_type.last_modified_by = self.request.user

        return super(CounsellingSessionTypeUpdateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class CounsellingSessionTypeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view that handles the deletion of a session type.

    This view is only available to users that are logged in and marked as active in the system.
    """
    model = CounsellingSessionType
    success_url = reverse_lazy('counselling_sessions_type_list')
    context_object_name = 'counselling_session_type'
    template_name = 'counselling_sessions/counselling_session_type_confirm_delete.html'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class CounsellingSessionListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that retrieves all available sessions.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_list.html'
    context_object_name = 'counselling_session_list'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class CounsellingSessionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of a session.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_form.html'
    fields = ['counselling_session_type', 'patient', 'notes']

    def form_valid(self, form):
        counselling_session = form.save(commit=False)
        # update the created by and last modified by fields
        counselling_session.created_by = self.request.user
        counselling_session.last_modified_by = self.request.user

        return super(CounsellingSessionCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class CounsellingSessionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view that handles displaying details of a session.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_view.html'
    context_object_name = 'counselling_session'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active
