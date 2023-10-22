import pandas as pd
from os import path as os_path
from home_work_checker.base_estimator import BaseEstimator


class A1(BaseEstimator):

    def __init__(self) -> None:
        self.__discipline__: str = "Алгебра"
        self.__work_number__: int = 1

    def check(self, file_name: os_path) -> int:
        answers = [10, 12, 11, 3, 4]
        errors = 0
        content = pd.read_excel(file_name, skiprows=[0])
        results = content.values[:, 4]
        for ans, res in zip(answers, results):
            try:
                if ans == int(res):
                    continue
                else:
                    errors += 1
            except Exception as e:
                print(str(e))
                errors += 1
        if errors == 0:
            return 5
        elif errors == 1:
            return 4
        elif errors == 2:
            return 3
        elif errors in [3, 4]:
            return 2
        else:
            return 1
        # return 0
    

# 1+2=3
# 2+3=6
# 3+4=7
# 10+1=11
# 11+12=23
