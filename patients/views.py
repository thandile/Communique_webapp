from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Patient

"""
Views for the web app.
"""


class PatientListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view to list all patients that currently exist in the system. This view is only available to logged in and active
    registered users of the system.

    If the user fails any part of the criteria, this view will redirect them to the login page.
    """
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patient_list'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active