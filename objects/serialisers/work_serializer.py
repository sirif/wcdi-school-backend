from rest_framework import serializers
from objects.models import WorkModel


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkModel
        fields = '__all__'
