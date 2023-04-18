from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EnemyStandardAttributeInstance:
    level: int  # 1
    maxlife: float  # 226.8
    pow: float  # 6.94
    dodge: float  # 2.14
    hit: float  # 3.33
    armor_piercing: float  # 3.0
    armor: float  # 30.72
    shield: float  # 1.0
    defense: float  # 336.0
    def_break: float  # 1.0


class EnemyStandardAttribute(ConfigTable):
    name = "enemy_standard_attribute"

    def add_instance(self, k):
        return EnemyStandardAttributeInstance(**self._data[k])
