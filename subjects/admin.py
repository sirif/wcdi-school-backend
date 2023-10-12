from django.contrib import admin
from .models.student_model import StudentModel
from .models.teacher_model import TeacherModel

admin.site.register(TeacherModel)
admin.site.register(StudentModel)
