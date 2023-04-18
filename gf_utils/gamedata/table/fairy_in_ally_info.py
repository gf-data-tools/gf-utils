from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class FairyInAllyInfoInstance:
    id: str  # '1'
    fairy_id: str  # '2'
    fairy_lv: str  # '1'
    quality_lv: str  # '1'
    skill_lv: str  # '1'
    passive_skill: str  # '910101'
    equip_id: str  # '0'
    mod: str  # '0'


class FairyInAllyInfo(ConfigTable):
    name = "fairy_in_ally_info"

    def add_instance(self, k):
        return FairyInAllyInfoInstance(**self._data[k])
