from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Appointment
from .forms import AppointmentForm


class AppointmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of an appointment.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'

    def form_valid(self, form):
        # the creator and last modified fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        # set the owner of the appointment as current user if not chosen in form
        if not form.instance.owner:
            form.instance.owner = self.request.user

        return super(AppointmentCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class AppointmentDetailView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles displaying appointment details.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Appointment
    template_name = 'appointments/appointment_view.html'
    context_object_name = 'appointment'

    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active