from rest_framework import viewsets

from objects.models import GroupModel
from objects.serialisers.group_serializer import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer

