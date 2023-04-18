from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class EquipTypeInstance:
    type: int  # 0
    name: str  # '没有'
    category: int  # 0
    code: str  # ''
    fit_gun_type: str  # '0'
    des: str  # '无'


class EquipType(ConfigTable):
    name = "equip_type"

    def add_instance(self, k):
        return EquipTypeInstance(**self._data[k])
