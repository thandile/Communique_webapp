from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^services/$', ServiceListView.as_view(), name='support_services_service_list'),
]
