from django.conf.urls import url

from patients.views import EnrollmentListView, EnrollmentCreateView, EnrollmentDetailView, EnrollmentUpdateView

urlpatterns = [
    url(r'^$', EnrollmentListView.as_view(), name='patients_enrollment_list'),
    url(r'^create/$', EnrollmentCreateView.as_view(), name='patients_enrollment_create'),
    url(r'^(?P<pk>[0-9]+)/$', EnrollmentDetailView.as_view(), name='patients_enrollment_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', EnrollmentUpdateView.as_view(), name='patients_enrollment_update'),
]