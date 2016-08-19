from django.conf.urls import url

from patients.views import EnrollmentListView

urlpatterns = [
    url(r'^$', EnrollmentListView.as_view(), name='patients_enrollment_list'),
]