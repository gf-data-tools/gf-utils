from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EquipExpInfoInstance:
    level: str  # '1'
    exp: str  # '50'


class EquipExpInfo(ConfigTable):
    name = "equip_exp_info"

    def add_instance(self, k):
        return EquipExpInfoInstance(**self._data[k])
