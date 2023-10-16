from base_estimator import BaseEstimator
from uuid import uuid4

class A1(BaseEstimator):
        
    def __init__(self, work_dir: str) -> None:
        self.__discipline__:str = "Алгебра"
        self.__work_number__:int = 1
        self.__work_dir__ = work_dir

    def check(self, work_uuid:uuid4):
        file_name = BaseEstimator.fill_filename(work_dir=self.__work_dir__, work_uuid=work_uuid)
        return file_name
    

# 1+2=3
# 2+3=6
# 3+4=7
# 10+1=11
# 11+12=23
