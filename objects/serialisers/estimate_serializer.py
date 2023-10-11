from rest_framework import serializers
from objects.models import EstimateModel


class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstimateModel
        fields = '__all__'
