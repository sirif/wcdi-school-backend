from rest_framework import serializers
from dictionaries.models import DictFirstNameModel


class DictFirstNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DictFirstNameModel
        fields = '__all__'
