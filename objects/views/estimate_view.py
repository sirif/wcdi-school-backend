from rest_framework import viewsets

from objects.models import EstimateModel
from objects.serialisers import EstimateSerializer


class EstimateViewSet(viewsets.ModelViewSet):
    queryset = EstimateModel.objects.all()
    serializer_class = EstimateSerializer
