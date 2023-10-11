from django.db import models
from uuid import uuid4
from dictionaries.models import DictFirstNameModel
from dictionaries.models import DictSecondNameModel


class TeacherModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False)
    # ToDo: проверить функционал related_name='teacher_set' через QuerySet
    first_name = models.ForeignKey(
        DictFirstNameModel,
        on_delete=models.RESTRICT,
        related_name='teacher_set'
    )
    second_name = models.ForeignKey(
        DictSecondNameModel,
        on_delete=models.RESTRICT,
        related_name='teacher_set'
    )

