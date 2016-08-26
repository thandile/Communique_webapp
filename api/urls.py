from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'users', CommuniqueUserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/(?P<username>\w+)/$', ProfileLoginView.as_view(), name='api_login'),
]
