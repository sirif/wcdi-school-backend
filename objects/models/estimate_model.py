from _ast import mod
from uuid import uuid4
from django.db import models
from objects.models import WorkModel
from django.core.validators import MinValueValidator, MaxValueValidator


class EstimateModel(models.Model):
    work = models.ForeignKey(
        WorkModel,
        on_delete=models.RESTRICT,
        related_name='estimate_set'
    )
    grade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    grade_date_time = models.DateTimeField()
    grade_description = models.TextField()



