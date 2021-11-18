"""
壁牌: bi pai
山: shan
"""
from dataclasses import dataclass
from typing import List
from mahjong.domain.pai import Pai


@dataclass(frozen=True)
class Zhuang:
    """
    幢
    """

    upper_pai: Pai
    lower_pai: Pai

    def get_pai(self) -> List[Pai]:
        return [self.upper_pai, self.lower_pai]

    def __str__(self):
        return f"upper: {str(self.upper_pai)}, lower: {str(self.lower_pai)}"


@dataclass(frozen=True)
class BiPai:
    """
    壁牌
    """

    zhuang_list: List[Zhuang]

    def __str__(self):
        return "\n".join([f"- {idx+1}: {str(zhuang)}" for idx, zhuang in enumerate(self.zhuang_list)])
