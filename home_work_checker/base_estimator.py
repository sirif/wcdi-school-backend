from uuid import uuid4
# from django.conf import settings
from os import path
from abc import abstractmethod

class BaseEstimator:
    def __init__(self, work_dir: str) -> None:
        self.__discipline__:str = ""
        self.__work_number__:int = 0
        self.__work_dir__ = work_dir

    def name(self):
        return f'{self.__discipline__}-{self.__work_number__}'
    
    @staticmethod
    def fill_filename(work_dir: str, work_uuid: uuid4):
        return path.join(work_dir, work_uuid)
    
    @abstractmethod
    def check(self, work_uuid: uuid4) ->int:
        file_name = BaseEstimator.fill_filename(work_dir=self.__work_dir__, work_uuid=work_uuid)
        pass