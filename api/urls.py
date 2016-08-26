from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import ProgramViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'programs', ProgramViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
