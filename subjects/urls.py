from rest_framework.routers import DefaultRouter
from subjects.views import *

router = DefaultRouter()

router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'student', StudentViewSet)

urlpatterns = router.urls
