from rest_framework.routers import DefaultRouter
from subjects.views.teacher_view import TeacherViewSet

router = DefaultRouter()

router.register(r'teacher', TeacherViewSet)

urlpatterns = router.urls
