from rest_framework import serializers
from objects.models import SchoolModel


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = '__all__'

    statistics = serializers.JSONField()
