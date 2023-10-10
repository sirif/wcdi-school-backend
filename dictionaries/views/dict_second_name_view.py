
from rest_framework import viewsets
from dictionaries.models import DictSecondNameModel
from dictionaries.serializers import DictSecondNameSerializer


class DictSecondNameViewSet(viewsets.ModelViewSet):
    queryset = DictSecondNameModel.objects.all()
    serializer_class = DictSecondNameSerializer

