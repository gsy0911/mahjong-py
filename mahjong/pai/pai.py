"""
牌: pai
"""

from abc import abstractmethod
from enum import Enum, auto
from typing import List


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


class SanYuanPaiEnum(Enum):
    # 白板
    BAI_BAN = "白"
    # 緑發
    LU_FA = "發"
    # 紅中
    HONG_ZHONG = "中"


class Pai:
    def __init__(self, pai_enum: PaiEnum):
        self.pai_enum = pai_enum
        self.priority = 0

    @abstractmethod
    def get_character(self) -> List[str]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def of(inputs: str):
        raise NotImplementedError

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
