from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SkinInstance:
    id: int  # 1
    name: str  # '马卡洛夫-南瓜熊熊'
    extra: int  # 0
    fit_gun: int  # 8
    ai: int  # 40001
    voice: int  # 18
    is_hidden: int  # 0
    substitute_voice: str  # ''
    dialog: str  # '大家都躲哪了呢～要捣蛋咯～'
    note: str  # '这世界上，是没有妖魔鬼怪的，但是你们敢耽误我今天跟指挥官一起度过的万圣节活动……'
    explore_tag: str  # '3001'
    gift_position: str  # '54.2,-115.6'
    illustrator_cv: str  # '河马,上坂すみれ,'
    order: int  # 1
    class_id: int  # 1


class Skin(ConfigTable):
    name = "skin"

    def add_instance(self, k):
        return SkinInstance(**self._data[k])
