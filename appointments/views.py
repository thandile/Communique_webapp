from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

import datetime

from .models import Appointment


class AppointmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of an appointment.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['title', 'patient', 'owner', 'appointment_date', 'start_time', 'notes']

    def form_valid(self, form):
        # the creator and last modified fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        # set the owner of the appointment as current user if not chosen in form
        if not form.instance.owner:
            form.instance.owner = self.request.user

        # if the start time is not set in form, set it to the current time
        if not form.instance.start_time:
            form.instance.start_time = datetime.datetime.now().time()

        return super(AppointmentCreateView, self).form_valid(form)