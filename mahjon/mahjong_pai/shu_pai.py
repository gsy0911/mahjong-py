"""
数牌: shu pai
"""

from .pai import Pai, PaiEnum


class ShuPai(Pai):

    def __init__(self, number: int):
        super().__init__(pai_enum=PaiEnum.SHU_PAI)
        self.number = number


class WanZi(ShuPai):
    """
    萬子
    """
    pass


class TongZi(ShuPai):
    """
    筒子
    """
    pass


class SuoZi(ShuPai):
    """
    索子
    """
    pass
