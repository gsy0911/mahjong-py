"""
壁牌: bi pai
山: shan
"""
from typing import List
from mahjong.pai import Pai


class Zhuang:
    """
    幢
    """
    def __init__(self, upper_pai: Pai, lower_pai: Pai):
        self.upper_pai = upper_pai
        self.lower_pai = lower_pai


class BiPai:
    """
    壁牌
    """

    def __init__(self, zhuang_list: List[Zhuang]):
        self.zhuang_list = zhuang_list
