from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'first_name', DictFirstNameViewSet)
router.register(r'second_name', DictSecondNameViewSet)

urlpatterns = router.urls
