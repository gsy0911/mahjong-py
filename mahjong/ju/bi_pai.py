"""
壁牌: bi pai
山: shan
"""
from typing import List
from mahjong.pai import Pai


class Zhuang:
    """
    幢
    """

    def __init__(self, upper_pai: Pai, lower_pai: Pai):
        self.upper_pai = upper_pai
        self.lower_pai = lower_pai

    def get_pai(self) -> List[Pai]:
        return [self.upper_pai, self.lower_pai]

    def __str__(self):
        return f"upper: {str(self.upper_pai)}, lower: {str(self.lower_pai)}"


class BiPai:
    """
    壁牌
    """

    def __init__(self, zhuang_list: List[Zhuang]):
        self.zhuang_list = zhuang_list

    def __str__(self):
        return "\n".join(
            [f"- {idx+1}: {str(zhuang)}" for idx, zhuang in enumerate(self.zhuang_list)]
        )
