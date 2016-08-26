from django.conf.urls import url

from patients.views import PatientListView, PatientCreateView, PatientDetailView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    url(r'^$', PatientListView.as_view(), name='patients_patient_list'),
    url(r'^create/$', PatientCreateView.as_view(), name='patients_patient_create'),
    url(r'^(?P<pk>[0-9]+)/$', PatientDetailView.as_view(), name='patients_patient_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', PatientUpdateView.as_view(), name='patients_patient_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PatientDeleteView.as_view(), name='patients_patient_delete'),
]