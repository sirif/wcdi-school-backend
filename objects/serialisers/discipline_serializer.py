from dataclasses import fields

from rest_framework import serializers
from objects.models import DisciplineModel


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineModel
        fields = '__all__'
        