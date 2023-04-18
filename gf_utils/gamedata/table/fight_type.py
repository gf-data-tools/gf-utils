from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class FightTypeInstance:
    id: int  # 1
    name: str  # '普通'
    code: str  # 'com_war'
    desc: str  # '普通战斗'


class FightType(ConfigTable):
    name = "fight_type"

    def add_instance(self, k):
        return FightTypeInstance(**self._data[k])
