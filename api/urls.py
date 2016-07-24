from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from support_services.views import ServiceListAPIView, ServiceDetailAPIView

urlpatterns = [
    url(r'^services/$', ServiceListAPIView.as_view()),
    url(r'^services/(?P<pk>[0-9]+)/$', ServiceDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
