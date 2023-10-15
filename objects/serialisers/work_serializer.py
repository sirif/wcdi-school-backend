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
        if not isinstance(data.get('item_meta'), dict):
            raise serializers.ValidationError("not dict")

        item_meta: dict = data.get('item_meta')
        if not (data.get('item_data') and item_meta.get('original_file_name')):
            raise serializers.ValidationError("missing data or original_file_name")

        return data


class WorkExportSerializer(serializers.Serializer):
    item_uuid = serializers.CharField(required=True)
