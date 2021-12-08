"""
役
"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import List

from mahjong.domain.pai import Pai


@dataclass(frozen=True)
class Hand(metaclass=ABCMeta):
    hand_name: str
    pei_pai: List[Pai]

    @staticmethod
    @abstractmethod
    def of(pei_pai: List[Pai]):
        raise NotImplementedError()

    @abstractmethod
    def is_hu_le(self) -> bool:
        """
        和了：アガり

        Returns:

        """
        raise NotImplementedError()

    @abstractmethod
    def is_ting_pai(self) -> bool:
        """
        聴牌：テンパイ

        Returns:

        """
        raise NotImplementedError()

    @abstractmethod
    def is_yi_xian_ting(self) -> bool:
        """
        一向聴：イーシャンテン

        Returns:

        """
        raise NotImplementedError()

    def decode_shun_zi(self):
        """
        順子

        """
