# Imports
from rest_framework.routers import DefaultRouter

# Views
from host_request.views import RequestViewSet


router = DefaultRouter()
router.register('request', RequestViewSet, basename='request')
