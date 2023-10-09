from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, GroupViewSet

router = DefaultRouter()

router.register(r'group', GroupViewSet)
router.register(r'school', SchoolViewSet)

urlpatterns = router.urls
