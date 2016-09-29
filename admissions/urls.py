from django.conf.urls import url

from .views import (AdmissionCreateView, AdmissionUpdateView, AdmissionDeleteView, AdmissionDetailView,
                    AdmissionListView)

urlpatterns = [
    url(r'^$', AdmissionListView.as_view(), name='admissions_admission_list'),
    url(r'^create/$', AdmissionCreateView.as_view(), name='admissions_admission_create'),
    url(r'^(?P<pk>[0-9]+)/$', AdmissionDetailView.as_view(), name='admissions_admission_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', AdmissionUpdateView.as_view(), name='admissions_admission_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', AdmissionDeleteView.as_view(), name='admissions_admission_delete'),
]