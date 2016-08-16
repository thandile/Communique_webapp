from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import *
from .forms import *

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


class ProgramCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view to handle creation of a Program by displaying the form and handling the post request.
    """
    form_class = ProgramForm
    model = Program
    template_name = 'programs/program_form.html'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class ProgramDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view to display the details of a Program. The name sort of gives it away.
    """
    model = Program
    template_name = 'programs/program_view.html'
    context_object_name = 'program'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active
