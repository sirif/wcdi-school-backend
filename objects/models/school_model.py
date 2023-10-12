from uuid import uuid4
from django.db import models



# statistics: {
#     groups_total: COUNT,
#     students_total: COUNT,
#     teachers_total: COUNT.
# }

class SchoolModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.number} - {super().__str__()}'


    # ToDo: должно возвращать расчитанное значение; не хранится в бд
    @property
    def statistics(self):
        from objects.models import GroupModel
        from subjects.models.student_model import StudentModel
        from subjects.models.teacher_model import TeacherModel

        # Todo читать 
        # тут магия
        # groups_total = self.group_set.count()

        groups_total = GroupModel.objects.filter(school__uuid = self.uuid).count()

        students_total = StudentModel.objects.filter(group__school_id=self.uuid).count()

        teachers_total = TeacherModel.objects.filter(group_set__school_id=self.uuid).distinct().count()



        return {"groups_total":groups_total, "students_total":students_total, "teachers_total":teachers_total}
