from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^pilot-programs/$', PilotProgramListView.as_view(),
        name='services_pilot_program_list'),
]
