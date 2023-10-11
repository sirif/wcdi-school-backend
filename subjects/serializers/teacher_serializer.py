from rest_framework import serializers
from subjects.models import TeacherModel


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'
        