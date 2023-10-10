from rest_framework import serializers
from dictionaries.models import DictSecondNameModel


class DictSecondNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DictSecondNameModel
        fields = '__all__'
