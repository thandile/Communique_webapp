from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', CounsellingSessionTypeListView.as_view(), name='counselling_sessions_type_list'),
]