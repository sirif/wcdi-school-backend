from rest_framework import serializers
from objects.serialisers.work_serializer import AllowedBase64File


class TransferStudentSerializer(serializers.Serializer):
    file = AllowedBase64File()
