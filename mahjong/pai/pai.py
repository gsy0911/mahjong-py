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
    BAI_BAN = " "
    # 緑發
    LU_FA = "發"
    # 紅中
    HONG_ZHONG = "中"


class Pai:

    def __init__(self, pai_enum: PaiEnum):
        self.pai_enum = pai_enum

    @abstractmethod
    def get_character(self) -> List[str]:
        pass
