from uuid import uuid4
from django.db import models
from objects.models import DisciplineModel
from subjects.models import StudentModel


class WorkModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    work = models.JSONField()
    discipline = models.ForeignKey(
        DisciplineModel,
        on_delete=models.RESTRICT,
        related_name = 'work_set'
    )
    student = models.ForeignKey(
        StudentModel,
        on_delete=models.RESTRICT,
        related_name='work_set'
    )