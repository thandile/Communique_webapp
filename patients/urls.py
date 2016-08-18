from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', PatientListView.as_view(), name='patients_patient_list'),
]