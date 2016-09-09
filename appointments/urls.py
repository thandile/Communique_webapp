from django.conf.urls import url

from .views import AppointmentCreateView, AppointmentDetailView, AppointmentUpdateView

urlpatterns = [
    url(r'^create', AppointmentCreateView.as_view(), name='appointments_appointment_create'),
    url(r'^(?P<pk>[0-9]+)/$', AppointmentDetailView.as_view(), name='appointments_appointment_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', AppointmentUpdateView.as_view(), name='appointments_appointment_update'),
]