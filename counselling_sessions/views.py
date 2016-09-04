from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


