from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet

router = DefaultRouter()
router.register(r'api/users/user', UserProfileViewSet)

urlpatterns = router.urls
