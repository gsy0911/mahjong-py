"""
字牌: zi pai
"""
from dataclasses import dataclass
from typing import List, Union
from .pai import Pai, PaiEnum, ZiPaiEnum, FengPaiEnum, SanYuanPaiEnum


@dataclass(frozen=True)
class ZiPai(Pai):
    zi_pai_enum: ZiPaiEnum

    def get_character(self):
        raise NotImplementedError()

    @staticmethod
    def of(s: Union[str, int]) -> Pai:
        pass

    @staticmethod
    def list_of(inputs: str) -> List[Pai]:
        pass

    def check_shu_pai_number(self, number: int) -> bool:
        return False

    def check_zi_pai_char(self, char: str) -> bool:
        return False


@dataclass(frozen=True)
class FengPai(ZiPai):
    feng_pai_enum: FengPaiEnum

    def get_character(self):
        return [self.feng_pai_enum.value]

    @staticmethod
    def of(s: str) -> Pai:
        if s == "d":
            priority = 50
            feng_pai_enum = FengPaiEnum.DONG
        elif s == "n":
            priority = 51
            feng_pai_enum = FengPaiEnum.NAN
        elif s == "x":
            priority = 52
            feng_pai_enum = FengPaiEnum.XI
        elif s == "b":
            priority = 53
            feng_pai_enum = FengPaiEnum.BEI
        else:
            raise ValueError()
        return FengPai(
            pai_enum=PaiEnum.ZI_PAI, zi_pai_enum=ZiPaiEnum.FENG_PAI, feng_pai_enum=feng_pai_enum, priority=priority
        )

    @staticmethod
    def list_of(inputs: str) -> List[Pai]:
        return [FengPai.of(s) for s in inputs]


@dataclass(frozen=True)
class SanYuanPai(ZiPai):
    san_yuan_pai_enum: SanYuanPaiEnum

    def get_character(self):
        return [self.san_yuan_pai_enum.value]

    @staticmethod
    def of(s: Union[str, int]) -> Pai:
        if s == "b":
            priority = 60
            san_yuan_pai_enum = SanYuanPaiEnum.BAI_BAN
        elif s == "f":
            priority = 61
            san_yuan_pai_enum = SanYuanPaiEnum.LU_FA
        elif s == "z":
            priority = 62
            san_yuan_pai_enum = SanYuanPaiEnum.HONG_ZHONG
        else:
            raise ValueError()
        return SanYuanPai(
            pai_enum=PaiEnum.ZI_PAI,
            zi_pai_enum=ZiPaiEnum.SAN_YUAN_PAI,
            san_yuan_pai_enum=san_yuan_pai_enum,
            priority=priority,
        )

    @staticmethod
    def list_of(inputs: str) -> List[Pai]:
        return [SanYuanPai.of(s) for s in inputs]
