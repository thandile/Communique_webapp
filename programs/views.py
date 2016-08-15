from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import *

"""
Views for the web app.
"""

class ProgramListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view to list all programs of the system. This view is only available to logged in active registered users of the
    system.

    If the user is fails any part of the criteria, this view will redirect them to the login page.
    """
    model = Program
    template_name = "programs/program_list.html"
    context_object_name = 'program_list'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active