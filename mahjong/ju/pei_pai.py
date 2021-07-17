"""
配牌: pei pai
"""
from typing import List, Optional
from mahjong.pai import Pai, WanZi, TongZi, SuoZi, FengPai, SanYuanPai


class PeiPai:
    """
    配牌: pei pai
    """

    def __init__(self, initial_pei_pai: List[Pai]):
        self.pei_pai: List[Pai] = initial_pei_pai

    def __str__(self):
        return "|".join(
            [str(pai) for pai in sorted(self.pei_pai, key=lambda pai: pai.priority)]
        )

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
            pei_pai.extend(WanZi.of(wang_zi))
        if tong_zi:
            pei_pai.extend(TongZi.of(tong_zi))
        if suo_zi:
            pei_pai.extend(SuoZi.of(suo_zi))
        if feng_pai:
            pei_pai.extend(FengPai.of(feng_pai))
        if san_yuan_pai:
            pei_pai.extend(SanYuanPai.of(san_yuan_pai))

        return PeiPai(initial_pei_pai=pei_pai)
