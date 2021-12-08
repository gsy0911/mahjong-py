from dataclasses import dataclass
from typing import List

from mahjong.domain.pai import Pai

from .hand import Hand


@dataclass(frozen=True)
class SanSeTongShun(Hand):
    @staticmethod
    def of(pei_pai: List[Pai]):
        return SanSeTongShun(hand_name="三色同順", pei_pai=pei_pai)

    def _hu_le_condition(self) -> bool:
        for p in self.pei_pai:
            if p.is_zi_pai():
                return False
            if p.check_shu_pai_number(number=1):
                return False
            if p.check_shu_pai_number(number=9):
                return False
        return True

    def is_hu_le(self) -> bool:
        return self._hu_le_condition()

    def is_ting_pai(self) -> bool:
        pass

    def is_yi_xian_ting(self) -> bool:
        pass
