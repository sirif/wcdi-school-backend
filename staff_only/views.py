from rest_framework import generics
from objects.models.work_model import WorkModel
from objects.models.disciline_model import DisciplineModel
from objects.models.estimate_model import EstimateModel
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import FileResponse, HttpResponse
from .serializers import TransferStudentSerializer
from subjects.models.student_model import StudentModel
from django.db import transaction


# в перспективе будет переделано на работу с файлами в личном деле
def transfer_check(file) -> dict:
    # result = {}
    # result = {
    #     StudentModel.__class__.__name__: {
    #         "first_name": "Вася",
    #         "second_name": "Пупкин",
    #         "birthday": "2015-10-12",
    #         "group.study_year": "1",
    #         "group.letter": "A"
    #     },
    #     WorkModel.__class__.__name__: [{
    #         "discipline": "Русский язык",
    #         "work_number": 1
    #         "Estimate.__class__.__name__: {
    #          "grade": 5,
    #           "grade_date_time": "2023-10-12",
    #           "grade_description": ""
    #         }
    #     }]
    # }
    return result


class TransferStudent(generics.CreateAPIView):
    serializer_class = TransferStudentSerializer

    @swagger_auto_schema(responses={200: openapi.Response(
        'Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        schema=openapi.Schema(type=openapi.TYPE_FILE)
    )})


    @transaction.atomic
    def _store_models_(self, dictionary) :
        student_data = dictionary.get(StudentModel.__class__.__name__)
        student_uuid = StudentModel.objects.create(**student_data).uuid

        for work_obj in dictionary.get(WorkModel.__class__.__name__):
            discipline_uuid = DisciplineModel.objects.get(title=work_obj.get('discipline'))
            work_obj.update('discipline', discipline_uuid)
            work_obj.update('student', student_uuid)
            work_uuid = WorkModel.objects.create(**work_obj).uuid
            estimate_obj = work_obj.get(EstimateModel.__class__.__name__)
            estimate_obj.update('work', work_uuid)
            EstimateModel.objects.create(**estimate_obj)
        return


    def create(self, request, *args, **kwargs):
        file = request.data.get('file')
        result = transfer_check(file)

        self._store_models_(result)





        return HttpResponse()
        #
        # try:
        #     work = WorkModel.objects.get(pk=item_uuid)
        # except WorkModel.DoesNotExist as e:
        #     return HttpResponse(str(e), status=status.HTTP_400_BAD_REQUEST)
        # print(file_name)
        # original_file_name = work.item_meta.get('original_file_name', 'default.xlsx')
        #
        # if not os.path.exists(file_name):
        #     raise Http404
        # # writer = self.xls_writer(request.data)
        # # writer.generate_report()
        # response = FileResponse(open(file_name, 'rb'), filename=original_file_name, as_attachment=True,
        #                         status=status.HTTP_200_OK)
        # del response['Transfer-Encoding']
        # return response