"""
字牌: zi pai
"""

from .pai import Pai, PaiEnum, ZiPaiEnum, FengPaiEnum, SanYuanPaiEnum


class ZiPai(Pai):

    def __init__(self, zi_pai_enum: ZiPaiEnum):
        super().__init__(pai_enum=PaiEnum.ZI_PAI)
        self.zi_pai_enum = zi_pai_enum

    def get_character(self):
        pass


class FengPai(ZiPai):

    def __init__(self, feng_pai_enum: FengPaiEnum):
        super().__init__(zi_pai_enum=ZiPaiEnum.FENG_PAI)
        self.feng_pai_enum = feng_pai_enum

        if self.feng_pai_enum is FengPaiEnum.DONG:
            self.priority = 50
        elif self.feng_pai_enum is FengPaiEnum.NAN:
            self.priority = 51
        elif self.feng_pai_enum is FengPaiEnum.XI:
            self.priority = 52
        elif self.feng_pai_enum is FengPaiEnum.BEI:
            self.priority = 53

    def get_character(self):
        return [self.feng_pai_enum.value]


class SanYuanPai(ZiPai):

    def __init__(self, san_yuan_pai_enum: SanYuanPaiEnum):
        super().__init__(zi_pai_enum=ZiPaiEnum.SAN_YUAN_PAI)
        self.san_yuan_pai_enum = san_yuan_pai_enum

        if self.san_yuan_pai_enum is SanYuanPaiEnum.BAI_BAN:
            self.priority = 60
        elif self.san_yuan_pai_enum is SanYuanPaiEnum.LU_FA:
            self.priority = 61
        elif self.san_yuan_pai_enum is SanYuanPaiEnum.HONG_ZHONG:
            self.priority = 62

    def get_character(self):
        return [self.san_yuan_pai_enum.value]
