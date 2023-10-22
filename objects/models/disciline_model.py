from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator
from subjects.models.teacher_model import TeacherModel


class DisciplineModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    title = models.CharField(max_length=20)
    study_year = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(11)]
    )
    teacher = models.ForeignKey(TeacherModel, on_delete=models.RESTRICT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['teacher', 'title'],
                                               name='teacher_title')]

    def __str__(self):
        return f'{self.title} - {super().__str__()}'
