from django.db import models
from uuid import uuid4

class DictSecondNameModel(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

# добавить валидацию regexp [a-z, A-Z, а-я, А-Я]
