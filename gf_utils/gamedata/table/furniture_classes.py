from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class FurnitureClassesInstance:
    id: int  # 1
    name: str  # '万圣节'
    rank: int  # 5
    bonus_picture: str  # '3000'
    k_bonus: str  # '6:2000,9:5000,12:8000'
    bonus_number: int  # 15
    description: str  # '万圣节源自古凯尔特人的新年，孩子们装扮成鬼怪乞讨糖果，不给糖甚至会炸掉别人的房子，非常可怕。'
    bonus_description: str  # '集齐后宿舍内会出现意想不到的现象。'
    code: str  # 'ws2016_deco_small_icon'
    is_showed: int  # 1
    placement: int  # 1
    years: int  # 2016


class FurnitureClasses(ConfigTable):
    name = "furniture_classes"

    def add_instance(self, k):
        return FurnitureClassesInstance(**self._data[k])
