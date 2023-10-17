from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib.request import Request
from home_work_checker.checker import HomeWorkChecker
from objects.models.work_model import WorkModel
from objects.models.estimate_model import EstimateModel
from django.conf import settings
import os.path


@api_view(['GET'])
def work_estimate(request: Request, item_uuid):
    file_name = os.path.join(settings.MEDIA_ROOT, WorkModel.__name__.lower(), str(item_uuid))
    work = WorkModel.objects.get(pk=item_uuid)
    key = f'{work.discipline.title}-{work.work_number}'
    hwc = HomeWorkChecker()
    grade = hwc.check(key, file_name)
    if grade != 0:
        if i := len(EstimateModel.objects.filter(work_id=item_uuid)):
            EstimateModel.objects.create(work_id=item_uuid, grade=grade, grade_description=f'reestimate: {i}')
        else:
            EstimateModel.objects.create(work_id=item_uuid, grade=grade)

    return Response(f'{key}  {file_name} {grade}')

