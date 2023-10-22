from os import path as os_path
from abc import abstractmethod


class BaseEstimator:

    @abstractmethod
    def __init__(self) -> None:
        self.__discipline__: str = ""
        self.__work_number__: int = 0

    def name(self):
        return f'{self.__discipline__}-{self.__work_number__}'

    @abstractmethod
    def check(self, file_name: os_path) -> int:
        pass
