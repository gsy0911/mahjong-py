"""
配牌: pei pai
"""
from typing import List
from mahjong.pai import Pai
from .bi_pai import Zhuang


class PeiPai:
    """
    配牌: pei pai
    """

    def __init__(self, initial_pei_pai: List[Pai]):
        self.pei_pai: List[Pai] = initial_pei_pai
