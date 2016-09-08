from django.conf.urls import url

from .views import AppointmentCreateView, AppointmentDetailView

urlpatterns = [
    url(r'^create', AppointmentCreateView.as_view(), name='appointments_appointment_create'),
    url(r'^(?P<pk>[0-9]+)/$', AppointmentDetailView.as_view(), name='appointments_appointment_detail'),
]