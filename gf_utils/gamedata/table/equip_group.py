from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class EquipGroupInstance:
    id: int  # 1
    name: str  # 'SHD定制"V"'
    des: str  # '使用了全套SHD特殊装备的特工维克托将获得极强的队伍辅助能力,提升队伍整体的生存能力。'
    code: str  # 'EgroupVec'
    equip_unit: str  # '199,200,201'
    group_skill: str  # '2:992050,3:992051'


class EquipGroup(ConfigTable):
    name = "equip_group"

    def add_instance(self, k):
        return EquipGroupInstance(**self._data[k])
