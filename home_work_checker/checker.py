import os.path

from home_work_checker.algebra import *
from home_work_checker.ru_lang import *
from os import path as os_path


class HomeWorkChecker:

    def __init__(self) -> None:
        self.__check_dict__: dict = {A1().name(): A1(),
                                     Ru1().name(): Ru1()}
        # self.__check_dict__[A1.name] = A1.check

    def check(self, key: str, file_name: os_path) -> int:
        if not os.path.exists(file_name):
            return 0
        # альтернативно можно так
        # result = self.__check_dict__.get(key).check(item_uuid) if self.__check_dict__.get(key) else 0

        if check_inst := self.__check_dict__.get(key):
            return check_inst.check(file_name)
        return 0
    
        
if __name__ == "__main__":
    HWC = HomeWorkChecker()
    print(HWC.check("Алгебра-1", "b1ca416b-69b5-4922-a512-825f96736c11"))
