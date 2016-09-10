from django.conf.urls import url
from django.views.generic import RedirectView

from .views import (MedicalReportTypeCreateView, MedicalReportUpdateView, MedicalReportCreateView,
                    MedicalReportTypeUpdateView, MedicalReportDeleteView, MedicalReportDetailView, MedicalReportListView
                    , MedicalReportTypeDeleteView, MedicalReportTypeDetailView, MedicalReportTypeListView)

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='dashboard_home', permanent=False)),
    url(r'^report-types/$', MedicalReportTypeListView.as_view(), name='medical_report_type_list'),
    url(r'^report-types/create/$', MedicalReportTypeCreateView.as_view(), name='medical_report_type_create'),
    url(r'^report-types/(?P<pk>[0-9]+)/$', MedicalReportTypeDetailView.as_view(), name='medical_report_type_detail'),
    url(r'^report-types/(?P<pk>[0-9]+)/update/$', MedicalReportTypeUpdateView.as_view(),
        name='medical_report_type_update'),
    url(r'^report-types/(?P<pk>[0-9]+)/delete/$', MedicalReportTypeDeleteView.as_view(),
        name='medical_report_type_delete'),
    url(r'^reports/$', MedicalReportListView.as_view(), name='medical_report_list'),
    url(r'^reports/create/$', MedicalReportCreateView.as_view(), name='medical_report_create'),
    url(r'^reports/(?P<pk>[0-9]+)/$', MedicalReportDetailView.as_view(), name='medical_report_detail'),
    url(r'^reports/(?P<pk>[0-9]+)/update/$', MedicalReportUpdateView.as_view(), name='medical_report_update'),
    url(r'^reports/(?P<pk>[0-9]+)/delete/$', MedicalReportDeleteView.as_view(), name='medical_report_delete'),
]