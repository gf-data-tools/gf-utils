from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class TheaterEffectInstance:
    id: int  # 41100
    name: str  # '前进基地'
    description: str  # '远征队梯队数量+0'
    icon: str  # 'TheaterBuff1'
    duration: int  # -1
    type: int  # 2
    formation_number: int  # 0
    ssoc_number: int  # 0
    hoc_number: int  # 0
    spare_gun_num: int  # 0
    spare_sangvis_cost: int  # 0
    spare_fairy_num: int  # 0


class TheaterEffect(ConfigTable):
    name = "theater_effect"

    def add_instance(self, k):
        return TheaterEffectInstance(**self._data[k])
