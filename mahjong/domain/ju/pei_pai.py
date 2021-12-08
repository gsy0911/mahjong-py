"""
配牌: pei pai
"""
from dataclasses import dataclass
from typing import List, Optional

from mahjong.domain.pai import FengPai, Pai, SanYuanPai, SuoZi, TongZi, WanZi


@dataclass(frozen=True)
class PeiPai:
    """
    配牌: pei pai
    """

    pei_pai: List[Pai]

    def __str__(self):
        return "|".join([str(pai) for pai in sorted(self.pei_pai, key=lambda pai: pai.priority)])

    @staticmethod
    def of(
        wang_zi: Optional[str] = None,
        tong_zi: Optional[str] = None,
        suo_zi: Optional[str] = None,
        feng_pai: Optional[str] = None,
        san_yuan_pai: Optional[str] = None,
    ):
        pei_pai = []
        if wang_zi:
            pei_pai.extend(WanZi.list_of(wang_zi))
        if tong_zi:
            pei_pai.extend(TongZi.list_of(tong_zi))
        if suo_zi:
            pei_pai.extend(SuoZi.list_of(suo_zi))
        if feng_pai:
            pei_pai.extend(FengPai.list_of(feng_pai))
        if san_yuan_pai:
            pei_pai.extend(SanYuanPai.list_of(san_yuan_pai))

        return PeiPai(pei_pai=pei_pai)
