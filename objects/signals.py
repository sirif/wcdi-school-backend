from django.db.models.signals import post_delete, post_save
from objects.models.work_model import WorkModel
import os
from pathlib import Path
from django.dispatch import receiver
from django.conf import settings


def excel_validator(file_path: Path):
    print('signals_file_path: ', file_path)
    return True


@receiver(post_save, sender=WorkModel)
def on_work_load(**kwargs):
    work = kwargs['instance']
    file_path = Path(settings.MEDIA_ROOT, WorkModel.__name__.lower(), str(work.uuid))

    print("signal file_path:", file_path)

    if excel_validator(file_path):
        print("signals: ", file_path)
        # fill_image_data(file_path, work, kwargs['created'])
        # create_data_image_obj(file_path, )
    else:
        os.remove(file_path)
        raise Exception('Excel-файл не валиден')


@receiver(post_delete, sender=WorkModel)
def on_work_deleted(**kwargs):
    work = kwargs['instance']
    file_name = os.path.join(settings.MEDIA_ROOT, WorkModel.__name__.lower(), str(work.uuid))
    try:
        os.remove(file_name)
    except Exception as e:
        print(f'Ошибка удаления файла:{str(e)}')