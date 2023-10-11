from rest_framework import viewsets
from subjects.models.student_model import StudentModel
from subjects.serializers.student_serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
