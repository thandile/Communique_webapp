from django.conf.urls import url

from .views import AppointmentCreateView

urlpatterns = [
    url(r'^create', AppointmentCreateView.as_view(), name='appointments_appointment_create'),
]