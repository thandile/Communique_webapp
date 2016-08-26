from django.conf.urls import url

from patients.views import EnrollmentListView, EnrollmentCreateView

urlpatterns = [
    url(r'^$', EnrollmentListView.as_view(), name='patients_enrollment_list'),
    url(r'^create/$', EnrollmentCreateView.as_view(), name='patients_enrollment_create'),
]