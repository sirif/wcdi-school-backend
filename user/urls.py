from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet


router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")


urlpatterns = [
    path(r'', include(router.urls)),
]