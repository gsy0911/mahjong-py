"""
役
"""
from abc import abstractmethod
from typing import List
from mahjong.pai import Pai


class Hand:
    def __init__(self, hand_name: str, pei_pai: List[Pai]):
        self.pei_pai = pei_pai
        self.hand_name = hand_name

    @abstractmethod
    def is_hu_le(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def is_ting_pai(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def is_yi_xian_ting(self) -> bool:
        raise NotImplementedError()

    def decode_shun_zi(self):
        """
        順子

        """
