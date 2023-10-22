from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path

router = DefaultRouter()

#uuid  воспринимается как тип! https://djangodoc.ru/3.2/topics/http/urls/
urlpatterns = router.urls + [path(r'transfer-student/', TransferStudent.as_view(), name='transfer_student')]
