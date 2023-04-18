from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SquadAdvancedBonusInstance:
    id: int  # 10101
    group_id: int  # 101
    lv: int  # 1
    unlock_number: int  # 5
    assist_damage: int  # 4
    assist_reload: int  # 0
    assist_hit: int  # 6
    assist_def_break: int  # 0
    damage: int  # 0
    atk_speed: int  # 0
    hit: int  # 0
    def_: int  # 0


class SquadAdvancedBonus(ConfigTable):
    name = "squad_advanced_bonus"

    def add_instance(self, k):
        return SquadAdvancedBonusInstance(**self._data[k])
