from uuid import uuid4
from django.db import models


class SchoolModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    number = models.IntegerField(unique=True)


    # ToDo: должно возвращать расчитанное значение; не хранится в бд
    @property
    def statistics(self):
        pass
