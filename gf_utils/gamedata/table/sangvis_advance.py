from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SangvisAdvanceInstance:
    lv: int  # 1
    star1: str  # ''
    star2: str  # ''
    star3: str  # ''
    unlock_lv: int  # 1
    advance_hp: int  # 80
    advance_pow: int  # 80
    advance_rate: int  # 80
    advance_hit: int  # 80
    advance_dodge: int  # 80
    advance_armor: int  # 80


class SangvisAdvance(ConfigTable):
    name = "sangvis_advance"

    def add_instance(self, k):
        return SangvisAdvanceInstance(**self._data[k])
