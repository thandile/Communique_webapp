from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy

from .models import Admission
from .forms import AdmissionUpdateForm, AdmissionCreateForm


class AdmissionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of an admission.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Admission
    form_class = AdmissionCreateForm
    template_name = 'admissions/admission_form.html'

    def form_valid(self, form):
        # the creator and modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(AdmissionCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class AdmissionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view that handles displaying details of an admission.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Admission
    template_name = 'admissions/admission_view.html'
    context_object_name = 'admission'

    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class AdmissionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view that handles updating of an admission.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Admission
    form_class = AdmissionUpdateForm
    template_name = 'admissions/admission_update_form.html'
    context_object_name = 'admission'

    def form_valid(self, form):
        # update the last modified by field
        form.instance.last_modified_by = self.request.user

        return super(AdmissionUpdateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True is user is active, false otherwise
        """
        return self.request.user.is_active


class AdmissionListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that lists the existing admissions.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Admission
    template_name = 'admissions/admission_list.html'
    context_object_name = 'admission_list'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True is user is active, false otherwise.
        """
        return self.request.user.is_active


class AdmissionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view that handles deletion of an admission.

    This view is only available to users that are logged in and marked as active in the system.
    """
    model = Admission
    success_url = reverse_lazy('admissions_admission_list')
    context_object_name = 'admission'
    template_name = 'admissions/admission_confirm_delete.html'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active