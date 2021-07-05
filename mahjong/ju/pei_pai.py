"""
配牌: pei pai
"""
from typing import List
from mahjong.pai import Pai


class PeiPai:
    """
    配牌: pei pai
    """

    def __init__(self, initial_pei_pai: List[Pai]):
        self.pei_pai: List[Pai] = initial_pei_pai

    def __str__(self):
        return "|".join([str(pai) for pai in sorted(self.pei_pai, key=lambda pai: pai.priority)])
