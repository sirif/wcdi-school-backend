# from home_work_checker.base_estimator import BaseEstimator
from algebra import A1


class HomeWorkChecker:

    def __init__(self, work_dir) -> None:
        self.__check_dict__: dict = {A1(work_dir=work_dir).name(): A1(work_dir=work_dir)}
        # self.__check_dict__[A1.name] = A1.check



    def check(self, key:str, item_uuid)->int:
        # альтернативно можно так
        # result = self.__check_dict__.get(key).check(item_uuid) if self.__check_dict__.get(key) else 0

        if check_inst := self.__check_dict__.get(key):
            return check_inst.check(item_uuid)
        return 0
    
        
if __name__ == "__main__":
    # print(A1("123").name())
    HWC = HomeWorkChecker("123")
    # a = A1("123")
    print(HWC.check("Алгебра-1", "b1ca416b-69b5-4922-a512-825f96736c11"))
