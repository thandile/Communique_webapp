from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy

from .models import Patient, Enrollment

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


class PatientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view to handle creation of patients. This view is only available to logged in and active registered users of the
    system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    model = Patient
    fields = ['first_name', 'last_name', 'middle_name', 'birth_date', 'identifier', 'location', 'contact_number',
              'reference_health_centre']
    template_name = 'patients/patient_form.html'

    def form_valid(self, form):
        patient = form.save(commit=False)
        # update the created by and last modified by user markers
        patient.created_by = self.request.user
        patient.last_modified_by = self.request.user

        return super(PatientCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class PatientDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view to display the details of a patient. This view is only available to logged in and active registered users of
    the system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    model = Patient
    template_name = 'patients/patient_view.html'
    context_object_name = 'patient'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to handle updating patient information. This view is only available to logged in and active registered users
    of the system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    model = Patient
    fields = ['first_name', 'last_name', 'middle_name', 'birth_date', 'identifier', 'location', 'contact_number',
              'reference_health_centre']
    template_name = 'patients/patient_update_form.html'
    context_object_name = 'patient'

    def form_valid(self, form):
        patient = form.save(commit=False)
        # update the last modified markers
        patient.last_modified_by = self.request.user

        return super(PatientUpdateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to handle the deletion of a patient. This view is only available to logged in registered users of the system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    model = Patient
    success_url = reverse_lazy('patients_patient_list')
    context_object_name = 'patient'
    template_name = 'patients/patient_confirm_delete.html'

    def test_func(self):
        """
        Checks whether the current user is an active user
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class EnrollmentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view to list all the enrollments that currently exist in the system. This view is only available to logged in and
    active registered users of the system.

    If the user fails any part of the criteria, this view will redirect them to the login page.
    """
    model = Enrollment
    template_name = 'patients/enrollment_list.html'
    context_object_name = 'enrollment_list'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class EnrollmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view to handle creation of an enrollment. This view is only available to logged in and active registered users of
    the system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    model = Enrollment
    fields = ['patient', 'program', 'comment']
    template_name = 'patients/enrollment_form.html'

    def form_valid(self, form):
        enrollment = form.save(commit=False)
        # add user that has enrolled patient into program
        enrollment.enrolled_by = self.request.user

        return super(EnrollmentCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is an active user/
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active

