from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse


from .views import *

urlpatterns = [
    # urls for logging in and out
    url(r'^$', RedirectView.as_view(pattern_name='dashboard_home',
        permanent=False)),
    url(r'^login/$', auth_views.login, {'template_name':'user/login.html'},
        name='user_login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'user/logout.html'},
        name='user_logout'),
    # urls to CRUD Communique users
    url(r'^communique-users/$', CommuniqueUserListView.as_view(),
        name='user_communique_user_list'),
    url(r'^communique-users/search/$', CommuniqueUserSearchListView.as_view(),
        name='user_communique_user_list_search'),
    url(r'^communique-users/create/$', CommuniqueUserCreateView.as_view(),
        name='user_communique_user_create'),
    url(r'^communique-users/(?P<pk>[0-9]+)/$',
        CommuniqueUserDetailView.as_view(), name='user_communique_user_detail'),
    url(r'^communique-users/(?P<pk>[0-9]+)/update/$',
        CommuniqueUserUpdateView.as_view(), name='user_communique_user_update'),
    # urls to view and update user profile
    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileDetailView.as_view(),
        name='user_profile_detail'),
    url(r'^profile/(?P<pk>[0-9]+)/update/$', ProfileUpdateView.as_view(),
        name='user_profile_update'),
    url(r'^profile/password-change/$', auth_views.password_change,
        {'template_name':'user/password_change_form.html',
            'post_change_redirect':'/user/profile/password-change-done/'},
                name='password_change'),
    url(r'^profile/password-change-done/$', auth_views.password_change_done,
        {'template_name':'user/password_change_done.html'},
            name='password_change_done'),
]
