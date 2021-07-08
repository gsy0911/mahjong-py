"""
面子: mian_zi
"""
from typing import List
from mahjong.pai import Pai


class MianZi:
    def __init__(self, pai_list: List[Pai], pai_num_limit: int):
        self.pai_list = pai_list
        assert len(pai_list) <= pai_num_limit


class ShunZi(MianZi):
    """
    順子
    """
    def __init__(self, pai_list: List[Pai]):
        super().__init__(pai_list=pai_list, pai_num_limit=3)


class KeZi(MianZi):
    """
    刻子
    """
    def __init__(self, pai_list: List[Pai]):
        super().__init__(pai_list=pai_list, pai_num_limit=3)


class GangZi(MianZi):
    """
    槓子
    """
    def __init__(self, pai_list: List[Pai]):
        super().__init__(pai_list=pai_list, pai_num_limit=4)


class DuiZi(MianZi):
    """
    対子
    """
    def __init__(self, pai_list: List[Pai]):
        super().__init__(pai_list=pai_list, pai_num_limit=2)


class TaZi(MianZi):
    """
    塔子
    """
    def __init__(self, pai_list: List[Pai]):
        super().__init__(pai_list=pai_list, pai_num_limit=2)
