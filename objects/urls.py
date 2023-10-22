from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path

router = DefaultRouter()

router.register(r'group', GroupViewSet)
router.register(r'school', SchoolViewSet)
router.register(r'discipline', DisciplineViewSet)
router.register(r'work', WorkViewSet)
router.register(r'estimate', EstimateViewSet)

#uuid  воспринимается как тип! https://djangodoc.ru/3.2/topics/http/urls/
urlpatterns = router.urls + [path(r'work_export/', WorkExportView.as_view(), name='work_export'),
                             path(r'work-estimate/<uuid:item_uuid>/', work_estimate),]
