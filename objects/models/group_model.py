from random import choices
from uuid import uuid4

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from objects.models.school_model import SchoolModel
from subjects.models.teacher_model import TeacherModel


class LetterChoices(models.TextChoices):
    """Литеры классов"""
    A = 'А'
    B = 'Б'
    V = 'В'
    G = 'Г'
    D = 'Д'


class GroupModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    study_year = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(11)]
    )

    letter = models.CharField(
        max_length=2,
        choices=((str(chr(v)), str(chr(v))) for v in range(ord('A'), ord('Z') + 1)),
        blank=False,
        default='Z'
    )
    
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    school = models.ForeignKey(
        SchoolModel,
        on_delete=models.CASCADE,
        related_name='group_set'
    )
    teacher = models.ForeignKey(
        TeacherModel,
        on_delete=models.RESTRICT,
        related_name='group_set',
        blank=True,
        null=True        
    )

    def __str__(self) -> str:
        return f'{self.study_year} {self.letter} - {super().__str__()}'

    # ToDo: должно возвращать расчитанное значение; не хранится в бд
    @property
    def statistics(self):
        pass
