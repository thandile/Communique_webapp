from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import ProgramViewSet, PatientViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
