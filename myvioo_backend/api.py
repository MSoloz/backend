from rest_framework import routers
from sponsor.views import SponsorViewSet

router = routers.DefaultRouter()
router.register(r'sponsors', SponsorViewSet,basename='sponsors')
