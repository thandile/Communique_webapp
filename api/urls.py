from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from support_services.views import ServiceViewSet
from user.views import UserViewSet
from services.views import PatientViewSet, PilotProgramViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'users', UserViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'pilots', PilotProgramViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
