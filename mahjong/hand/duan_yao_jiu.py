from .hand import Hand
from typing import List
from mahjong.pai import Pai


class DuanYaoJiu(Hand):

    def __init__(self, pei_pai: List[Pai]):
        super().__init__(hand_name="", pei_pai=pei_pai)

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
