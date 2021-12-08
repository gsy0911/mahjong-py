"""
面子: mian_zi
"""
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from typing import List
from mahjong.domain.pai import Pai


@dataclass(frozen=True)
class MianZi(metaclass=ABCMeta):
    pai_list: List[Pai]
    pai_num_limit: int

    def __post_init__(self):
        assert len(self.pai_list) <= self.pai_num_limit

    @staticmethod
    @abstractmethod
    def of(pai_list: List[Pai]):
        raise NotImplementedError()


@dataclass(frozen=True)
class ShunZi(MianZi):
    """
    順子
    """

    @staticmethod
    def of(pai_list: List[Pai]):
        return ShunZi(pai_list=pai_list, pai_num_limit=3)


@dataclass(frozen=True)
class KeZi(MianZi):
    """
    刻子
    """

    @staticmethod
    def of(pai_list: List[Pai]):
        return KeZi(pai_list=pai_list, pai_num_limit=3)


@dataclass(frozen=True)
class GangZi(MianZi):
    """
    槓子
    """

    @staticmethod
    def of(pai_list: List[Pai]):
        return GangZi(pai_list=pai_list, pai_num_limit=4)


@dataclass(frozen=True)
class DuiZi(MianZi):
    """
    対子
    """

    @staticmethod
    def of(pai_list: List[Pai]):
        return DuiZi(pai_list=pai_list, pai_num_limit=2)


@dataclass(frozen=True)
class TaZi(MianZi):
    """
    塔子
    """

    @staticmethod
    def of(pai_list: List[Pai]):
        return TaZi(pai_list=pai_list, pai_num_limit=2)
