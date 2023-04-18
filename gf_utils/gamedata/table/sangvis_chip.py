from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SangvisChipInstance:
    id: int  # 1001
    name: str  # '夜战视野'
    unlock_furniture_level: int  # 0
    type: int  # 1
    equip_boss: int  # 0
    dev_specialitem_num: str  # ''
    code: str  # 'NightView'
    des: str  # '夜间作战时,额外为梯队提供1格视野。'
    dev_battery_num: int  # 1000
    dev_time: int  # 300
    active_special_skill: str  # ''
    active_special_skill_cd: str  # ''
    active_special_skill_cost: str  # ''
    active_mission_skill: str  # ''
    chip_skill: str  # ''
    passive_mission_skill: str  # '30001:1'
    special_skill_parameter: str  # ''
    night_view_percent: int  # 0
    dev_num: int  # 0
    dev_item_value: str  # ''


class SangvisChip(ConfigTable):
    name = "sangvis_chip"

    def add_instance(self, k):
        return SangvisChipInstance(**self._data[k])
