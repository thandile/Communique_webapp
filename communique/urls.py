from django.conf.urls import url, include
from django.views.generic import RedirectView

from dashboard import urls as dashboard_urls
from user import urls as user_urls
from api import urls as api_urls

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='user_login', permanent=False)),
    url(r'^user/', include(user_urls)),
    url(r'^dashboard/', include(dashboard_urls)),
    url(r'^api/', include(api_urls)),
]
