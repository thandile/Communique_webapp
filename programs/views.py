from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
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

    If the user fails any part of the criteria, this view will redirect them to the login page.
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
    A view to handle creation of a Program by displaying the form and handling the post request. This view is only
    available to logged in active registered users of the system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    form_class = ProgramForm
    model = Program
    template_name = 'programs/program_form.html'

    def form_valid(self, form):
        program = form.save(commit=False)
        # update the created by and last modified by markers
        program.created_by = self.request.user
        program.last_modified_by = self.request.user

        return super(ProgramCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class ProgramDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view to display the details of a Program. The name sort of gives it away. This view is only available to logged in
    active registered users of the system.

    If the user fails any of the criteria, this view will redirect them to the login page.
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


class ProgramUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    """
    A view to update the details of a Program. This view is only available to logged in, active registered users of the
    system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    form_class = ProgramForm
    model = Program
    template_name = 'programs/program_update_form.html'
    context_object_name = 'program'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active
