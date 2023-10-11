from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, GroupViewSet, DisciplineViewSet

router = DefaultRouter()

router.register(r'group', GroupViewSet)
router.register(r'school', SchoolViewSet)
router.register(r'discipline', DisciplineViewSet)

urlpatterns = router.urls
