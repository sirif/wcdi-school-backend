from builtins import filter
from tokenize import group

from rest_framework import generics
from objects.models.work_model import WorkModel
from objects.models.disciline_model import DisciplineModel
from objects.models.estimate_model import EstimateModel
from objects.models.group_model import GroupModel
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import FileResponse, HttpResponse
from .serializers import TransferStudentSerializer
from subjects.models.student_model import StudentModel
from django.db import transaction
from dictionaries.models.dict_first_name import DictFirstNameModel
from dictionaries.models.dict_second_name import DictSecondNameModel


# в перспективе будет переделано на работу с файлами в личном деле
def transfer_check(file) -> dict:
    # # ToDo: перенести логику создания в transfer_check
    # for param, class_name in zip(["first_name", "second_name"], [DictFirstNameModel, DictSecondNameModel]):
    #     param_val: class_name = None
    #     try:
    #         param_val = class_name.objects.get(pk=student_data.get(param))
    #     except Exception as e:
    #         param_val = class_name.objects.create(name=student_data.get(param))
    #         print(str(e))
    #     finally:
    #         student_data.update({param: param_val})
    #
    # GroupModel.objects.get()
    # try:
    #     param_val = GroupModel.objects.get(pk=student_data.get("group.study_year"))
    # except Exception as e:
    #     param_val = GroupModel.objects.create(name=student_data.get(param))
    #     print(str(e))
    # finally:
    #     student_data.update({param: param_val})

    group = GroupModel.objects.get(study_year="1", letter="A")
    result = {
        StudentModel.__name__: {
            "first_name": DictFirstNameModel.objects.get(pk="Вася"),
            "second_name": DictSecondNameModel.objects.get(pk="Пупкин"),
            "birthday": "2015-10-12",
            "group": group,
        },
        WorkModel.__name__: [{
            "discipline": DisciplineModel.objects.get(title="Русский язык"),
            "work_number": 1,
            "item_meta": {"meta": "transfer from school number 32"},
            EstimateModel.__name__: {
             "grade": 5,
             "grade_date_time": "2023-10-12",
             "grade_description": ""
            }
        }]
    }
    return result


class TransferStudent(generics.CreateAPIView):
    serializer_class = TransferStudentSerializer

    @swagger_auto_schema(responses={200: openapi.Response(
        'Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        schema=openapi.Schema(type=openapi.TYPE_FILE)
    )})

    @transaction.atomic
    def _store_models_(self, dictionary):
        student_data = dictionary.get(StudentModel.__name__)
        student_obj = StudentModel.objects.create(**student_data)

        for work_dict in dictionary.get(WorkModel.__name__):
            discipline_obj = work_dict.get('discipline')
            work_dict.update({'discipline': discipline_obj})
            work_dict.update({'student': student_obj})
            estimate_obj = work_dict.get(EstimateModel.__name__)
            work_dict.pop(EstimateModel.__name__)
            print(work_dict)
            work_obj = WorkModel.objects.create(**work_dict)
            estimate_obj.update({'work': work_obj})
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