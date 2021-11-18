"""
牌: pai
"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Union


class PaiEnum(Enum):
    SHU_PAI = auto()
    ZI_PAI = auto()
    HUA_PAI = auto()


class ZiPaiEnum(Enum):
    # 風牌
    FENG_PAI = auto()
    # 三元牌
    SAN_YUAN_PAI = auto()


class FengPaiEnum(Enum):
    # 東
    DONG = "東"
    # 南
    NAN = "南"
    # 西
    XI = "西"
    # 北
    BEI = "北"

    @staticmethod
    def chars() -> List[str]:
        return ["d", "n", "x", "b"]


class SanYuanPaiEnum(Enum):
    # 白板
    BAI_BAN = "白"
    # 緑發
    LU_FA = "發"
    # 紅中
    HONG_ZHONG = "中"

    @staticmethod
    def chars() -> List[str]:
        return ["b", "f", "z"]


@dataclass(frozen=True)
class Pai(metaclass=ABCMeta):
    pai_enum: PaiEnum
    priority: int

    @abstractmethod
    def get_character(self) -> List[str]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def of(s: Union[str, int]) -> "Pai":
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def list_of(inputs: str) -> List["Pai"]:
        raise NotImplementedError()

    def __str__(self):
        return "".join(self.get_character())

    def is_shu_pai(self) -> bool:
        return self.pai_enum == PaiEnum.SHU_PAI

    def is_zi_pai(self) -> bool:
        return self.pai_enum == PaiEnum.ZI_PAI

    @abstractmethod
    def check_shu_pai_number(self, number: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def check_zi_pai_char(self, char: str) -> bool:
        raise NotImplementedError()
