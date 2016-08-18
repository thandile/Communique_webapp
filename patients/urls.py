from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', PatientListView.as_view(), name='patients_patient_list'),
    url(r'^create/$', PatientCreateView.as_view(), name='patients_patient_create'),
    url(r'^(?P<pk>[0-9]+)/$', PatientDetailView.as_view(), name='patients_patient_detail'),
]