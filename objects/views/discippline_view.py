from rest_framework import viewsets

from objects.models import DisciplineModel
from objects.serialisers import DisciplineSerializer


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = DisciplineModel.objects.all()
    serializer_class = DisciplineSerializer