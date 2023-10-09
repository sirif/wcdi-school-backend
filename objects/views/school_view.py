from django.shortcuts import render
from rest_framework import viewsets

from objects.models import SchoolModel
from objects.serialisers.school_serializer import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer
