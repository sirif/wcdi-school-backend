from rest_framework import viewsets
from subjects.models.teacher_model import TeacherModel
from subjects.serializers.teacher_serializer import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer