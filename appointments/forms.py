from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    """
    A form used to create and update an appointment
    """

    class Meta:
        model = Appointment
        fields = ['title', 'owner', 'patient', 'appointment_date', 'start_time', 'end_time', 'notes']

    def clean(self):
        # check that the start_time is less than the end_time
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        if start_time >= end_time:
            raise forms.ValidationError('The start time cannot be greater than or equal to the end time')

        return super(AppointmentForm, self).clean()
