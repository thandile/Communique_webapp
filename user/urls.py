from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='dashboard_home',
        permanent=False)),
    url(r'^login/$', auth_views.login, {'template_name':'user/login.html'},
        name='user_login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'user/logout.html'},
        name='user_logout'),
    url(r'^accounts/$', AccountListView.as_view(),
        name='user_accounts_list_view'),
    url(r'^accounts/create/$', AccountCreateView.as_view(),
        name='user_accounts_create_view'),
]
