from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SangvisChipSkillInstance:
    id: int  # 3001
    trigger_target_type: str  # ''
    trigger_range: str  # ''
    trigger_formula: str  # ''
    target_type: str  # '4,5,6'
    target_range: int  # 2
    battle_skill: str  # '610004'
    code: str  # 'SpotTarget0'


class SangvisChipSkill(ConfigTable):
    name = "sangvis_chip_skill"

    def add_instance(self, k):
        return SangvisChipSkillInstance(**self._data[k])
