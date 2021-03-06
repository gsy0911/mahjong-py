"""
字牌: zi pai
"""
from typing import List
from .pai import Pai, PaiEnum, ZiPaiEnum, FengPaiEnum, SanYuanPaiEnum


class ZiPai(Pai):
    def __init__(self, zi_pai_enum: ZiPaiEnum):
        super().__init__(pai_enum=PaiEnum.ZI_PAI)
        self.zi_pai_enum = zi_pai_enum

    def get_character(self):
        pass

    @staticmethod
    def of(inputs: str) -> List[Pai]:
        pass

    def check_shu_pai_number(self, number: int) -> bool:
        return False

    def check_zi_pai_char(self, char: str) -> bool:
        return False


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

    @staticmethod
    def of(inputs: str) -> List[Pai]:
        pai_list = []
        for s in inputs:
            if s == "d":
                pai_list.append(FengPai(feng_pai_enum=FengPaiEnum.DONG))
            elif s == "n":
                pai_list.append(FengPai(feng_pai_enum=FengPaiEnum.NAN))
            elif s == "x":
                pai_list.append(FengPai(feng_pai_enum=FengPaiEnum.XI))
            elif s == "b":
                pai_list.append(FengPai(feng_pai_enum=FengPaiEnum.BEI))
        return pai_list


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

    @staticmethod
    def of(inputs: str) -> List[Pai]:
        pai_list = []
        for s in inputs:
            if s == "b":
                pai_list.append(SanYuanPai(san_yuan_pai_enum=SanYuanPaiEnum.BAI_BAN))
            elif s == "f":
                pai_list.append(SanYuanPai(san_yuan_pai_enum=SanYuanPaiEnum.LU_FA))
            elif s == "z":
                pai_list.append(SanYuanPai(san_yuan_pai_enum=SanYuanPaiEnum.HONG_ZHONG))
        return pai_list
