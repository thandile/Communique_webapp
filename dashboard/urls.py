from django.conf.urls import url, include
from .views import DashboardView
from services import urls as services_urls
from user import urls as user_urls

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard_home'),
    url(r'^services/', include(services_urls)),
    url(r'^user/', include(user_urls)),
]
