from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FairyInAllyInstance:
    id: int  # 1
    fairy_id: int  # 2
    fairy_lv: int  # 1
    quality_lv: int  # 1
    skill_lv: int  # 1
    passive_skill: int  # 910101
    equip_id: int  # 0
    mod: int  # 0


class FairyInAlly(ConfigTable):
    name = "fairy_in_ally"

    def add_instance(self, k):
        return FairyInAllyInstance(**self._data[k])
