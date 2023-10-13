import os.path
from django.http import Http404

from rest_framework import viewsets, generics, status

from objects.models import WorkModel
from objects.serialisers.work_serializer import WorkSerializer, WorkExportSerializer
from django.http import FileResponse, HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.conf import settings


class WorkViewSet(viewsets.ModelViewSet):
    queryset = WorkModel.objects.all()
    serializer_class = WorkSerializer


class WorkExportView(generics.CreateAPIView):
    serializer_class = WorkExportSerializer

    @swagger_auto_schema(responses={200: openapi.Response(
        'Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        schema=openapi.Schema(type=openapi.TYPE_FILE)
    )})
    def create(self, request, *args, **kwargs):
        item_uuid = request.data.get('item_uuid')
        file_name = os.path.join(settings.MEDIA_ROOT, WorkModel.__name__.lower(), item_uuid)
        try:
            work = WorkModel.objects.get(pk=item_uuid)
        except WorkModel.DoesNotExist as e:
            return HttpResponse(str(e), status=status.HTTP_400_BAD_REQUEST)
        print(file_name)
        original_file_name = work.item_meta.get('original_file_name', 'default.xlsx')

        if not os.path.exists(file_name) :
            raise Http404
        # writer = self.xls_writer(request.data)
        # writer.generate_report()
        response = FileResponse(open(file_name, 'rb'), filename=original_file_name, as_attachment=True, status=status.HTTP_200_OK)
        del response['Transfer-Encoding']
        return response
