from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ProgramListView.as_view(), name='programs_program_list'),
    url(r'^create/$', ProgramCreateView.as_view(), name='programs_program_create'),
    url(r'^(?P<pk>[0-9]+)/$', ProgramDetailView.as_view(), name='programs_program_detail'),
]