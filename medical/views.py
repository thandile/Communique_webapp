from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy

from .models import MedicalReport, MedicalReportType


class MedicalReportTypeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that retrieves all available medical report types.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReportType
    template_name = 'medical/medical_report_type_list.html'
    context_object_name = 'medical_report_type_list'

    def test_func(self):
        """
        Checks whether the user is marked as active
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportTypeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of a report type.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReportType
    template_name = 'medical/medical_report_type_form.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        # fill the created by and modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(MedicalReportTypeCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportTypeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view that handles displaying details of a report type.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReportType
    template_name = 'medical/medical_report_type_view.html'
    context_object_name = 'medical_report_type'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportTypeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view that handles updating the details of a report type.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReportType
    fields = ['name', 'description']
    template_name = 'medical/medical_report_type_update_form.html'
    context_object_name = 'medical_report_type'

    def form_valid(self, form):
        # update the modified by fields
        form.instance.last_modified_by = self.request.user

        return super(MedicalReportTypeUpdateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportTypeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    This view handles the deletion of a report type.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReportType
    success_url = reverse_lazy('medical_report_type_list')
    context_object_name = 'medical_report_type'
    template_name = 'medical/medical_report_type_confirm_delete.html'

    def test_func(self):
        """
        Checks whether the user is marked as active
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that retrieves all available medical reports.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_list.html'
    context_object_name = 'medical_report_list'

    def test_func(self):
        """
        Checks whether the user is marked active
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles the creation of a medical report.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_form.html'
    fields = ['title', 'report_type', 'patient', 'notes']

    def form_valid(self, form):
        # set the created by and modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(MedicalReportCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked active
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view that handles displaying details of a medical report.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_view.html'
    context_object_name = 'medical_report'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view that handles updating a medical report.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_update_form.html'
    fields = ['title', 'report_type', 'notes']

    def form_valid(self, form):
        # set the modified fields
        form.instance.last_modified_by = self.request.user

        return super(MedicalReportUpdateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class MedicalReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view that handles the deletion of a medical report.

    This view is only available to users that are logged in and marked as active in the system.
    """
    model = MedicalReport
    success_url = reverse_lazy('medical_report_list')
    context_object_name = 'medical_report'
    template_name = 'medical/medical_report_confirm_delete.html'

    def test_func(self):
        """
        Checks whether the user is marked as active.
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active