from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SquadChipExpInstance:
    lv: int  # 1
    exp: int  # 50
    strength_coef: int  # 108


class SquadChipExp(ConfigTable):
    name = "squad_chip_exp"

    def add_instance(self, k):
        return SquadChipExpInstance(**self._data[k])
