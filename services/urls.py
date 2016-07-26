from django.conf.urls import url
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='dashboard_home',
        permanent=False)),
    url(r'^pilot-programs/$', PilotProgramListView.as_view(),
        name='services_pilot_program_list'),
    url(r'^pilot-programs/create/$', PilotProgramCreateView.as_view(),
        name='services_pilot_program_create'),
    url(r'^pilot-programs/(?P<pk>[0-9]+)/$', PilotProgramDetailView.as_view(),
        name='services_pilot_program_detail'),
    url(r'^pilot-programs/(?P<pk>[0-9]+)/update/$',
        PilotProgramUpdateView.as_view(), name='services_pilot_program_update'),
    url(r'^pilot-programs/(?P<pk>[0-9]+)/delete/$',
        PilotProgramDetailView.as_view(), name='services_pilot_program_delete'),
    url(r'^patients/$', PatientListView.as_view(),
        name='services_patient_list'),
    url(r'^patients/create/$', PatientCreateView.as_view(),
        name='services_patient_create'),
    url(r'^patients/(?P<pk>[0-9]+)/$', PatientDetailView.as_view(),
        name='services_patient_detail'),
    url(r'^patients/(?P<pk>[0-9]+)/update/$', PatientUpdateView.as_view(),
        name='services_patient_update'),
    url(r'^patients/(?P<pk>[0-9]+)/delete/$', PatientDeleteView.as_view(),
        name='services_patient_delete'),
]
