from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy

from .models import Patient, Enrollment
from counselling_sessions.models import CounsellingSession
from appointments.models import Appointment
from medical.models import MedicalReport
from .forms import PatientAppointmentForm


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
        Checks whether the user is an active user
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class EnrollmentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view to display details of an enrollment. This view is only available to logged in and active registered users of
    the system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    model = Enrollment
    template_name = 'patients/enrollment_view.html'
    context_object_name = 'enrollment'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class EnrollmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to handle updating an enrollment. This view is only available to logged in and active users of the system.

    If the user fails any of the criteria, this view will redirect them to the login page.
    """
    model = Enrollment
    fields = ['is_active']
    template_name = 'patients/enrollment_update_form.html'
    context_object_name = 'enrollment'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class PatientEnrollmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view to create an enrollment for a defined patient. This view is only available to logged in  and active
     registered users of the system.

     If the user fails any of the criteria, this view will redirect them to the login page.
    """
    model = Enrollment
    fields = ['program', 'comment']
    template_name = 'patients/patient_enrollment_form.html'

    def get_success_url(self):
        # on enrolling the patient, redirect to the patient details view
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        return patient.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(PatientEnrollmentCreateView, self).get_context_data(**kwargs)
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        context['patient'] = patient
        return context

    def form_valid(self, form):
        # set the user thats made the enrollment and the patient whom it is for
        form.instance.enrolled_by = self.request.user
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientEnrollmentCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is an active user
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class PatientSessionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of a session for a specific patient.

    This view is only available to users that are logged in and marked as active in the system.
    """
    model = CounsellingSession
    fields = ['counselling_session_type', 'notes']
    template_name = 'patients/patient_session_form.html'

    def get_success_url(self):
        # on adding the session, redirect to the patient details view
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        return patient.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(PatientSessionCreateView, self).get_context_data(**kwargs)
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        context['patient'] = patient
        return context

    def form_valid(self, form):
        # set the user adding the session and the patient whom it is for
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientSessionCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class PatientMedicalReportCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of a medical report for a specific patient.

    This view is only available to users that are logged in and marked as active in the system.
    """
    model = MedicalReport
    fields = ['title', 'report_type', 'notes']
    template_name = 'patients/patient_medical_report_form.html'

    def get_success_url(self):
        # on adding the medical report, redirect to the patient details view
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        return patient.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(PatientMedicalReportCreateView, self).get_context_data(**kwargs)
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        context['patient'] = patient
        return context

    def form_valid(self, form):
        # set the user adding the medical report and the patient whom it is for
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientMedicalReportCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class PatientAppointmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of an appointment for a specific patient.

    This view is only available to users that are logged in and marked as active in the system.
    """
    model = Appointment
    form_class = PatientAppointmentForm
    template_name = 'patients/patient_appointment_form.html'

    def get_success_url(self):
        # on adding the appointment, redirect to the patient details view
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        return patient.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(PatientAppointmentCreateView, self).get_context_data(**kwargs)
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        context['patient'] = patient
        return context

    def form_valid(self, form):
        # set the user adding the appointment and the patient whom it is for
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        if not form.instance.owner:
            form.instance.owner = self.request.user

        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientAppointmentCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active
