from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class GunInAllyInstance:
    id: int  # 1
    gun_id: int  # 26
    gun_level: int  # 90
    location: int  # 1
    position: int  # 14
    life: int  # 795
    pow: int  # 16
    hit: int  # 10
    dodge: int  # 53
    rate: int  # 24
    skill1: int  # 9
    skill2: int  # 0
    number: int  # 5
    equip1: int  # 56
    equip2: int  # 57
    equip3: int  # 58
    skin: int  # 0
    eat_lv: int  # 90
    if_modification: int  # 0


class GunInAlly(ConfigTable):
    name = "gun_in_ally"

    def add_instance(self, k):
        return GunInAllyInstance(**self._data[k])
