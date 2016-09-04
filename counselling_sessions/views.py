from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import *


class CounsellingSessionTypeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that retrieves all the available session types.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_list.html'
    context_object_name = 'counselling_session_list'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active

