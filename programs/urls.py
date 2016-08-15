from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ProgramListView.as_view(), name='programs_program_list'),
]