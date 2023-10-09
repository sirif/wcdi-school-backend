from uuid import uuid4

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from objects.models.school_model import SchoolModel


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
        choices=LetterChoices.choices,
        blank=False,
        null=False
    )
    year = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(11)]
    )
    school = models.ForeignKey(
        SchoolModel,
        on_delete=models.CASCADE,
        related_name='group_set'
    )

    # ToDo: должно возвращать расчитанное значение; не хранится в бд
    @property
    def statistics(self):
        pass
