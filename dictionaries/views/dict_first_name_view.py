
from rest_framework import viewsets
from dictionaries.models import DictFirstNameModel
from dictionaries.serializers import DictFirstNameSerializer


class DictFirstNameViewSet(viewsets.ModelViewSet):
    queryset = DictFirstNameModel.objects.all()
    serializer_class = DictFirstNameSerializer

