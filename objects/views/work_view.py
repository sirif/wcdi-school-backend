from django.shortcuts import render
from rest_framework import viewsets

from objects.models import WorkModel
from objects.serialisers.work_serializer import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = WorkModel.objects.all()
    serializer_class = WorkSerializer
