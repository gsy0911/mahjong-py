"""
牌: pai
"""

from enum import Enum


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
    DONG = auto()
    # 南
    NAN = auto()
    # 西
    XI = auto()
    # 北
    BEI = auto()


class SanYuanPaiEnum(Enum):
    # 白板
    BAI_BAN = auto()
    # 緑發
    LU_FA = auto()
    # 紅中
    HONG_ZHONG = auto()


class Pai:

    def __init__(self, pai_enum: PaiEnum):
        self.pai_enum = pai_enum
