from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from support_services.views import ServiceListAPIView, ServiceDetailAPIView
from user.views import UserListAPIView, UserDetailAPIView

urlpatterns = [
    url(r'^services/$', ServiceListAPIView.as_view()),
    url(r'^services/(?P<pk>[0-9]+)/$', ServiceDetailAPIView.as_view()),
    url(r'^users/$', UserListAPIView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
