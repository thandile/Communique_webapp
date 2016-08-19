from django.conf.urls import url, include
from django.views.generic import RedirectView

from user import urls as user_urls
from api import urls as api_urls
from programs import urls as programs_urls
from patients.urls import patient_urls as patients_urls

from .views import DashboardTemplateView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='user_login', permanent=False)),
    url(r'^dashboard/$', DashboardTemplateView.as_view(), name='dashboard_home'),
    url(r'^user/', include(user_urls)),
    url(r'^programs/', include(programs_urls)),
    url(r'^patients/', include(patients_urls)),
    url(r'^api/', include(api_urls)),
]
