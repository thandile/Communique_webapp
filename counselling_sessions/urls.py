from django.conf.urls import url
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='dashboard_home', permanent=False)),
    url(r'^session-types/$', CounsellingSessionTypeListView.as_view(), name='counselling_sessions_type_list'),
    url(r'^session-types/create/$', CounsellingSessionTypeCreateView.as_view(), name='counselling_sessions_type_create'),
    url(r'^session-types/(?P<pk>[0-9]+)/$', CounsellingSessionTypeDetailView.as_view(),
        name='counselling_sessions_type_detail'),
    url(r'^session-types/(?P<pk>[0-9]+)/update/$', CounsellingSessionTypeUpdateView.as_view(),
        name='counselling_sessions_type_update'),
    url(r'^session-types/(?P<pk>[0-9]+)/delete/$', CounsellingSessionTypeDeleteView.as_view(),
        name='counselling_sessions_type_delete'),
    url(r'^sessions/$', CounsellingSessionListView.as_view(), name='counselling_sessions_session_list'),
    url(r'^sessions/create/$', CounsellingSessionCreateView.as_view(), name='counselling_sessions_session_create'),
    url(r'^sessions/(?P<pk>[0-9]+)/$', CounsellingSessionDetailView.as_view(),
        name='counselling_sessions_session_detail'),
]