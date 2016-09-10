from django.conf.urls import url

from .views import (AppointmentCreateView, AppointmentDetailView, AppointmentUpdateView, AppointmentListView,
                    AppointmentDeleteView)

urlpatterns = [
    url(r'^$', AppointmentListView.as_view(), name='appointments_appointment_list'),
    url(r'^create', AppointmentCreateView.as_view(), name='appointments_appointment_create'),
    url(r'^(?P<pk>[0-9]+)/$', AppointmentDetailView.as_view(), name='appointments_appointment_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', AppointmentUpdateView.as_view(), name='appointments_appointment_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', AppointmentDeleteView.as_view(), name='appointments_appointment_delete'),
]