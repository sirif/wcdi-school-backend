import os
from builtins import any, sorted
from os import path as os_path
import pandas as pd
from home_work_checker.base_estimator import BaseEstimator


class Ru1(BaseEstimator):

    def __init__(self):
        self.__discipline__: str = "Русский язык"
        self.__work_number__: int = 1

    def check(self, file_name: os_path) -> int:
        answers = [str(chr(v)) for v in range(ord('а'), ord('я') + 1)]
        answers.insert(6, 'ё')
        errors = 0
        df = pd.read_excel(file_name, header=None)
        letter_count = df.iloc[0, 1]
        if letter_count != len(answers):
            errors += 1

        result = list(df.iloc[2:2 + len(answers), 0].astype('str'))
        if result == answers:
            return 5 - errors
        elif sorted(result) == answers:
            errors += 1
            return 5 - errors
        else:
            for ans, res in zip(answers, result):
                if ans != res:
                    errors += 1
            return 2 if 5 - errors <= 2 else 5 - errors

'''
if __name__ == "__main__":
    answers = [str(chr(v)) for v in range(ord('а'), ord('я') + 1)]
    answers.insert(6, 'ё')
    errors = 0
    df = pd.read_excel('./../../data/ru_lang_1.xlsx', header=None)
    letter_count = df.iloc[0, 1]
    if letter_count != len(answers):
        errors += 1

    result = list(df.iloc[2:2 + len(answers), 0].astype('str'))
    if result == answers:
        print(5 - errors)
    elif sorted(result) == answers:
        errors += 1
        print(5 - errors)
    else:
        for ans, res in zip(answers, result):
            if ans != res:
                errors += 1
        print(2 if 5 - errors <= 2 else 5 - errors)
'''