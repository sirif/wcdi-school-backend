from rest_framework import serializers
from objects.models import WorkModel
from drf_extra_fields.fields import Base64FileField


class AllowedBase64File(Base64FileField):
    ALLOWED_TYPES = ['xlsx']

    def get_file_extension(self, filename, decoded_file):
        return "xlsx"


class WorkSerializer(serializers.ModelSerializer):
    item_data = AllowedBase64File()

    class Meta:
        model = WorkModel
        fields = '__all__'

    def validate(self, data):
        print("validator", data)
        if 'original_file_name' in data.get('item_meta').keys():
            return data
        else:
            raise serializers.ValidationError("missing orig_file_name")


class WorkExportSerializer(serializers.Serializer):
    item_uuid = serializers.CharField(required=True)
