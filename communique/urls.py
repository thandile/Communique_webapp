from django.conf.urls import url, include
from django.views.generic import RedirectView

from user import urls as user_urls
from api import urls as api_urls
from programs import urls as programs_urls
from counselling_sessions import urls as counselling_session_urls
from appointments import urls as appointment_urls
from occasions import urls as occasion_urls
from medical import urls as medical_urls
from patients.urls import patient_urls as patients_urls
from patients.urls import enrollment_urls as enrollment_urls

from .views import DashboardTemplateView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='user_login', permanent=False)),
    url(r'^dashboard/$', DashboardTemplateView.as_view(), name='dashboard_home'),
    url(r'^user/', include(user_urls)),
    url(r'^programs/', include(programs_urls)),
    url(r'^patients/', include(patients_urls)),
    url(r'^enrollments/', include(enrollment_urls)),
    url(r'^counselling/', include(counselling_session_urls)),
    url(r'^appointments/', include(appointment_urls)),
    url(r'^events/', include(occasion_urls)),
    url(r'^medical/', include(medical_urls)),
    url(r'^api/', include(api_urls)),
]
