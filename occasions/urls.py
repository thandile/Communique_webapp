from django.conf.urls import url

from .views import (EventCreateView, EventDetailView, EventUpdateView, EventListView, EventDeleteView)


urlpatterns = [
    url(r'^$', EventListView.as_view(), name='occasions_event_list'),
    url(r'^create/$', EventCreateView.as_view(), name='occasions_event_create'),
    url(r'^(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='occasions_event_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', EventUpdateView.as_view(), name='occasions_event_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', EventDeleteView.as_view(), name='occasions_event_delete'),
]