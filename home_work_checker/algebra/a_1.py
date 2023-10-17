from os import path as os_path
from home_work_checker.base_estimator import BaseEstimator


class A1(BaseEstimator):

    def __init__(self) -> None:
        self.__discipline__: str = "Алгебра"
        self.__work_number__: int = 1

    def check(self, file_name: os_path) -> int:
        # file_name = BaseEstimator.fill_filename(work_dir=self.__work_dir__, work_uuid=work_uuid)
        return 4
    

# 1+2=3
# 2+3=6
# 3+4=7
# 10+1=11
# 11+12=23
