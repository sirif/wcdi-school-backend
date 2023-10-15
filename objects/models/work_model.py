import os.path
from uuid import uuid4
from django.db import models
from objects.models import DisciplineModel
from subjects.models.student_model import StudentModel
from django.core.validators import FileExtensionValidator


class WorkModel(models.Model):

    def _work_path_(self, file_name):
        print("work_path: ", file_name)
        self.item_meta = {"original_file_name": file_name}
        return os.path.join(str(self.__class__.__name__).lower(), str(self.uuid))

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    item_meta = models.JSONField()
    discipline = models.ForeignKey(
        DisciplineModel,
        on_delete=models.RESTRICT,
        related_name='work_set'
    )
    student = models.ForeignKey(
        StudentModel,
        on_delete=models.RESTRICT,
        related_name='work_set'
    )
    item_data = models.FileField(
        upload_to=_work_path_,
        help_text='Excel-file',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['xlsx'])]
    )
