"""
局: ju
"""
import random
from typing import List

from mahjong.pai import Pai, WanZi, SuoZi, TongZi, FengPai, SanYuanPai, FengPaiEnum, SanYuanPaiEnum
from .bi_pai import Zhuang, BiPai


class Ju:

    def __init__(self):
        pass

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
