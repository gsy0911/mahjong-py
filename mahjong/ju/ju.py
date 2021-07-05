"""
局: ju
"""
import random
from typing import List, Optional

from mahjong.pai import Pai, WanZi, SuoZi, TongZi, FengPai, SanYuanPai, FengPaiEnum, SanYuanPaiEnum
from .bi_pai import Zhuang, BiPai


class Ju:
    """
    Placement:

        西[2]
    北[3]    南[1]
        東[0]

    index:

         [0 - 17]
    [17            [0
     |              |
    0]             17]
        [17 - 0]

    Dice:
             [3,7,11]
    [4,8,12]         [2,6,10]
             [5,9]
    """

    def __init__(self, dice_sum: Optional[int] = None):
        bi_bai_list = self.create_bi_pai()
        # 壁牌: bi_pai
        self.bi_pai_tong = bi_bai_list[0].zhuang_list
        self.bi_pai_nan = bi_bai_list[1].zhuang_list
        self.bi_pai_xi = bi_bai_list[2].zhuang_list
        self.bi_pai_bei = bi_bai_list[3].zhuang_list

        if dice_sum is None:
            dice_sum = 8
        # 王牌: wang_pai
        self.wang_pai, self.fixed_bi_pai = self.get_wang_pai_and_fixed_bi_pai(
            dice_sum=dice_sum,
            bi_pai_tong=self.bi_pai_tong,
            bi_pai_nan=self.bi_pai_nan,
            bi_pai_xi=self.bi_pai_xi,
            bi_pai_bei=self.bi_pai_bei)

    @staticmethod
    def xi_pai() -> List[Pai]:
        all_pai = []
        for _ in range(4):
            for i in range(1, 10):
                all_pai.append(WanZi(i))
                all_pai.append(SuoZi(i))
                all_pai.append(TongZi(i))

            for feng_pai in FengPaiEnum:
                all_pai.append(FengPai(feng_pai))

            for san_yuan_pai in SanYuanPaiEnum:
                all_pai.append(SanYuanPai(san_yuan_pai))

        return random.sample(all_pai, len(all_pai))

    @staticmethod
    def create_zhuang() -> List[Zhuang]:
        all_pai = Ju.xi_pai()
        zhuang_list = []
        for t in range(0, len(all_pai), 2):
            zhuang_list.append(Zhuang(upper_pai=all_pai[t], lower_pai=all_pai[t + 1]))

        return zhuang_list

    @staticmethod
    def create_bi_pai() -> List[BiPai]:
        zhuang_list = Ju.create_zhuang()
        bi_pai_list = []
        for t in range(0, len(zhuang_list), 17):
            bi_pai_list.append(BiPai(zhuang_list=zhuang_list[t:t+17]))
        return bi_pai_list

    @staticmethod
    def get_wang_pai_and_fixed_bi_pai(
            dice_sum: int,
            bi_pai_tong: List[Zhuang],
            bi_pai_nan: List[Zhuang],
            bi_pai_xi: List[Zhuang],
            bi_pai_bei: List[Zhuang]) -> (List[Zhuang], List[Zhuang]):
        fixed_bi_pai: List[Zhuang] = []

        if dice_sum in [5, 9]:
            fixed_bi_pai.extend(bi_pai_tong[dice_sum:])
            fixed_bi_pai.extend(bi_pai_bei)
            fixed_bi_pai.extend(bi_pai_xi)
            fixed_bi_pai.extend(bi_pai_nan)
            fixed_bi_pai.extend(bi_pai_tong[:dice_sum])
        elif dice_sum in [2, 6, 10]:
            fixed_bi_pai.extend(bi_pai_nan[dice_sum:])
            fixed_bi_pai.extend(bi_pai_tong)
            fixed_bi_pai.extend(bi_pai_bei)
            fixed_bi_pai.extend(bi_pai_xi)
            fixed_bi_pai.extend(bi_pai_nan[:dice_sum])
        elif dice_sum in [3, 7, 11]:
            fixed_bi_pai.extend(bi_pai_xi[dice_sum:])
            fixed_bi_pai.extend(bi_pai_nan)
            fixed_bi_pai.extend(bi_pai_tong)
            fixed_bi_pai.extend(bi_pai_bei)
            fixed_bi_pai.extend(bi_pai_xi[:dice_sum])
        elif dice_sum in [4, 8, 12]:
            fixed_bi_pai.extend(bi_pai_bei[dice_sum:])
            fixed_bi_pai.extend(bi_pai_xi)
            fixed_bi_pai.extend(bi_pai_nan)
            fixed_bi_pai.extend(bi_pai_tong)
            fixed_bi_pai.extend(bi_pai_bei[:dice_sum])

        return fixed_bi_pai[-7:], fixed_bi_pai[:-7]
