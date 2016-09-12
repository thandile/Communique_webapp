from appointments.models import Appointment
from appointments.forms import AppointmentForm


class PatientAppointmentForm(AppointmentForm):
    """
    A form used to create an appointment for a patient.
    """
    class Meta(AppointmentForm.Meta):
        model = Appointment
        fields = ['title', 'owner', 'appointment_date', 'start_time', 'end_time', 'notes']
