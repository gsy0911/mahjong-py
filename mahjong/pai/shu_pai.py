"""
数牌: shu pai
"""
from .pai import Pai, PaiEnum


class ShuPai(Pai):

    def __init__(self, number: int):
        super().__init__(pai_enum=PaiEnum.SHU_PAI)
        self.number = number

    def get_character(self):
        pass


class WanZi(ShuPai):
    """
    萬子
    """

    def __init__(self, number: int):
        super().__init__(number=number)
        self.priority = 10 + number

    def get_character(self):
        return ["萬", str(self.number)]


class TongZi(ShuPai):
    """
    筒子
    """

    def __init__(self, number: int):
        super().__init__(number=number)
        self.priority = 20 + number

    def get_character(self):
        return ["筒", str(self.number)]


class SuoZi(ShuPai):
    """
    索子
    """

    def __init__(self, number: int):
        super().__init__(number=number)
        self.priority = 30 + number

    def get_character(self):
        return ["索", str(self.number)]
