"""
数牌: shu pai
"""

from dataclasses import dataclass
from typing import List, Union
from .pai import Pai, PaiEnum


@dataclass(frozen=True)
class ShuPai(Pai):
    number: int

    def get_character(self):
        pass

    @staticmethod
    def of(s: Union[str, int]) -> Pai:
        pass

    @staticmethod
    def list_of(inputs: str) -> List[Pai]:
        pass

    def check_shu_pai_number(self, number: int) -> bool:
        return self.number == number

    def check_zi_pai_char(self, char: str) -> bool:
        return False


@dataclass(frozen=True)
class WanZi(ShuPai):
    """
    萬子
    """

    def get_character(self):
        return ["萬", str(self.number)]

    @staticmethod
    def of(s: Union[str, int]) -> Pai:
        if type(s) is int:
            n = s
        elif type(s) is str:
            n = int(s)
        else:
            raise ValueError()
        return WanZi(number=n, priority=10 + n, pai_enum=PaiEnum.SHU_PAI)

    @staticmethod
    def list_of(inputs: str) -> List[Pai]:
        pai_list = []
        for s in inputs:
            pai_list.append(WanZi.of(s))
        return pai_list


@dataclass(frozen=True)
class TongZi(ShuPai):
    """
    筒子
    """

    def get_character(self):
        return ["筒", str(self.number)]

    @staticmethod
    def of(s: Union[str, int]) -> Pai:
        if type(s) is int:
            n = s
        elif type(s) is str:
            n = int(s)
        else:
            raise ValueError()
        return TongZi(number=n, priority=20 + n, pai_enum=PaiEnum.SHU_PAI)

    @staticmethod
    def list_of(inputs: str) -> List[Pai]:
        pai_list = []
        for s in inputs:
            pai_list.append(TongZi.of(s))
        return pai_list


@dataclass(frozen=True)
class SuoZi(ShuPai):
    """
    索子
    """

    def get_character(self):
        return ["索", str(self.number)]

    @staticmethod
    def of(s: Union[str, int]) -> Pai:
        if type(s) is int:
            n = s
        elif type(s) is str:
            n = int(s)
        else:
            raise ValueError()
        return SuoZi(number=n, priority=30 + n, pai_enum=PaiEnum.SHU_PAI)

    @staticmethod
    def list_of(inputs: str) -> List[Pai]:
        pai_list = []
        for s in inputs:
            pai_list.append(SuoZi.of(s))
        return pai_list
