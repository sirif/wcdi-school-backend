from builtins import print

from rest_framework import generics
from objects.models.work_model import WorkModel
from objects.models.disciline_model import DisciplineModel
from objects.models.group_model import GroupModel
from objects.models.estimate_model import EstimateModel
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import HttpResponse
from .serializers import TransferStudentSerializer
from subjects.models.student_model import StudentModel
from django.db import transaction
from dictionaries.models.dict_first_name import DictFirstNameModel
from dictionaries.models.dict_second_name import DictSecondNameModel
import pandas as pd
from rest_framework.exceptions import APIException

STUDENT = "student"
GROUP = "group"
DISCIPLINE = "discipline"
ITEM_META = "item_meta"

STUDENT_TEMPLATE = {"Имя": "first_name",
                    "Фамилия": "second_name",
                    "Дата рождения": "birthday"}

GROUP_TEMPLATE = {"Класс поступления": "study_year",
                  "Литера": "letter"}

WORK_TEMPLATE = {"Work number": "work_number",
                 "Start date": "start_date"}

ESTIMATE_TEMPLATE = {"Grade": "grade",
                     "grade_date_time": "grade_date_time",
                     "Description": "grade_description"}


class TransferException(APIException):
    """ custom transfer exception"""
    pass


def __parse_student__(student_df):
    """
    Парсинг страницы студента
    """
    student = {}

    try:
        for key in STUDENT_TEMPLATE:
            res = student_df.loc[student_df[0] == key][1].values[0]
            student[STUDENT_TEMPLATE[key]] = res
    except Exception as e:
        print(str(e))

    # Обновляем имя, вместо него ставим непосредственно объект из словаря имён:
    first_name_key = list(STUDENT_TEMPLATE.values())[0] # Костыль
    first_name_obj = DictFirstNameModel.objects.get(pk=student[first_name_key])
    student[first_name_key] = first_name_obj

    # Обновляем фамилию, вместо неё ставим непосредственно объект из словаря фамилий:
    second_name_key = list(STUDENT_TEMPLATE.values())[1]
    second_name_obj = DictSecondNameModel.objects.get(pk=student[second_name_key])
    student[second_name_key] = second_name_obj

    group = {}
    try:
        for key in GROUP_TEMPLATE:
            res = student_df.loc[student_df[0] == key][1].values[0]
            group[GROUP_TEMPLATE[key]] = res
    except Exception as e:
        print(str(e))
    group_keys = list(GROUP_TEMPLATE.values())
    group_obj = GroupModel.objects.get(study_year=group.get(group_keys[0]),
                                       letter=group.get(group_keys[1]))
    student[GROUP] = group_obj
    d = {StudentModel.__name__: student}
    return d


def __parse_disciplines__(file: pd.ExcelFile, study_year: int) -> dict:
    """
    Парсинг страниц дисциплин excel документа
    """
    disciplines = []
    for sheet in file.sheet_names:
        if sheet == STUDENT:
            continue
        disciplines.append(sheet)
    if not __check_disciplines__(disciplines, study_year):
        raise TransferException("Кол-во дисциплин не соответствует программе школы")

    estimates = []

    works = []
    for discipline in disciplines:
        discipline_df = file.parse(sheet_name=discipline, header=None)
        head = discipline_df.loc[0].to_list()
        for indexRow, row in discipline_df.iterrows():
            # Пропускаем заголовок
            if indexRow == 0:
                continue
            work_dict = {}
            estimate_dict = {}
            for h, val in zip(head, row.to_list()):
                if WORK_TEMPLATE.get(h) is not None:
                    work_dict[WORK_TEMPLATE.get(h)] = val
                elif ESTIMATE_TEMPLATE.get(h) is not None:
                    estimate_dict[ESTIMATE_TEMPLATE.get(h)] = val
                if list(ESTIMATE_TEMPLATE.keys())[0] == h:
                    estimates.append(int(val))

            estimate_dict[list(ESTIMATE_TEMPLATE.keys())[1]] =\
                work_dict[list(WORK_TEMPLATE.values())[1]]
            work_dict[EstimateModel.__name__] = estimate_dict
            work_dict[DISCIPLINE] = DisciplineModel.objects.get(title=discipline)
            work_dict[ITEM_META] = {"meta": "transfer from another school"}
            works.append(work_dict)
    mean_estimate = sum(estimates)/len(estimates)
    if mean_estimate < 5:
        raise TransferException(f"Средний балл не удовлетворительный - {mean_estimate:.2f}, необходим выше 3")
    return {WorkModel.__name__: works}


def __check_disciplines__(disc: list, study_year: int) -> bool:
    """
    Проверяем набор необходимых предметов
    """
    disciplines_by_year = DisciplineModel.objects.filter(study_year=study_year)
    result_list = [v for v in disciplines_by_year if v.title in disc]
    return len(result_list) == len(disc)


# в перспективе будет переделано на работу с файлами в личном деле
def transfer_check(file) -> dict:
    """
    Проверяет файл перевода на корректность, возвращает словарь для заполнения данных об ученике в БД
    """
    xlsx_file = pd.ExcelFile(file)
    result: dict = {}
    try:
        result.update(__parse_student__(xlsx_file.parse(sheet_name=STUDENT, header=None)))
        result.update(__parse_disciplines__(xlsx_file, result.get(StudentModel.__name__, {}).get(GROUP).study_year))

    except Exception as e:
        print(str(e))
        raise e

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
            discipline_obj = work_dict.get(DISCIPLINE)
            work_dict.update({DISCIPLINE: discipline_obj})
            work_dict.update({STUDENT: student_obj})
            estimate_obj = work_dict.get(EstimateModel.__name__)
            work_dict.pop(EstimateModel.__name__)
            print(work_dict)
            work_obj = WorkModel.objects.create(**work_dict)
            estimate_obj.update({'work': work_obj})
            EstimateModel.objects.create(**estimate_obj)
        return

    def create(self, request, *args, **kwargs):
        """
        Функция, осуществляющая перевод студента в школу
        """
        file = request.data.get('file')
        result = transfer_check(file)

        self._store_models_(result)

        return HttpResponse()
