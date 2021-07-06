"""
数牌: shu pai
"""
from typing import List
from .pai import Pai, PaiEnum


class ShuPai(Pai):

    def __init__(self, number: int):
        super().__init__(pai_enum=PaiEnum.SHU_PAI)
        self.number = number

    def get_character(self):
        pass

    @staticmethod
    def of(inputs: str) -> List[Pai]:
        pass

    def check_shu_pai_number(self, number: int) -> bool:
        return self.number == number

    def check_zi_pai_char(self, char: str) -> bool:
        return False


class WanZi(ShuPai):
    """
    萬子
    """

    def __init__(self, number: int):
        super().__init__(number=number)
        self.priority = 10 + number

    def get_character(self):
        return ["萬", str(self.number)]

    @staticmethod
    def of(inputs: str) -> List[Pai]:
        pai_list = []
        for s in inputs:
            pai_list.append(WanZi(number=int(s)))
        return pai_list


class TongZi(ShuPai):
    """
    筒子
    """

    def __init__(self, number: int):
        super().__init__(number=number)
        self.priority = 20 + number

    def get_character(self):
        return ["筒", str(self.number)]

    @staticmethod
    def of(inputs: str) -> List[Pai]:
        pai_list = []
        for s in inputs:
            pai_list.append(TongZi(number=int(s)))
        return pai_list


class SuoZi(ShuPai):
    """
    索子
    """

    def __init__(self, number: int):
        super().__init__(number=number)
        self.priority = 30 + number

    def get_character(self):
        return ["索", str(self.number)]

    @staticmethod
    def of(inputs: str) -> List[Pai]:
        pai_list = []
        for s in inputs:
            pai_list.append(SuoZi(number=int(s)))
        return pai_list
